---
name: persona
description: Generates N distinct synthetic personas, interviews them in character (scales + open answers), and writes a Markdown report with scores, themes, and takeaways. Works worldwide for product research (pricing, messaging, features) and for playful use (game NPCs, fiction, dinner parties, debate panels, roast sessions). Use when the user says "create personas", "generate personas", "persona research", "synthetic personas", "interview personas", "simulate users", "ask my customers", "roleplay stakeholders", or wants a cast of characters interviewed on a topic. Do NOT use for recruiting real participants, published market-size stats, legal proof, or live customer interviews.
---

# Persona

Spin up a cast of distinct people (or characters), interview them in character, and turn answers into a clear report.

Loop: **GENERATE → INTERVIEW → REPORT → SUMMARY**.

This skill is for **any market or culture**. Take locale, language, and context from the user. Never assume Australia, the US, or any default country.

Two flavours of the same loop:

| Flavour | Typical asks | Report tone |
|---------|----------------|-------------|
| **Research** | pricing, messaging, features, content, positioning | Crisp, decision-ready, validation-minded |
| **Play** | game NPCs, fiction, parties, debate panels, roasts, “what if” casts | Same structure, lighter, more voice and comedy when invited |

Both are valid. Keep the persona math honest in both.

## Important

- Missing inputs → ask. Do not invent a silent default product, country, or cast.
- Personas must actually differ (role, stakes, budget/power, temperament). Cosmetic clones are a fail.
- Allow mid scores, `unsure`, and dislike. Uniform 9/10 cheerleading is a fail.
- Prefer counts (`6/10`) over fake precision (`62.7% confident`).
- Research flavour: synthetic results are **hypotheses**. Always say validate with real people before real money.
- Play flavour: still mark outputs as fictional. Do not dress comedy as market data.
- Match the user’s language and spelling (e.g. en-US, en-GB, en-AU, or the language they write in).

## Instructions

### Step 1 — Gather inputs

| Input | Rule |
|-------|------|
| `n` | How many personas. Research default 5–10. Play default 5–12 (ensembles up to 30). Hard cap 30. Reject 0 or >30. If `n` is large, cap questions at 3–5 so answers stay distinct. |
| `questions` | Each question is scale (0–10) or open |
| `context` | What we’re testing or playing with (product, scene, game, topic) |
| `cast` | Optional constraints: age, role, budget, culture, vibe, era, species… |
| `flavour` | `research` or `play`. Infer from the ask; confirm if mixed. |
| `locale` | Country/culture/market **only if** the brief needs it. Infer; ask if it would change the cast. |

If something’s missing, ask (Claude Code: `AskUserQuestion`; otherwise a short numbered prompt). If they give fewer than 3 questions, suggest 3–5 more; let them accept, edit, or skip.

**Smart defaults for fun:** If the ask is playful, propose one extra “chaos” question (e.g. “What’s the worst thing that could happen on the night?”). For research, propose one trade-off question.

### Step 2 — GENERATE

Create `n` personas. Each gets:

- id (`P1`…)
- name + one-line hook
- role / life context (or species, era, class — for fiction)
- resources (money, time, power, skill)
- goals, fears, constraints
- decision style + deal-breakers
- voice note (how they talk — one line)

Requirements:

- Vary power, budget, time pressure, and temperament — not just names and ages.
- When the brief names a culture/country, ground details there. When it doesn’t, stay neutral or ask.
- Research with `n >= 5`: include at least one price-sensitive, one time-poor, one risk-averse profile.
- Play: include at least one wildcard (chaotic, petty, absurdly literal, or hostile).
- Never clone the same persona with cosmetic edits.

### Step 3 — INTERVIEW

For every persona × question:

- **scale** → integer 0–10 + 1–2 sentences tied to their goals/fears
- **open** → 1–3 sentences in their voice

Rules:

- Stay consistent to that persona across the full run.
- Let them be wrong, biased, or bored. They are not user testers for hire.
- No salesy agreement. Dislike and refusal are useful data (or good comedy).
- Research: allow `unsure` when the profile wouldn’t know.
- Play: allow jokes, drama, and conflict — still in character.

### Step 4 — REPORT

Emit one Markdown report in chat (write a file only if they asked to save).

When `scripts/check_report.py` is installed next to this skill, run it on the report before finishing (or on `persona-report.md` if saved) and fix any ERROR-level gaps.

```markdown
## Executive Summary
- Headline takeaway
- Main friction or punchline
- Standout persona

## Scoreboard
| Question | Avg (0-10) | Median | Top / bottom split |
|----------|------------|--------|--------------------|
| ... | ... | ... | High group vs low group |

## Themes
- **Theme** — synthesis -> *"quote" (P##, hook)*
- Aim for 3 themes when the data supports it

## Takeaways
1. **Action / lesson** — backed by [count/10 at threshold] or [theme]. Next step: [...]

## Golden Combos
- **Golden [X]**: best option/wording/structure across the cast, plus who disagreed

## Footnote
*Synthetic personas (N=…) for [context/locale if any], based on the brief — not real respondents.
Research: ideate and prioritise only; validate with real users before spending money or publishing claims.
Play: fictional characters for entertainment/prototyping; not market evidence. Follow local ad/research rules if you publish anything commercial.*
```

### Step 5 — SUMMARY

After the report:

- **Who they are** — 2–3 sentences on the cast
- **Key findings** — numbered, one each
- **Top 3 takeaways** — ranked
- **Golden combos** — one per major question

### Step 6 — Follow-ups

Stay on the same cast unless asked to rebuild.

1. Answer from existing personas
2. Show counts (`7/10 prefer X`) when it’s a pattern
3. Give a short golden combo
4. Offer a saved summary when the session feels done

## Examples

**Research (global SaaS)**  
“8 personas in Germany and Brazil for a €29/€99 pricing page — will they upgrade?”  
→ Flavour research. Locale DE + BR (not AU). Interview on price, clarity, upgrade trigger. Report with counts + validate-with-real-buyers footnote.

**Play (game NPCs)**  
“6 shopkeeper NPCs for my fantasy city — interview them on whether they’d sell to a suspicious hero.”  
→ Flavour play. Wildcard shopkeeper required. Scales can be trust/risk; keep the scoreboard. Lighter footnote (fictional).

**Play (social)**  
“Dinner party: 5 historical figures on AI. Who derails the table?”  
→ Flavour play. Voice-heavy open answers. Golden combo = how to seat them.

**Follow-up**  
“What jobs do they hire this for?” after a research run  
→ Stay on cast. Counts + golden job-to-be-done. No new personas.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Everyone sounds the same | Re-generate with explicit power/budget/temperament clashes; require a wildcard |
| All scores 8–10 | Force trade-offs; invite dislike, boredom, `unsure` |
| Feels stuck in one country | Drop hardcoded market; ask locale only when the cast needs it |
| User wants “statistically significant” | Refuse for synthetic n. Point at Footnote + real-user validation |
| Jokes getting in the way of a business call | Default to research tone unless they asked for play |
| Too stiff for a party/game prompt | Turn up voice, conflict, and one chaos question |
| They want a file | Write `persona-report.md` in the working directory |
| `check_report.py` flags missing sections | Fill Executive Summary / Scoreboard / Themes / Takeaways / Golden Combos / Footnote and re-check |
