# BUILD-LOG — news-image-20261119

Entry: **"The World Today" — a newspaper front page summing up Thursday,
19 November 2026.** Competition `news-image-20261119`, account @rfq404
(make.fun), GitHub rifki500 (verified linked). Built 20 November 2026
(WIB) in a session started after the competition opened
(19 Nov 2026 00:00 UTC). BUILD ONLY — parent submits.

## The image

1024×1024 PNG, drawn entirely in code (`build_image.py`, PIL — no
external photos, no network). Masthead names the day prominently
("THURSDAY, 19 NOVEMBER 2026"), seven stories with headlines,
one-to-two-line summaries and small drawn visuals (scales of justice,
three flags, warming globe, burning house, rising chart, EU star ring,
tanker). The entrypoint `main.py` (stdlib only) copies the pre-built
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).

## Stories used (all of Thursday 19 November 2026)

1. **World court: Myanmar committed genocide** — The International Court
   of Justice rules Myanmar's military acted with genocidal intent
   against the Rohingya in 2017 and orders restitution. Sources: ICJ
   ruling reported 19 Nov 2026 (Reuters; Foreign Exchanges world
   roundup; Russell Record daily headlines).
2. **Trump, Xi and Putin meet in first three-way summit** — The three
   leaders meet in Shenzhen and issue a joint "Declaration toward
   Peace"; no deal on Ukraine or Iran. Sources: Horizon daily briefing
   19 Nov 2026; Standard Topic world archive, Nov 19; Medium strategic
   brief, 19 Nov 2026.
3. **COP31 draft drops fossil fuels** — A new draft deal in Antalya
   removes every mention of moving away from coal, oil and gas, and
   admits the world will overshoot 1.5°C. Sources: UN News, 19 Nov
   2026 ("COP31: Ambition goes missing…"); Climate Home News via
   Carbon Energy Nexus, 19 Nov 2026.
4. **Bangladesh lockdown as violence spreads** — Hasina supporters try
   to shut the country down; Muhammad Yunus's ancestral home is torched
   and unrest hits 28 districts. Sources: Reuters, 19 Nov 2026
   ("Parts of Bangladesh shut down…"); Devdiscourse/Reuters, 19 Nov
   2026; AP, 19 Nov 2026.
5. **Anthropic's record IPO soars on debut** — The AI firm behind
   Claude lists on Nasdaq at $83, opens at $111.50 and raises $81bn —
   the largest IPO ever. Sources: Reuters, 19 Nov 2026; WSJ, 19 Nov
   2026; NPR, 19 Nov 2026.
6. **EU proposes €45bn loan for Ukraine** — The European Commission
   proposes a new loan to cover two-thirds of Kyiv's 2027 funding gap:
   €25bn military, €20bn civilian. Sources: Serrari Group daily
   brief, 19 Nov 2026; The Missing Link Hub brief, 19 Nov 2026;
   Horizon, 19 Nov 2026.
7. **Hormuz tanker attacks mount** — More ships are hit in the Strait
   of Hormuz as US–Iran strikes escalate; an ADNOC vessel is attacked,
   11 crew hurt, one missing. Sources: Standard Topic world archive,
   Nov 19, 2026; 10 Things Global News, 19 Nov 2026.

## Verification (run 20 Nov 2026, ~19:35 WIB)

- `main.py` run twice with `MAKEFUN_OUTPUT_DIR` set to two scratch
  dirs; both outputs byte-identical and matching the repo `entry.png`:
  sha256 `bda9e53c05c0f882fb7e416f28be4e9283f3a2c999b1482c992348494dc11f7a`
  (run 1, run 2, and repo file — all three identical).
- Dimensions: 1024×1024 px (limit 1024×1024). Format: PNG.
- File size: 152,337 bytes (limit 1,048,576 bytes).
- Visual inspection: all seven headlines and summaries legible at
  1024 px; date prominent in the masthead and restated in the footer;
  no garbled text, no text-on-text overlap. One cosmetic touch: the
  Shenzhen summary's final line sits close to the row divider, but
  remains fully legible.
- `main.py` imports only `os` and `sys` (stdlib); no network access in
  the entrypoint or the generator.

## Commit

- Repository: https://github.com/rifki500/news-image-20261119-entry
- Commit sha: (filled in after push)

## Honest caveats

- The fire at Yunus's ancestral home was set late on Wednesday night
  (18 Nov); the story on the page is the Thursday lockdown and the
  day's spreading violence, which the 19 Nov reporting covers. The
  image does not date the fire itself.
- Anthropic's $83 pricing was announced late Wednesday (US time); the
  Nasdaq debut — opening at $111.50, the record $81bn raise — happened
  Thursday 19 Nov, which is what the story reports.
- The Shenzhen summit's joint declaration is described as pledging
  further talks; the page says plainly there was no deal on Ukraine
  or Iran, per the 19 Nov reporting.
