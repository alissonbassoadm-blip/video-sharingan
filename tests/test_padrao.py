"""Checador do padrão de edição: roda sobre analysis.json, sem OpenCV."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import padrao  # noqa: E402

METAS = json.loads((ROOT / "padrao" / "metas.json").read_text())
BASE = json.loads((ROOT / "examples" / "synthetic" / "analysis.json").read_text())


def _reels(**edit):
    an = copy.deepcopy(BASE)
    an["source"].update(width=1080, height=1920, aspect=0.5625, fps=30.0, duration_s=40.0)
    an["edit"]["stats"].update(asl_s=2.2, max_shot_s=4.0, cuts_per_min=27)
    an["edit"]["shots"] = [{"index": 1, "start_s": 0.0, "dur_s": 4.0}]
    an["edit"]["stats"].update(edit)
    return an


def _status(rows, nome):
    return next(r[1] for r in rows if r[0].startswith(nome))


def test_reels_de_negocios_aprovado():
    fmt, rows = padrao.checar(_reels(), METAS, "negocios")
    assert fmt == "vertical"
    assert not [r for r in rows if r[1] == "FALHA"], rows


def test_ritmo_lento_reprova_negocios_mas_passa_familia():
    an = _reels(asl_s=4.5)
    assert _status(padrao.checar(an, METAS, "negocios")[1], "duração média") == "FALHA"
    assert _status(padrao.checar(an, METAS, "familia")[1], "duração média") == "OK"


def test_plano_longo_e_horizontal_reprovam():
    an = _reels()
    an["edit"]["shots"].append({"index": 2, "start_s": 10.0, "dur_s": 6.5})
    assert _status(padrao.checar(an, METAS, "negocios")[1], "plano mais longo") == "FALHA"
    _, rows = padrao.checar(BASE, METAS, "negocios")  # 1280x720
    assert _status(rows, "formato") == "FALHA"


def test_cli_exit_code(tmp_path):
    p = tmp_path / "a.json"
    p.write_text(json.dumps(_reels()))
    assert padrao.main([str(p), "--pilar", "negocios"]) == 0
    assert padrao.main([str(ROOT / "examples" / "synthetic" / "analysis.json"), "--pilar", "negocios"]) == 1
