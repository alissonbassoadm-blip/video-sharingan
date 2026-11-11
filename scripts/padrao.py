#!/usr/bin/env python3
"""padrao: confere um vídeo pessoal contra o padrão de edição (padrao/metas.json).

Lê o analysis.json gerado por `sharingan analyze` e checa formato, duração, ritmo de
cortes, plano mais longo, áudio e temperatura de cor contra as metas do pilar.
Só usa a biblioteca padrão: roda mesmo sem OpenCV, desde que o analysis.json exista.

uso:
  sharingan analyze meu-video.mp4 -o analise
  python3 scripts/padrao.py analise/analysis.json --pilar negocios [--formato vertical] [-o relatorio.md]

pilares: negocios | familia | palestras | palestra_inteira     sai com código 1 se alguma regra FALHA.
"""
import argparse
import json
import sys
from pathlib import Path

METAS = Path(__file__).resolve().parents[1] / "padrao" / "metas.json"


def checar(an, metas, pilar, formato=None):
    p = metas["pilares"][pilar]
    src, stats = an["source"], an["edit"]["stats"]
    shots = an["edit"].get("shots") or []
    au, look = an.get("audio") or {}, an.get("look") or {}
    rows = []

    def regra(nome, ok, meta, obtido, dura=True):
        rows.append((nome, "OK" if ok else ("FALHA" if dura else "ATENÇÃO"), meta, obtido))

    # formato: o informado, ou o mais próximo do aspecto do arquivo
    fmts = {k: metas["formatos"][k] for k in p["formatos"]}
    if formato is None:
        formato = min(fmts, key=lambda k: abs(fmts[k]["aspect"] - src["aspect"]))
    f = metas["formatos"][formato]
    regra(f"formato ({formato})", formato in p["formatos"] and abs(src["aspect"] - f["aspect"]) < 0.02,
          f"{f['largura']}x{f['altura']} em {', '.join(p['formatos'])}", f"{src['width']}x{src['height']}")
    regra("resolução", src["width"] >= f["largura"] and src["height"] >= f["altura"],
          f"≥ {f['largura']}x{f['altura']}", f"{src['width']}x{src['height']}", dura=False)
    regra("fps", abs(src["fps"] - f["fps"]) < 0.5, f["fps"], src["fps"], dura=False)

    lo, hi = p["duracao_s"]
    d = src["duration_s"]
    regra("duração", lo <= d <= hi, f"{lo}–{hi} s", f"{d:.1f} s")

    lo, hi = p["asl_s"]
    asl = stats["asl_s"]
    regra("duração média do plano (ASL)", lo <= asl <= hi, f"{lo}–{hi} s", f"{asl} s")
    longos = [s for s in shots if s["dur_s"] > p["plano_max_s"]]
    regra("plano mais longo", not longos, f"≤ {p['plano_max_s']} s",
          f"{stats['max_shot_s']} s" + (" (planos " + ", ".join(f"{s['index']}@{s['start_s']:.1f}s" for s in longos) + ")" if longos else ""))
    regra("cortes por minuto", stats["cuts_per_min"] >= p["cortes_por_min_min"],
          f"≥ {p['cortes_por_min_min']}", stats["cuts_per_min"], dura=False)

    if not src.get("has_audio"):
        regra("áudio", False, "trilha de áudio presente", "sem áudio")
    elif au:
        g = metas["audio_global"]
        regra("pico de áudio", au["peak_dbfs"] <= g["pico_max_dbfs"], f"≤ {g['pico_max_dbfs']} dBFS", f"{au['peak_dbfs']} dBFS")
        regra("volume médio (RMS)", g["rms_min_dbfs"] <= au["rms_dbfs"] <= g["rms_max_dbfs"],
              f"{g['rms_min_dbfs']} a {g['rms_max_dbfs']} dBFS", f"{au['rms_dbfs']} dBFS", dura=False)
        regra("silêncio (respiros/vazios)", au["silence_fraction"] <= p["silencio_max"],
              f"≤ {p['silencio_max']:.0%}", f"{au['silence_fraction']:.0%}", dura=False)
        regra("classe de áudio", au.get("class") in p["audio_classes"], " / ".join(p["audio_classes"]), au.get("class"), dura=False)

    grade = look.get("grade") or {}
    if "warm_minus_cool" in grade:
        lo, hi = p["temperatura"]
        w = grade["warm_minus_cool"]
        regra("temperatura de cor", lo <= w <= hi, f"{lo} a {hi} (quente − frio)", w, dura=False)
    if grade.get("crushed_whites"):
        regra("brancos estourados", False, "não", "sim (pele/janela estourada?)", dura=False)
    return formato, rows


def to_md(pilar_nome, formato, rows):
    falhas = sum(r[1] == "FALHA" for r in rows)
    md = [f"## Padrão: {pilar_nome} · {formato}", "", "| regra | resultado | meta | vídeo |", "|---|---|---|---|"]
    md += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    md += ["", "**Reprovado**: corrija as FALHAS, uma por vez, e meça de novo." if falhas else
           "**Aprovado** nas regras medíveis. Agora rode o checklist humano (padrao/checklist.md)."]
    return "\n".join(md), falhas


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("analysis")
    ap.add_argument("--pilar", required=True, help="chave em metas.json: negocios | familia | palestras | palestra_inteira")
    ap.add_argument("--formato", choices=["vertical", "feed", "youtube"])
    ap.add_argument("--metas", default=str(METAS))
    ap.add_argument("-o", "--out")
    a = ap.parse_args(argv)
    metas = json.loads(Path(a.metas).read_text())
    if a.pilar not in metas["pilares"]:
        ap.error(f"pilar desconhecido: {a.pilar} (opções: {', '.join(metas['pilares'])})")
    an = json.loads(Path(a.analysis).read_text())
    formato, rows = checar(an, metas, a.pilar, a.formato)
    md, falhas = to_md(metas["pilares"][a.pilar]["nome"], formato, rows)
    print(md)
    if a.out:
        Path(a.out).write_text(md + "\n")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
