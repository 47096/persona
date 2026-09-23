# Persona

**Customer interviews in minutes, not weeks** — synthetic personas, interviewed in character, delivered as a scored Markdown report with quotes and takeaways.

For **indie founders & PMs** who need a call before real user research, and **writers & game makers** who want a cast that argues back. A Claude Code skill. Works worldwide.

Synthetic results are **hypotheses, not proof**. Use them to rank and spot patterns; validate money decisions with real people.

## Why this skill (not a freeform prompt)

- **Diverse cast** — forced different jobs, budgets, and temperaments (not five clones who all love you)
- **Honest scores** — mid scores, `unsure`, and refusals allowed; no cheerleading
- **Guardrails** — fixed report shape + `scripts/check_report.py` blocks overclaims like “statistically significant”

## Samples (abridged)

**1 — Pricing** (10 buyers, meal kit €49/week)

| Question | Avg | Split |
|----------|-----|-------|
| Subscribe at €49/week? | 6.4 | Busy PM (8) vs student (3) |

- **Takeaway** — Pilot a 3-night plan; 4/10 asked for partial boxes. → *“I’d pay for three dinners, not seven.”* (P2, PM)

**2 — Roadmap** (8 PMs, B2B SaaS features)

| Question | Avg | Split |
|----------|-----|-------|
| Ship SSO in Q3? | 7.8 | IT lead (9) vs solo founder (5) |

- **Takeaway** — SSO for the enterprise tier first. → *“I can’t sell to security without it.”* (P5, IT lead)

**3 — Play** (6 fantasy NPCs, sell to a suspicious hero?)

| Question | Avg | Split |
|----------|-----|-------|
| Sell to this hero? | 5.2 | Fence (9) vs temple merchant (2) |

- **Takeaway** — Gate the magic shop behind a favour. → *“Heroes break things. Heroes don’t pay.”* (P4, Armorer)

*Synthetic personas — not real respondents. Validate money decisions with real people.*

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

Requires [Claude Code](https://claude.ai/claude-code). Only `SKILL.md` + `scripts/` go in the skill folder — do **not** `git clone` this repo into `~/.claude/skills/persona`.

Then in Claude Code: `/persona`, or describe what you want (see use cases above).

## Remove

```bash
rm -rf ~/.claude/skills/persona
```

## How it works

1. **Generate** — N distinct personas (research 5–10; play ensembles up to 30)
2. **Interview** — each answers in character (0–10 scales + open)
3. **Report** — scoreboard, themes, takeaways, golden combos, honesty footnote
4. **Summary** — cast overview + top takeaways

## License

MIT
