# Persona

A Claude Code skill that generates synthetic user personas, interviews them with structured questions, and produces a data-driven Markdown report with actionable recommendations.

Built for Australian market research contexts — ABS demographics, ACCC-compliant language, ESOMAR-inspired methodology.

## Use Cases

### 1. Co-Founder Alignment Sessions

Two co-founders disagree on which customer segment to target first. Generate 8 personas across both segments, interview them on the same value propositions, and let the data decide — not the loudest voice in the room.

**Impact:** Turns subjective founder debates into objective scorecards. Prevents the #1 startup killer: building for the wrong audience because co-founders couldn't agree.

### 2. Pricing Page A/B Testing (Before Code)

You're about to spend three weeks building a pricing page with four tiers. Before that, generate personas matching your buyer profiles, present each tier configuration, and find the "golden price anchor" — the tier structure that maximises perceived value across segments.

**Impact:** Saves 3 weeks of dev time if the data says your 4-tier model confuses people. You launch with the right structure from day one.

### 3. Competitive Positioning War Games

Map your top 3 competitors as personas with their real traits (budget, priorities, objections). Then generate your ideal customer personas and interview them on switching triggers, deal-breakers, and the "golden argument" that wins them over.

**Impact:** You walk into sales calls knowing exactly which objection to address first and which competitor weakness to exploit — without waiting for real lost deals to teach you.

### 4. Content Strategy Persona Mapping

You're planning a 6-month content calendar but writing for everyone means writing for no one. Generate personas by role, seniority, and content preference. Interview them on what they'd actually click, share, and save.

**Impact:** Each blog post, email, and LinkedIn thread targets a specific persona's trigger. Content becomes a conversion tool instead of a vanity metric generator.

### 5. Product Roadmap Stakeholder Simulation

Your board wants "user evidence" before approving Q3 features. Generate 10 personas representing your core segments, run them through your proposed features, and produce a report showing which features score highest and why.

**Impact:** Turns "we think users want X" into "8/10 personas scored Feature A at 8.5/10 with these specific reasons." Boards approve faster when they see numbers, not hunches.

## Value

| Without Persona | With Persona |
|-----------------|-------------|
| Weeks of recruiting for interviews | Instant synthetic respondents |
| Expensive research tools (Qualtrics, Maze) | Zero cost, runs in Claude Code |
| Subjective "I think users want..." | Scored, ranked, quote-backed insights |
| No methodology documentation | ESOMAR-inspired, ACCC-aware reports |

## Impact

- **Speed:** 15-minute research cycle vs. 2-4 week traditional recruitment
- **Cost:** $0 vs. $2k-10k for research panels or tools
- **Decision quality:** Quantitative scores + qualitative themes reduce assumption-driven mistakes
- **Repeatability:** Run the same questions across different contexts to compare segments

## Installation

Copy `SKILL.md` to your Claude Code skills directory:

```bash
cp SKILL.md ~/.claude/skills/persona/SKILL.md
```

Or clone this repo and link it:

```bash
git clone https://github.com/wsamuelw/persona.git ~/.claude/skills/persona
```

## Usage

In Claude Code, invoke with:

```
/persona
```

Or describe what you need:

- "Create 5 personas for a B2B accounting app targeting small business owners in Sydney"
- "Generate personas and interview them on pricing sensitivity"
- "Run persona research on a meal kit delivery service in Melbourne"

## How It Works

1. **Generate** — Creates N distinct personas grounded in realistic demographics
2. **Interview** — Answers your questions in character (scale 0-10 + open-ended)
3. **Report** — Aggregates into a structured Markdown report with tables and themes
4. **Summary** — Delivers top 3 recommendations and "golden combos" per question

## Sample Output

<details>
<summary>Click to expand — Sample report excerpt (B2B SaaS pricing research, 10 personas)</summary>

### Quantitative Insights

| Question | Avg (0-10) | Median | Top/Bottom Split |
|----------|------------|--------|------------------|
| How appealing is the $49/mo Starter tier? | 7.2 | 7 | Solo founders (8.3) vs. Ops managers (5.8) |
| Would you upgrade to the $149/mo Pro tier? | 6.1 | 6 | Agency owners (8.0) vs. Freelancers (4.2) |
| How clear is the pricing page layout? | 5.4 | 5 | Technical buyers (7.1) vs. Non-technical (3.9) |

### Qualitative Themes

- **Price anchoring matters more than tier count**: 7/10 personas compared pricing relative to a "reference point" rather than evaluating each tier independently. → *"I didn't pick the best plan — I picked the one that didn't feel like a rip-off compared to the cheap one." (P3, Agency Owner)*
- **Feature gating creates anxiety**: Non-technical buyers feared hitting limits mid-project. → *"What happens when I hit 500 contacts? Do I get a warning or does the system just stop?" (P7, Marketing Manager)*
- **Annual discount needs context**: The 20% annual discount didn't resonate without a monthly equivalent. → *"Show me the monthly price first, then tell me I save by going annual. Don't hide the monthly behind a toggle." (P2, Freelancer)*

### Golden Combos

- **Golden tier structure**: 3 tiers with the middle tier highlighted as "Most Popular" — 8/10 personas preferred this over a 4-tier layout
- **Golden price anchor**: Lead with $49/mo, position $149/mo as "everything you need", make $299/mo feel premium without being absurd
- **Golden CTA**: "Start free trial — no card required" scored 9.1/10 vs. "Get started" at 5.3/10

### Methodology Note

*Findings based on 10 synthetic personas generated per ABS demographic distributions and provided context. Synthetic data supports ideation and prioritisation; validate with 5-10 real prospects before commercial rollout. Inspired by ESOMAR research principles. Outputs are synthetic — do not use in advertising claims. Refer to Australian Privacy Principles (APPs) for data handling.*

</details>

## License

MIT
