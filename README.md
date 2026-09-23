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

The pattern is always the same: **hire a cast → interview in character → leave with scores, quotes, and a golden combo.** Swap the cast and the questions. If it helps to hear ten different people react to a decision, this skill fits.

**Commercial / business**

1. **Pricing page before code** — You’re tempted to ship four tiers and a toggle for annual. Build buyers who differ on budget authority and risk, then score each layout and price anchor. Walk away with a tier structure, a lead price, and which segment you’d be quietly losing — *before* three weeks of frontend work. *Spin-off: test packaging, trial length, or “contact us” vs self-serve.*

2. **Co-founder segment fight** — Two founders want two different first markets. Generate eight personas split across both segments, ask the same value props, and let the scoreboard end the debate. No loudest-voice-in-the-room. *Spin-off: investor narrative stress-test, or “who do we fire as ICP?”*

3. **Competitive war-gaming** — Turn each rival into a persona with their budget, priorities, and pride. Interview your ideal customers on switching triggers, deal-breakers, and the argument that actually moves them. You’ll know which objection to answer first on sales calls. *Spin-off: win/loss themes before you have real lost deals.*

4. **Content that converts** — “Write for everyone” is writing for no one. Cast roles and seniorities, then ask what they’d click, skip, share, or mock. Get a calendar angle per persona and the phrases that make them bounce. *Spin-off: newsletter subject lines, conference talk abstracts, onboarding emails.*

5. **Roadmap stakeholder theatre** — The board wants “user evidence.” Score the Q3 list across segments and show who wants what, with quotes. Better: use it to *cut* the list to three bets, then validate those with 5–10 real users. *Spin-off: RFC pushback simulation, procurement/security review cosplay.*

6. **Landing page & CTA pressure test** — Five visitors, ten seconds each: what do they think you sell, what’s the first objection, which CTA earns a click? Cheap way to kill a clever-but-cryptic hero before launch. *Spin-off: onboarding friction, paywall wording, support macro tone.*

7. **Hiring & job-branding** — Write a JD, then interview candidates who differ on stage of life and risk appetite. What scares them off, what actually sounds like growth? Useful before you post to three boards and wait. *Spin-off: offer negotiation scripts, internal mobility messaging.*

**Personal / fun**

8. **Game NPCs who can say no** — Shopkeepers, guards, fences with real incentives — not quest kiosks. Interview them on whether they’d help, rob, or report the hero. You’ll leave with loot tables of *attitude*: who needs a bribe, a favour, or a threat. *Spin-off: faction politics, boss monologue test, “would the village notice the missing relic?”*

9. **Dinner party seating chart** — Five historical figures (or your actual friends) on AI, money, or whether a hot dog is a sandwich. Same questions, different worldviews. Golden combo = where to sit them so the night is interesting instead of a brawl. *Spin-off: family holiday negotiation, podcast guest mix, classroom debate set.*

10. **Roast panel** — Five very different haters on your landing page, portfolio, or dating profile: the cynic, the busy parent, the design snob, the price-sensitive student, the “I don’t get it.” Leave with the line that dies first and the one that actually lands. *Spin-off: wedding speech, stand-up set, apology letter that isn’t cringe.*

11. **Debate panel / decision under disagreement** — Need a fight, not consensus? Cast true believers on opposite sides and run the same proposal. Find the golden compromise — or the exact wedge that splits the room — before you run the real meeting. *Spin-off: policy options, “relocate or stay,” which friend to trust with the secret.*

12. **Story & character continuity** — Keep a cast of 10–30 and ask follow-ups across scenes: who would lie here, who would crack, who would escalate? Cheap beta readers for motivation and consistency before you write the draft. *Spin-off: RPG campaign arcs, marketing mascot voice, alternate endings.*

**Invent your own:** any decision where you’d like **ten consistent judges with names** — and a written summary — is in scope. If it’s a real-money or real-reputation call, use this to sharpen questions, then talk to humans.

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

Four phases: **GENERATE → INTERVIEW → REPORT → SUMMARY**. One loop for research and play; tone and footnotes change, score honesty does not.

### 1. Generate

You bring `n`, questions, and a brief (product, scene, or cast rules). The skill asks for anything missing — it won’t silently invent a market.

Each persona gets an id (`P1`…), name and hook, role or life context, resources (money, time, power), goals and fears, constraints, decision style, deal-breakers, and a one-line voice note.

Rules that keep the cast useful:

- **Real differences** — budget power, time pressure, temperament, risk; not just age and job title
- **Research** (`n` 5–10): at least one price-sensitive, one time-poor, one risk-averse profile
- **Play** (5–12, ensembles up to 30): at least one wildcard (chaotic, petty, literal, or hostile)
- Locale only if the brief needs it — no default country

### 2. Interview

Every persona answers every question **in character**:

| Question type | Answer |
|---------------|--------|
| **Scale** | Integer 0–10 + 1–2 sentences tied to their goals/fears |
| **Open** | 1–3 sentences in their voice |

They stay consistent across the run. They’re allowed to be wrong, biased, bored, or hostile. Mid scores, `unsure`, and refusal are real answers — not failures. Uniform 8–10 cheerleading is treated as a bug.

### 3. Report

One Markdown report in chat (saved to a file if you want):

1. **Executive summary** — headline, main friction (or punchline), standout persona  
2. **Scoreboard** — avg, median, top/bottom split per question  
3. **Themes** — patterns with verbatim quotes and persona ids  
4. **Takeaways** — ranked actions/lessons, each backed by counts (`6/10`) or a theme  
5. **Golden combos** — the option/wording/structure that wins across the cast, plus who disagreed  
6. **Footnote** — synthetic-data disclaimer; validate with real people before money or PR  

Optional: `scripts/check_report.py` asserts that skeleton and blocks overclaims (“statistically significant” and friends).

### 4. Summary

After the report: who the cast is in a few sentences, numbered key findings, top takeaways ranked by impact, and a golden combo per major question.

### Follow-ups

Same cast stays on the bench. Ask more (“what jobs do they hire this for?”, “where do we meet them?”) and you get counts + a short golden combo — no re-rolling the world unless you ask.

## License

MIT
