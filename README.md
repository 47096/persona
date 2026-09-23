# Persona

Claude Code skill: generate a cast of synthetic personas, interview them in character, get a scored Markdown report.

**Research** (pricing, messaging, roadmaps) or **play** (game NPCs, fiction, dinner parties, roasts). Works worldwide — no default country.

Synthetic results are **hypotheses, not proof**. Great for ranking and spotting patterns; validate money decisions with real people.

## Use cases

**Commercial / business**

1. **Pricing tiers** — test anchors and “most popular” structure before you build the page
2. **Co-founder alignment** — score two target segments; stop debating from gut feel
3. **Competitive positioning** — map rivals as personas; find switching triggers and objections
4. **Content strategy** — what each role would click, share, or ignore
5. **Roadmap ranking** — which features score highest across your buyer types (validate before the board deck)

**Personal / fun**

6. **Game NPCs** — will these shopkeepers trust a suspicious hero?
7. **Dinner party** — historical figures (or friends) on a topic: who derails the table?
8. **Roast / critique** — five very different haters on your landing page or dating profile
9. **Debate panel** — force disagreement; find the compromise or the fight
10. **Story ensemble** — check whether a cast stays consistent across scenes

## Install

```bash
mkdir -p ~/.claude/skills/persona/scripts
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/SKILL.md \
  -o ~/.claude/skills/persona/SKILL.md
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/scripts/check_report.py \
  -o ~/.claude/skills/persona/scripts/check_report.py
```

Only `SKILL.md` + `scripts/` go in the skill folder. Do **not** `git clone` this repo into `~/.claude/skills/persona` (that pulls in `README.md` / `LICENSE` and breaks the package).

## Remove

```bash
rm -rf ~/.claude/skills/persona
```

## Usage

In Claude Code: `/persona`, or just ask.

- “Create 5 personas for a B2B accounting app targeting small business owners in Berlin”
- “Generate personas and interview them on pricing sensitivity for $29/$99/$199”
- “6 fantasy shopkeeper NPCs — would they sell to a suspicious hero?”
- “Dinner party: 5 historical figures on AI. Who derails the table?”

## How it works

1. **Generate** — N distinct personas (research 5–10; play ensembles up to 30)
2. **Interview** — each answers in character (0–10 scales + open)
3. **Report** — scoreboard, themes, takeaways, golden combos, honesty footnote
4. **Summary** — cast overview + top takeaways

`scripts/check_report.py` can validate report shape and block overclaims.

## License

MIT
