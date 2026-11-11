# Manual de edição: posts e vídeos pessoais

Três pilares, uma identidade. Cada regra aqui é um número ou um sim/não, para que qualquer editor
(você, um freelancer ou uma IA) entregue o mesmo resultado. O que é medível está em
[`metas.json`](metas.json) e é conferido por `scripts/padrao.py`. O resto está no
[`checklist.md`](checklist.md).

> **Antes de usar: preencha a seção 1.** Fontes, cores e @ abaixo são valores provisórios. Um padrão
> com valores provisórios vira três padrões diferentes em um mês.

---

## 0. A lógica (e onde ela pode falhar)

| pilar | o que entrega | o que mede sucesso | risco principal |
|---|---|---|---|
| **Negócios** | autoridade: você sabe algo útil | salvamentos, compartilhamentos, DMs | virar "coach genérico": frase motivacional sem número, caso ou método |
| **Família / vida de empresário** | conexão: quem é a pessoa por trás | comentários, tempo de visualização | parecer encenado, ou expor filhos, casa e rotina |
| **Palestras** | prova: outras pessoas pagam para ouvir você | contratações, convites, seguidores novos | corte mal gravado (áudio de câmera, plano aberto) que reduz a autoridade |

Proporção sugerida para começar: **50 % negócios · 30 % família · 20 % palestras**. Ajuste pelos números
depois de 8 semanas, não por intuição. Se você palestra pouco, 20 % de cortes vai esgotar o material:
um bom palco rende de 6 a 10 cortes, não 40.

**Regra de ouro:** o mesmo vídeo não pode servir aos três pilares. Um vídeo de família com CTA de venda
perde a conexão e não vende.

---

## 1. Identidade fixa (igual nos três pilares)

Preencha uma vez e não mude por 6 meses.

| item | valor | observação |
|---|---|---|
| Fonte de legenda | `Montserrat ExtraBold` *(provisório)* | uma única família; peso 800 para legenda, 600 para texto de apoio |
| Fonte de título/capa | `Montserrat Black` *(provisório)* | caixa alta, no máximo 5 palavras |
| Cor primária | `#______` | destaque da palavra-chave na legenda |
| Cor secundária | `#______` | selo do pilar e barras |
| Texto | `#FFFFFF` com contorno ou sombra preta 60 % | nunca texto sem contorno sobre vídeo |
| Assinatura | `@seuperfil` | só na capa e no card final, nunca marca d'água fixa |
| Card final | 1,0 s, fundo da cor primária, `@` + uma frase | opcional em negócios e palestras; **nunca** em família |

### Selo de pilar (consistência no grid)

Uma etiqueta pequena no canto superior esquerdo da **capa** (não no vídeo):

- Negócios: `NEGÓCIOS` · cor primária
- Família: sem selo (o selo deixaria o post com cara de campanha)
- Palestras: `NO PALCO` · cor secundária

---

## 2. Formatos e área segura

| formato | resolução | fps | uso |
|---|---|---|---|
| Vertical 9:16 | 1080 × 1920 | 30 | Reels, TikTok, Shorts, Status. **Formato principal** |
| Feed 4:5 | 1080 × 1350 | 30 | carrossel e vídeo no feed |
| Horizontal 16:9 | 1920 × 1080 | 30 | palestra inteira no YouTube |

Exportação: H.264, 15–20 Mbps (vertical), AAC 320 kbps 48 kHz. Grave em 30 fps (ou 60 se for usar
câmera lenta). Não misture 24 e 30 fps na mesma timeline.

**Área segura no 9:16** (a interface do app cobre o resto):
- topo: 220 px livres
- base: 420 px livres (legenda do app, botões)
- laterais: 60 px à esquerda, 160 px à direita (ícones de curtir/comentar)
- **Legenda dinâmica:** centro da linha de base entre 1150 e 1300 px a partir do topo (logo abaixo do queixo)
- Rosto: olhos a ~1/3 da altura (≈ 640 px a partir do topo)

---

## 3. Regras por pilar

### 3.1 Negócios e empreendedorismo: ritmo de autoridade

| item | regra |
|---|---|
| Duração | 25–75 s (alvo: 40 s) |
| Gancho | frase final do vídeo nos primeiros **1,5 s**, falada e escrita na tela. Sem "oi, pessoal", sem logo de abertura |
| Ritmo | duração média do plano entre 1,4 e 3,0 s; **nenhum plano acima de 5 s** sem mudança (corte, punch-in ou B-roll) |
| Cortes de silêncio | remova pausas maiores que 0,25 s; mantenha respiração natural (não corte a palavra) |
| Punch-in | alterne enquadramento a cada 2–3 frases: 100 % → 115 % → 100 %. No máximo 130 % para não perder nitidez em 4K → 1080 |
| B-roll | 1 inserção a cada 8–12 s: tela de planilha, número, escritório, equipe. Sempre ilustra a frase, nunca decora |
| Legenda | dinâmica, 2–4 palavras por vez, palavra-chave na cor primária (no máximo 1 por bloco) |
| Texto de apoio | números grandes na tela quando você falar um número ("R$ 2 mi", "3 anos") |
| Música | instrumental, sem letra, 90–120 BPM, **−20 dB abaixo da voz** |
| SFX | só em textos que entram (pop/click curto). No máximo 1 a cada 5 s. Sem "whoosh" em todo corte |
| Cor | neutra; pele natural; contraste médio. Nada de LUT de cinema |
| Fim | 1 CTA único e específico ("comenta PLANILHA que eu te mando"), não três |

**Estrutura:** gancho (0–2 s) → problema em 1 frase → 2 ou 3 pontos com exemplo real → virada/lição → CTA.

### 3.2 Vida de empresário e família: ritmo de conexão

| item | regra |
|---|---|
| Duração | 15–60 s |
| Gancho | imagem, não frase: o primeiro plano tem que ser o mais forte (abraço, olhar, momento real). Texto opcional, curto |
| Ritmo | plano médio entre 2,0 e 5,0 s; plano máximo 8 s. Deixe o momento respirar |
| Som | **som ambiente real** sempre presente (risada, conversa) a −12 dB; música por baixo, com letra permitida |
| Legenda | menor e discreta (peso 600, sem cor de destaque). Se não houver fala, não force texto |
| Movimento | sem punch-in agressivo, sem zoom digital, sem SFX. Câmera na mão está ok; tremida não |
| Cor | levemente quente (+300–500 K) e consistente entre os posts |
| Fim | sem CTA de venda e sem card final. No máximo uma pergunta ("vocês também…?") |

**Privacidade (obrigatório, não estético):**
- Rosto de filhos menores: só com acordo do outro responsável. Na dúvida, de costas, mãos ou fora de foco.
- Nunca mostre: fachada da casa, placa do carro, uniforme ou nome da escola, rotina com horário fixo, localização em tempo real (poste depois).
- Revise o fundo de cada plano: correspondência, tela de celular, documentos.

### 3.3 Palestras: prova de palco

**Captação (é aqui que se ganha ou perde o pilar):**
- Áudio da **mesa de som ou microfone de lapela próprio**. Áudio da câmera, gravado do fundo da sala, inviabiliza o corte.
- Duas câmeras: uma **fechada** (peito para cima, para o 9:16) e uma **aberta** (palco + plateia). Com uma câmera só, grave em 4K para reenquadrar.
- Uma terceira fonte, mesmo um celular, voltada para a **plateia** (reações, risadas, aplausos).

| item | regra |
|---|---|
| Duração do corte | 30–90 s, uma ideia por corte |
| Gancho | a frase mais forte do trecho no início (pode antecipar e depois voltar). Nunca comece em "bom dia" ou em aplauso |
| Ritmo | plano médio entre 2,0 e 4,5 s (alternando fechada/aberta/plateia); plano máximo 7 s |
| Prova social | 1 plano de plateia a cada 15–20 s; plano aberto mostrando a sala cheia **nos primeiros 5 s** |
| Lower third | nome do evento + cidade + ano, 3 s, entra no segundo 2–4 |
| Legenda | igual à de negócios (mesma marca), mantendo pausas de efeito do palco |
| Música | só se o trecho não tiver plateia audível; sempre −22 dB abaixo da voz |
| Cor | iluminação de palco costuma ficar amarela ou magenta: corrija pele primeiro, depois o resto |
| Palestra inteira | YouTube 16:9, capítulos na descrição, cortes linkando para ela |

---

## 4. Áudio (vale para todos)

- Voz: **−14 LUFS integrado** na exportação, pico real ≤ −1 dBTP.
- Cadeia na voz: redução de ruído leve → EQ (corte abaixo de 80 Hz) → compressor 3:1 → limitador −1 dB.
- Microfone de lapela sem fio em todo vídeo falado. Áudio ruim derruba mais visualizações que imagem ruim.
- Música sempre com licença (biblioteca do app ou banco pago). Sem música com direitos autorais em vídeo que você vai impulsionar.

## 5. Capa e primeiro quadro

- Rosto em close + no máximo 5 palavras em caixa alta, sempre na mesma posição (terço superior).
- Capa de negócios: promessa concreta ("COMO CORTEI 30% DO CUSTO"). Palestras: selo `NO PALCO` + nome do evento. Família: só a foto, sem texto ou com 1–2 palavras.
- A capa precisa funcionar recortada em 1:1 no grid do perfil: texto dentro do quadrado central.

## 6. Fluxo de produção

1. **Roteiro** com o modelo do pilar em [`roteiros.md`](roteiros.md).
2. **Captação** (seção 3 e checklist).
3. **Edição** seguindo as regras do pilar.
4. **Medição automática**:
   ```bash
   ./sharingan analyze video-final.mp4 -o analise --title "Nome do post"
   python3 scripts/padrao.py analise/analysis.json --pilar negocios     # ou familia | palestras | palestra_inteira
   ```
   O comando sai com erro se alguma regra dura falhar. Corrija uma regra por vez.
5. **Checklist humano** em [`checklist.md`](checklist.md): o que a máquina não mede (gancho, legenda, privacidade).
6. **Publicar** e anotar retenção aos 3 s, retenção média e salvamentos por pilar. Depois de 8 semanas, revise as metas com base nos números.

### Limites da medição automática

- `sharingan` foi feito para motion design. Em vídeo falado, os números de **câmera** (px/s, easing) não importam; os úteis são **cortes, ASL, plano mais longo, áudio e cor**.
- **Punch-in** no mesmo take pode não ser detectado como corte (a detecção ignora mudanças contínuas de enquadramento). Se o ASL sair alto demais, confira `sheets/shots.png` e, se preciso, passe os cortes manualmente com `--cuts`.
- A classe de áudio distingue música e SFX; voz pura pode ser classificada de forma inesperada. Por isso essa regra é só "ATENÇÃO".
- RMS em dBFS não é LUFS. O alvo de −14 LUFS se confere no editor (Premiere, DaVinci ou CapCut) ou com `ffmpeg -af ebur128`.

## 7. Presets por editor

| | CapCut | Premiere / DaVinci |
|---|---|---|
| Projeto | 1080 × 1920, 30 fps | sequência 1080 × 1920, 29,97/30 fps |
| Legenda | legenda automática → estilo salvo "Padrão Negócios" e "Padrão Família" | Essential Graphics / Text+ salvos como modelo |
| Cortes de silêncio | "Remover pausas" com sensibilidade média, revisar à mão | Auto Cut / Silence Remover, depois revisão |
| Cor | filtro salvo "Pele neutra" e "Família quente" | LUT própria de correção (não criativa) + ajuste de pele |
| Áudio | "Reduzir ruído" + volume da voz até −14 LUFS (conferir) | Loudness Normalization −14 LUFS |

Salve esses estilos com o nome do pilar. O padrão só se sustenta se for **um clique**, não uma lembrança.
