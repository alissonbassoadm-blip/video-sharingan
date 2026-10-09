"""End-to-end test: synthetic reel with known camera/edit/audio -> analyze -> compare to ground truth.

Run:  pytest -q tests/
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "examples" / "synthetic"))

import camera_track  # noqa: E402
import check  # noqa: E402
import compare  # noqa: E402
import sharingan  # noqa: E402


@pytest.fixture(scope="session")
def synthetic(tmp_path_factory):
    d = tmp_path_factory.mktemp("synthetic")
    subprocess.run([sys.executable, str(ROOT / "examples" / "synthetic" / "make_synthetic.py"), str(d)], check=True)
    an = sharingan.analyze(str(d / "synthetic.mp4"), d / "out", title="Synthetic test reel")
    gt = json.loads((d / "ground_truth.json").read_text())
    return gt, an, d


def test_every_ground_truth_check_passes(synthetic):
    gt, an, _ = synthetic
    rows = check.checks(gt, an)
    failed = [r for r in rows if not r["ok"]]
    assert not failed, check.to_md(failed)


def test_outputs_written(synthetic):
    _, _, d = synthetic
    for p in ["analysis.json", "brief.md", "sheets/overview.png", "sheets/shots.png", "focus/focus_shot02.png"]:
        assert (d / "out" / p).exists(), p
    brief = (d / "out" / "brief.md").read_text()
    assert "Distilled spec" in brief and "## 9. Don't" in brief


def test_compare_self_passes(synthetic):
    _, an, _ = synthetic
    _, fails = compare.compare(an, an)
    assert fails == 0


def test_compare_catches_a_stopping_camera(synthetic):
    _, an, _ = synthetic
    ref = json.loads(json.dumps(an))
    for s in ref["camera"]["shots"]:  # pretend the reference never stops and never pulls out
        s["never_stops"] = True
        s["pull_out"]["detected"] = False
    ref["camera"]["summary"]["camera_never_stops"] = True
    _, fails = compare.compare(ref, an)
    assert fails >= 2  # our reel has a static shot, an eased shot and a pull-out


@pytest.mark.parametrize("name", ["linear", "power1.inOut", "power2.out", "power3.in", "sine.inOut"])
def test_ease_fit_recovers_curve(name):
    x = np.linspace(0, 1, 97)
    prog = camera_track.EASES[name](x)
    motion = np.diff(prog) * 1000
    assert camera_track.fit_ease(motion)["best"] == name
