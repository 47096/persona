# Who actually wants this?

**A product decision problem, solved before you build.**

Teams argue from vibes: loudest founder wins, the roadmap fills up, and three months later nobody can say why that feature shipped. I help product teams **pressure-test pricing, ICP, and prioritisation with a synthetic buyer panel** — scores, quotes, and a ranked call — *before* they spend the quarter.

---

## The stake

A wrong product bet is not a bad meeting. It is **weeks of engineering, a weak launch, and a quiet churn story**. Discovery is slow. Aligning co-founders is slower. The cost of *deciding badly* is the budget you never get back.

## The story

A team has three pricing options, two target segments, and one prioritisation meeting next week.

Instead of another opinion fight, they **hire a panel** (5–10 distinct buyers), interview them in character, and leave with:

- **Scores** — who wants what, and who doesn’t  
- **Quotes** — lines they can paste into the PRD or the board deck  
- **A ranked call** — including the option that won and who objected  

**Outcome on a typical run:**
- Same panel reusable for follow-ups (“what would make you switch?”)
- A decision the room can **defend** — not a consensus shrug
- A clear **next step: talk to 5–10 real people** with sharper questions

> **The commercial idea:** spend discovery *after* you know what to validate — not before.

---

## What that looks like in your world

| You are stuck on | I help you leave with |
|------------------|------------------------|
| Pricing page / packaging | Tier shape, lead price, who you’d lose |
| Feature prioritisation | Ranked bets + segment split |
| Co-founder ICP fight | One scoreboard instead of two opinions |
| Positioning & messaging | Which claim lands, which line bounces |
| Stakeholder pushback | Quote bank and “who disagrees” before the room |

**Typical engagement**
1. **Decision workshop** — one high-stakes call, facilitated with the panel method  
2. **Sprint support** — we run several bets in a week (pricing, page, roadmap)  
3. **Team enablement** — your PMs learn to run this in Claude Code themselves  

**[Talk to me about a decision →](https://datafying.co/#contactus)** · [datafying](https://datafying.co/)

---

## Why product leaders bring me in

- I sell **decision evidence**, not “AI demos”
- Panels are designed to **disagree** (uniform 9/10 cheerleading is a fail)
- Outputs are **hypothesis-grade** — we say so in the report, so you can use them in a room
- You can **keep the skill** and run it without me after enablement

---

## Proof of craft *(product + technical)*

### What you get every run
- **Decision memo** — ranked takeaways with counts (`6/10`) or themes  
- **Scoreboard** — avg / median / top–bottom split  
- **Quote bank** — verbatim, with persona ids  
- **Golden combo** — what won across the panel + who objected  
- **Honesty footnote** — synthetic disclaimer for real meetings  

### Samples (abridged)

**Pricing — meal kit at $49/week**  
*10 buyers.* Busy parents lean yes; students don’t — **avg 6.4**.  
> “I’d pay for three dinners, not seven.” — P2, PM  
**Decision:** Pilot a 3-night plan.

**Prioritisation — ship SSO in Q3?**  
**7.8/10** · IT lead 9 vs solo founder 5.  
> “I can’t sell to security without it.” — P5, IT lead  
**Decision:** Enterprise-first SSO; don’t block self-serve.

### How it works
Four phases: **GENERATE → INTERVIEW → REPORT → SUMMARY**.

1. You bring the decision brief, panel size `n`, and questions  
2. Personas differ on **budget power, time pressure, temperament, risk**  
3. Scales 0–10 + open answers in character (refusal and `unsure` count)  
4. Report: summary → scoreboard → themes + quotes → ranked takeaways → golden combos → footnote  

Optional `scripts/check_report.py` enforces report shape and blocks overclaims.

### Limits (honesty)
- **Hypothesis generation, not market research** — validate with real people before real money  
- Not for published market-size stats, legal proof, or replacing live interviews  
- Best used to **sharpen questions and rank options** — then talk to humans  

---

## Install (Claude Code skill)

```bash
mkdir -p ~/.claude/skills/persona/scripts
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/SKILL.md \
  -o ~/.claude/skills/persona/SKILL.md
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/scripts/check_report.py \
  -o ~/.claude/skills/persona/scripts/check_report.py
```

Requires [Claude Code](https://claude.ai/claude-code). Put only `SKILL.md` + `scripts/` in the skill folder — do **not** `git clone` this repo into `~/.claude/skills/persona`.

Then: `/persona`, or describe the decision you’re making.

```bash
rm -rf ~/.claude/skills/persona   # remove
```

---

## Use cases (commercial + workshop)

Pattern: **hire a panel → interview in character → scores, quotes, and a decision you can defend.**

1. **Pricing page before code** — tier structure and who you’d quietly lose  
2. **Co-founder ICP fight** — one scoreboard, less politics  
3. **Competitive win themes** — objections to answer first on calls  
4. **Message & content test** — what they’d click, skip, or mock  
5. **Roadmap cut** — three bets, not twelve  
6. **Landing page pressure test** — ten seconds, first objection, CTA  
7. **Hiring & job brand** — what scares candidates off  

*Also useful:* workshops, fictional casts, debate panels — same loop, lighter tone.

**Invent your own:** any decision where **ten named judges + a written summary** would beat a hallway opinion.

---

## Next step

If a pricing, ICP, or roadmap call is coming up and the room is already arguing — that is exactly the engagement I run.

**[Book a decision workshop →](https://datafying.co/#contactus)** · Product decisions with evidence · [datafying](https://datafying.co/)
