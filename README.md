# Persona — decision evidence before you build

Interview 5–10 synthetic buyers in Claude Code. Leave with **scores, quotes, and a ranked call** — before you book discovery or run the prioritisation meeting.

For **product managers and product owners** who are comfortable in Claude Code and need faster decision evidence than a gut-feel debate. Hypothesis generation, not market research.

## When to use it

| Job | You leave with |
|-----|----------------|
| **Pricing & packaging** | Tier structure, lead price, which segment you’d lose |
| **Feature prioritisation** | Ranked bets + who wants what (and who doesn’t) |
| **Segment / ICP fight** | A scoreboard so co-founders stop arguing from vibes |
| **Positioning & messaging** | Which claim lands, which line bounces |
| **Landing page / CTA** | What they think you sell in ten seconds, first objection, CTA that earns a click |
| **Stakeholder prep** | Quote bank and “who disagrees” before the room |

*Also works for workshops and fictional casts (game NPCs, debate panels, roast sessions).*

## What you get

- **Decision memo** — ranked takeaways, each backed by counts (`6/10`) or a theme  
- **Scoreboard** — avg / median / top-bottom split per question  
- **Quote bank** — verbatim lines with persona ids (paste into the PRD or the deck)  
- **Golden combo** — the option that won across the panel, plus who objected  
- **Honesty footnote** — synthetic disclaimer so you can use this in a room without overclaiming  

Same panel stays on the bench for follow-ups (“what jobs do they hire this for?”) unless you re-roll.

## Samples (abridged)

*“Split” = who scored high vs low. “Golden combo” = what won across the panel.*

**1 — Pricing** (10 buyers, meal kit $49/week)

| Question | Avg | Split |
|----------|-----|-------|
| Subscribe at $49/week? | 6.4 | Busy PM (8) vs student (3) |

- **Decision** — Pilot a 3-night plan; 4/10 asked for partial boxes. → *“I’d pay for three dinners, not seven.”* (P2, PM)

**2 — Prioritisation** (8 buyers, B2B SaaS)

| Question | Avg | Split |
|----------|-----|-------|
| Ship SSO in Q3? | 7.8 | IT lead (9) vs solo founder (5) |

- **Decision** — SSO in the enterprise tier first. → *“I can’t sell to security without it.”* (P5, IT lead)

## Install

```bash
mkdir -p ~/.claude/skills/persona/scripts
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/SKILL.md \
  -o ~/.claude/skills/persona/SKILL.md
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/scripts/check_report.py \
  -o ~/.claude/skills/persona/scripts/check_report.py
```

Requires [Claude Code](https://claude.ai/claude-code). Only `SKILL.md` + `scripts/` go in the skill folder — do **not** `git clone` this repo into `~/.claude/skills/persona`.

Then in Claude Code: `/persona`, or describe the decision you’re making (see use cases below).

## Remove

```bash
rm -rf ~/.claude/skills/persona
```

## Use cases for PMs

Pattern: **hire a panel → interview in character → scores, quotes, and a decision you can defend.**

1. **Pricing page before code** — You’re tempted to ship four tiers and an annual toggle. Score layouts and anchors on buyers with different budget power and risk. Leave with tier structure, lead price, and who you’d quietly lose — *before* three weeks of frontend. *Spin-off: trial length, packaging, self-serve vs “contact sales.”*

2. **Co-founder ICP fight** — Two markets, two founders, one first bet. Eight personas split across both, same value props, one scoreboard. Kills the loudest-voice debate. *Spin-off: investor narrative stress-test.*

3. **Competitive win themes** — Map rivals as buyers with budget and pride. Interview your ICP on switching triggers and deal-breakers. Know which objection to answer first on calls. *Spin-off: win/loss themes before you have lost deals.*

4. **Message & content test** — Ask each role what they’d click, skip, or mock. Leave with a line per persona and the phrases that bounce. *Spin-off: launch email, conference abstract, onboarding copy.*

5. **Roadmap cut, not theatre** — Score the Q3 list across segments with quotes. Use it to cut to three bets — then validate those with real users before the board deck. *Spin-off: RFC pushback, procurement/security review cosplay.*

6. **Landing page pressure test** — Five visitors, ten seconds: what do they think you sell, first objection, which CTA converts. *Spin-off: paywall wording, support macro tone, empty-state copy.*

7. **Hiring & job brand** — Interview candidates on what scares them off and what sounds like growth, before you post the JD. *Spin-off: offer narrative, internal mobility.*

**Also useful (workshops & fiction)** — game NPCs who can refuse, dinner-party seating, roast panels, debate setups, story cast continuity. Same loop; lighter tone.

**Invent your own:** any decision where **ten named judges + a written summary** would beat a hallway opinion.

## How it works

Four phases: **GENERATE → INTERVIEW → REPORT → SUMMARY**.

### 1. Generate

You bring panel size `n`, questions, and the decision brief. The skill asks for anything missing.

Personas differ on **budget power, time pressure, temperament, and risk**. Research default: 5–10 with price-sensitive, time-poor, and risk-averse profiles. Play/workshop panels can run larger with a wildcard.

### 2. Interview

| Type | Answer |
|------|--------|
| **Scale** | 0–10 + 1–2 sentences tied to their goals/fears |
| **Open** | 1–3 sentences in their voice |

They can be wrong, biased, or hostile. Mid scores, `unsure`, and refusal count. Uniform 8–10 cheerleading is a bug.

### 3. Report

Executive summary → scoreboard → themes (with quotes) → ranked takeaways → golden combos → footnote.

Optional: `scripts/check_report.py` checks that skeleton and blocks overclaims (“statistically significant” and friends).

### 4. Summary + follow-ups

Cast overview, key findings, top takeaways, golden combos. Follow-ups stay on the same panel unless you ask for a re-roll.

## Why this skill (not a freeform prompt)

- **Diverse panel** — not five clones who all love the idea  
- **Honest scores** — disagreement is data  
- **Guardrails** — fixed report shape + overclaim checks you can take into a room  

## In a PM week

Mon: drop the brief and questions into Claude Code → same day: scoreboard + quotes → Thu prioritisation: show who scored what and who objected → **then** talk to 5–10 real users for the final call.

## Not for

Published market-size stats, legal proof, or replacing live customer interviews. Use it to sharpen questions and rank options — then talk to humans.

## Feedback

Ideas and issues → [GitHub Issues](https://github.com/47096/persona/issues).

## License

MIT
