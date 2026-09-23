# Persona

A Claude Code skill for synthetic personas — anywhere, for work or play. Generate a cast, interview them in character (scales + open answers), and get a Markdown report with scores, themes, and takeaways.

Works worldwide. Use it for product research (pricing, messaging, features) or for fun (game NPCs, fiction, dinner parties, debate panels, roast sessions). No default country.

## What Are Synthetic Personas?

Synthetic personas are fictional characters created by AI to stand in for real customer segments — or for any cast you invent. Instead of recruiting 10 people for interviews (weeks, thousands of dollars), this skill builds 10 distinct profiles — jobs, budgets, fears, decision patterns — and interviews them on your behalf.

Think of it like a flight simulator. A simulator doesn’t replace real flying, but it lets pilots test scenarios safely and quickly. Synthetic personas do the same for product decisions — and they’re also a fast way to pressure-test stories, games, and “what if” social scenarios.

### How Reliable Are the Results?

Useful, but not a replacement for real people when money or reputation is on the line:

| Trust | Validate |
|-------|----------|
| Directional signals (e.g. a price-sensitive segment exists) | Exact numbers (e.g. “73% prefer $49/mo”) |
| Pattern detection across the cast | Individual persona opinions |
| Feature prioritisation and ranking | Final pricing or positioning decisions |
| Hypothesis generation | Hypothesis confirmation |

**Bottom line:** Narrow options and sharpen questions — then validate the final call with 5–10 real humans (for research). For play, have fun; just don’t dress fiction up as market data.

## Two flavours

| Flavour | Good for | Tone |
|---------|----------|------|
| **Research** | pricing pages, messaging, roadmaps, content | Decision-ready, validation-minded |
| **Play** | game NPCs, fiction, parties, debates, roasts | Same structure, more voice and comedy |

## Use Cases

### Research

1. **Co-founder alignment** — two segments, one scorecard, less loudest-voice-in-the-room.
2. **Pricing before code** — test tier structures and price anchors before building the page.
3. **Competitive positioning** — map rivals as personas; find switching triggers and objections.
4. **Content strategy** — what each role would click, share, and save.
5. **Roadmap “user evidence”** — score proposed features across the cast (still validate before the board deck ships).

### Play

6. **Game NPCs** — will these shopkeepers trust the suspicious hero?
7. **Dinner party** — historical figures (or friends) on a topic: who derails the table?
8. **Debate panel** — force disagreement; find the golden compromise or the fight.
9. **Roast / critique** — five very different haters on your landing page or dating profile.
10. **Ensemble cast** — up to 30 characters for story consistency checks.

## Value

| Without Persona | With Persona |
|-----------------|-------------|
| Weeks of recruiting (research) | Instant synthetic cast |
| Expensive panels and tools | Runs in Claude Code |
| “I think users want…” | Scored, ranked, quote-backed output |
| No structured write-up | Report template + honesty footnote |

## Impact

- **Speed:** minutes, not 2–4 weeks of recruitment
- **Cost:** $0 beyond your Claude usage
- **Decision quality:** scores + themes cut assumption-driven mistakes (research)
- **Fun:** playable casts for games, stories, and social experiments

## Installation

Requires [Claude Code](https://claude.ai/claude-code) with skills support.

Install **`SKILL.md`** (and optionally `scripts/`). Do **not** copy `README.md` or `LICENSE` into the skills folder.

### Option A — one-liner (no clone)

```bash
mkdir -p ~/.claude/skills/persona/scripts
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/SKILL.md \
  -o ~/.claude/skills/persona/SKILL.md
# optional report checker
curl -fsSL https://raw.githubusercontent.com/47096/persona/main/scripts/check_report.py \
  -o ~/.claude/skills/persona/scripts/check_report.py
```

### Option B — from a local copy of this repo

```bash
mkdir -p ~/.claude/skills/persona
cp SKILL.md ~/.claude/skills/persona/
cp -R scripts ~/.claude/skills/persona/
```

### Option C — clone somewhere else, then copy

```bash
git clone https://github.com/47096/persona.git ~/src/persona
mkdir -p ~/.claude/skills/persona
cp ~/src/persona/SKILL.md ~/.claude/skills/persona/
cp -R ~/src/persona/scripts ~/.claude/skills/persona/
```

### Do not clone into the skills folder

```bash
# Wrong — pulls README.md and LICENSE into the skill package
git clone https://github.com/47096/persona.git ~/.claude/skills/persona
```

If you already did that:

```bash
rm -f ~/.claude/skills/persona/README.md ~/.claude/skills/persona/LICENSE
```

After install, the folder should hold `SKILL.md` and optionally `scripts/check_report.py`, nothing else from GitHub.

## Usage

In Claude Code:

```
/persona
```

Or just ask:

**Research**

- “Create 5 personas for a B2B accounting app targeting small business owners in Berlin”
- “Generate personas and interview them on pricing sensitivity for $29/$99/$199”
- “Run persona research on a meal-kit service in São Paulo”

**Play**

- “6 fantasy shopkeeper NPCs — would they sell to a suspicious hero?”
- “Dinner party: 5 historical figures on AI. Who derails the table?”
- “Roast my landing page as five very different people”

## How It Works

1. **Generate** — N distinct personas (research default 5–10; play ensembles up to 30)
2. **Interview** — each answers in character (0–10 scales + open)
3. **Report** — scoreboard, themes with quotes, takeaways, golden combos
4. **Summary** — cast overview, key findings, top takeaways

Optional: `check_report.py` validates report structure and honesty markers.

## Sample Output

<details>
<summary>Click to expand — research sample (B2B SaaS pricing, 10 personas)</summary>

### Executive Summary

- Starter tier is attractive; Pro upgrade is conditional on clear limits
- Feature-gate anxiety is the main friction for non-technical buyers
- Solo founders and agency owners want different anchors

### Scoreboard

| Question | Avg (0-10) | Median | Top / bottom split |
|----------|------------|--------|--------------------|
| How appealing is the $49/mo Starter tier? | 7.2 | 7 | Solo founders (8.3) vs ops managers (5.8) |
| Would you upgrade to the $149/mo Pro tier? | 6.1 | 6 | Agency owners (8.0) vs freelancers (4.2) |
| How clear is the pricing page layout? | 5.4 | 5 | Technical buyers (7.1) vs non-technical (3.9) |

### Themes

- **Price anchoring over tier count** — 7/10 compared plans to a reference price, not in isolation. → *“I picked the one that didn’t feel like a rip-off compared to the cheap one.” (P3, Agency owner)*
- **Feature gating creates anxiety** — non-technical buyers feared silent limits. → *“What happens when I hit 500 contacts — a warning, or does it just stop?” (P7, Marketing manager)*
- **Annual discount needs a monthly frame** — 20% off annual didn’t land without a monthly equivalent. → *“Show monthly first, then tell me I save going annual.” (P2, Freelancer)*

### Takeaways

1. **Ship 3 tiers, highlight the middle** — 8/10 preferred that over 4 tiers. Next step: mock this layout.
2. **Lead with $49/mo** — keep $149 as “everything you need”. Next step: rewrite the price page hero.
3. **Replace “Get started”** — “Start free trial — no card required” won the CTA battle in this cast. Next step: A/B with real traffic.

### Golden Combos

- **Golden tier structure** — 3 tiers, middle marked Most Popular (8/10)
- **Golden price ladder** — $49 lead → $149 core → $299 premium without absurdity
- **Golden CTA** — “Start free trial — no card required”

### Footnote

*Synthetic personas (N=10) for a B2B SaaS pricing brief, based on the provided context — not real respondents. Ideate and prioritise only; validate with real buyers before spending money or publishing claims. Follow local advertising and research rules for anything commercial.*

</details>

<details>
<summary>Click to expand — play sample (fantasy shopkeeper NPCs, 6 personas)</summary>

### Executive Summary

- Three will deal with a suspicious hero; three need cover stories or bribes
- Trust is currency; inventory risk beats profit for the paranoid
- The wildcard fence is the most interesting quest hook

### Scoreboard

| Question | Avg (0-10) | Median | Top / bottom split |
|----------|------------|--------|--------------------|
| Would you sell to this hero? | 5.2 | 5.5 | Fence (9) vs temple merchant (2) |
| How risky does the deal feel? | 7.1 | 7 | Everyone high — law still matters |

### Themes

- **Coin first, legend second** — most care about not getting robbed. → *“Heroes break things. Heroes don’t pay for broken things.” (P4, Armorer)*
- **One wildcard is enough chaos** — the fence will launder the plot. → *“If it glows, I don’t ask. If it glows *and* whispers, I charge extra.” (P6, Fence)*

### Takeaways

1. **Gate the magic shop behind a favour** — 4/6 won’t sell openly.
2. **Let the fence move the quest** — best hook for a second act.
3. **Keep the temple merchant hostile** — useful moral foil.

### Golden Combos

- **Golden opener** — buy something boring first, then ask about the glowing item
- **Golden bribe** — information over gold for 5/6

### Footnote

*Synthetic characters (N=6) for a fantasy game brief — fiction, not market evidence. Not real respondents. Safe for entertainment and design prototyping; don’t cite as player research without real playtests.*

</details>

## License

MIT
