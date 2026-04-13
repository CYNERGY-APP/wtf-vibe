<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/dizzy-face_1f635.png" width="120" />
</p>

<h1 align="center">wtf-vibe</h1>

<p align="center"><strong>linters check syntax. tests check behavior. this checks the vibe.</strong></p>

<p align="center">
  <a href="https://github.com/CYNERGY-APP/wtf-vibe/stargazers"><img src="https://img.shields.io/github/stars/CYNERGY-APP/wtf-vibe?style=flat&color=ff69b4" /></a>
  <a href="https://github.com/CYNERGY-APP/wtf-vibe/commits"><img src="https://img.shields.io/github/last-commit/CYNERGY-APP/wtf-vibe?style=flat" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/CYNERGY-APP/wtf-vibe?style=flat" /></a>
</p>

<p align="center">
  <a href="#before--after">Before/After</a> •
  <a href="#install">Install</a> •
  <a href="#dimensions">Dimensions</a> •
  <a href="#examples">Examples</a> •
  <a href="#usage">Usage</a> •
  <a href="#faq">FAQ</a>
</p>

---

Your code works. Your tests pass. Your linter is green.

**But how does your code _feel_?**

`wtf-vibe` is a Claude Code skill that rates your codebase's emotional energy across **5 dimensions** — Chaos, Ego, Trust, Karma, and Energy. Then it streams the scoreboard live in your terminal.

Same insight as a 600-token code review. Delivered in **~80 tokens**. With personality.

Not a linter. Not a test suite. The friend who reviews your code, makes you laugh, and somehow uses 7x fewer tokens.

---

## Before / After

Same codebase. Same problems. Two completely different vibes.

<table>
<tr>
<th width="50%">🥱 Normal Code Review</th>
<th width="50%">🔥 wtf-vibe</th>
</tr>
<tr>
<td>

```
I've completed a thorough analysis of your
authentication module. Overall, the code
demonstrates a functional implementation,
however there are several areas that could
benefit from refinement to improve
maintainability and security posture.

The authentication module would benefit
from additional error handling, particularly
around the JWT verification flow. I noticed
that the nested conditional logic in the
login handler exceeds recommended cyclomatic
complexity thresholds and should be
considered for refactoring to improve
readability and reduce cognitive load on
future maintainers.

Additionally, the JWT secret appears to be
hardcoded in the source file. While this
follows a common pattern, you may want to
consider extracting it to an environment
variable to align with security best
practices and to facilitate easier rotation
in production environments.

Some functions in this module exceed the
recommended length and could be decomposed
into smaller, more focused units. The error
handling strategy is inconsistent across
endpoints and could benefit from
standardization. Test coverage is below
the recommended threshold.

I'd recommend prioritizing the security
items first, followed by the refactoring
opportunities. Let me know if you'd like
me to elaborate on any of these points or
draft specific implementation suggestions.
```

**~480 tokens of careful corporate hedging.**

You will scroll past this. You know you will.

</td>
<td>

```
🎰  W T F   V I B E  🎰

  Chaos Index    ████████░░  78/100  😰
  Ego Score      ██░░░░░░░░  23/100  🎓
  Trust Factor   ███░░░░░░░  29/100  😬
  Karma          ████░░░░░░  41/100  😐
  Energy         ⛈️  Stormy

  ✨ overall vibe: needs a hug

💀 auth.js — 47 nested ifs.
   JWT secret is "secret123".
   Trying its best. Not enough.

🧬 "haunted house. tests pass,
    but at what cost?"
```

**~85 tokens. Same insight. With personality.**

You will screenshot this. Send it to your team.

</td>
</tr>
</table>

> **~82% fewer tokens. 100% more shareable.**

---

## Install

**One line. That's it.**

```bash
mkdir -p ~/.claude/skills/wtf-vibe && curl -o ~/.claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

That's the global install — works in every project on your machine.

**Project-only install:**

```bash
mkdir -p .claude/skills/wtf-vibe && curl -o .claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

**Other agents:** drop `SKILL.md` into your agent's skills directory.

| Agent | Path |
|-------|------|
| Claude Code | `~/.claude/skills/wtf-vibe/SKILL.md` |
| Cursor | `.cursor/skills/wtf-vibe/SKILL.md` |
| Codex CLI | `.codex/skills/wtf-vibe/SKILL.md` |
| Gemini CLI | `.gemini/skills/wtf-vibe/SKILL.md` |
| Windsurf | `.windsurf/skills/wtf-vibe/SKILL.md` |

**Then restart your session and type `/wtf-vibe`.**

Zero dependencies. Just markdown.

---

## Dimensions

Five scores. No other tool measures these. That's the point.

| Dimension | Range | Meaning |
|-----------|-------|---------|
| **Chaos Index** | 0-100 (low good) | how tangled is it? |
| **Ego Score** | 0-100 (low good) | is it showing off? |
| **Trust Factor** | 0-100 (high good) | 3am deploy safe? |
| **Karma** | 0-100 (high good) | kind to next dev? |
| **Energy** | weather emoji | overall climate |

### Chaos Index — _low is good_
```
 0-20   🧘  Zen garden. Everything has a place.
21-40   🌿  A few weeds, but maintained.
41-60   🏚️  It works but nobody's proud of it.
61-80   😰  New devs cry during onboarding.
81-100  🔥  The codebase is a cry for help.
```

### Ego Score — _low is good_
```
 0-20   🤝  Humble, readable, unpretentious.
21-40   🎓  Some abstractions, mostly justified.
41-60   🤔  "Did we really need a factory for this?"
61-80   🧠  "I learned monads this weekend" energy.
81-100  🌌  Galaxy brain. Only the author understands it. Maybe.
```

### Trust Factor — _high is good_
```
 0-20   🚨  Would not deploy on a bet.
21-40   😬  Production incidents waiting to happen.
41-60   🤞  Works if nothing unexpected happens.
61-80   😌  Handles most things gracefully.
81-100  😴  Sleep-like-a-baby safe. Battle-tested.
```

### Karma — _high is good_
```
 0-20   💀  Hostile to the next developer.
21-40   😤  "Good luck" energy.
41-60   😐  Not great, not terrible.
61-80   🙂  Considerate. Easy to onboard.
81-100  🎁  A gift to humanity.
```

### Energy — _the weather report_
```
 ☀️   Sunny      Clean, calm, confident. A joy to work in.
 🌤️   Clear      Solid, professional. Gets the job done.
 🌥️   Cloudy     Works, but something feels off.
 ⛈️   Stormy     Tension everywhere. Storms incoming.
 🌀   Hurricane  Active disaster. Every change breaks something.
```

---

## Examples

### Example 1: The Startup MVP

> `/wtf-vibe`

```
🎰  W T F   V I B E  🎰

  Chaos Index    ███████░░░  67/100  😰
  Ego Score      █░░░░░░░░░  12/100  🤝
  Trust Factor   ███░░░░░░░  34/100  😬
  Karma          █████░░░░░  52/100  😐
  Energy         ⛈️  Stormy

  ✨ overall vibe: shipping fast, praying faster
```

**🏆 Vibe Leaders**
- `src/utils/format.ts` — the emotional support file. Clean, tested, reliable. The team therapist.
- `src/config/index.ts` — quiet, organized, knows its role. Respect.

**💀 Vibe Killers**
- `src/api/routes.js` — 1,400 lines. Auth, billing, webhooks, cron jobs, and what appears to be a TODO list from 2024. This file needs an intervention.
- `src/db/queries.js` — raw SQL strings concatenated with user input. Line 187 is a security incident waiting to clock in.

**🧬 Vibe Summary**

> "This codebase is a food truck. Fast, scrappy, gets the job done. The health inspector hasn't visited yet. When they do, it's going to be a long day."

**💊 Vibe Prescription**
1. Split `routes.js` before it becomes sentient. One file per domain.
2. Line 187 in `queries.js` — parameterize that query or start drafting the breach notification email.
3. Add error handling to the payment flow. The current strategy is "hope."

---

### Example 2: The Over-Engineered Monolith

> `/wtf-vibe src/core`

```
🎰  W T F   V I B E  🎰   ·   src/core

  Chaos Index    ████░░░░░░  41/100  🏚️
  Ego Score      █████████░  89/100  🌌
  Trust Factor   ███████░░░  71/100  😌
  Karma          ██░░░░░░░░  22/100  😤
  Energy         🌥️  Cloudy

  ✨ overall vibe: impressive and exhausting
```

**🏆 Vibe Leaders**
- `src/core/auth/tokens.ts` — tight, focused, well-tested. No nonsense. Chef's kiss.

**💀 Vibe Killers**
- `src/core/di/container.ts` — a dependency injection framework... for 6 services. This is like hiring a bouncer for a house party of 6 people.
- `src/core/base/AbstractBaseEntityServiceProviderFactory.ts` — the file name alone is 52 characters. If you need a factory to create a provider to create a service to create an entity... you've gone too far.

**🧬 Vibe Summary**

> "This codebase is a fresh bootcamp grad who learned every design pattern in one weekend and used ALL of them. The enthusiasm is admirable. The abstractions are not."

**💊 Vibe Prescription**
1. Delete `AbstractBaseEntityServiceProviderFactory.ts`. I don't know what it does. Neither does anyone else. Delete it and see what breaks.
2. The DI container is solving a problem that doesn't exist yet. Replace with direct imports. You're a startup, not Spring Boot.
3. Rename things so a human can read them. `UserService` > `AbstractUserServiceImpl`.

---

### Example 3: The Clean One

> `/wtf-vibe`

```
🎰  W T F   V I B E  🎰

  Chaos Index    █░░░░░░░░░  14/100  🧘
  Ego Score      █░░░░░░░░░  18/100  🤝
  Trust Factor   ████████░░  82/100  😴
  Karma          █████████░  88/100  🎁
  Energy         ☀️  Sunny

  ✨ overall vibe: immaculate
```

**🧬 Vibe Summary**

> "This codebase is a senior dev who's been through three rewrites and just wants things to work. It's tired, but reliable. Buy it a coffee."

---

## Usage

```
/wtf-vibe                        # Check the whole codebase
/wtf-vibe src/auth               # Check a specific directory
/wtf-vibe src/utils/format.ts    # Deep-check a single file
```

**What you get:**
1. **The Scoreboard** — all 5 dimensions, streamed live as Claude types it.
2. **Vibe Leaders** — the good code. Devs rarely hear what they're doing RIGHT.
3. **Vibe Killers** — the bad code. Named, shamed, and roasted with love.
4. **Vibe Summary** — your codebase as a person, in 2 sentences.
5. **Vibe Prescription** — specific fixes. Not "add comments." Real fixes.

---

## Why it uses fewer tokens

Most code review prompts ask for "thorough analysis" and Claude responds with paragraphs of corporate hedging. wtf-vibe asks for a **scoreboard + 3 callouts + 1 metaphor** — and that's it.

| Tool | Avg tokens per review | Memorable? |
|------|----------------------|------------|
| Standard `/review` | ~600-1000 | No, you scroll past |
| Generic linter output | ~200-400 | No, you ignore |
| **wtf-vibe** | **~80-150** | Yes, you screenshot |

Same coverage of the actual issues. Just delivered through pattern recognition + personality instead of throat-clearing.

---

## Philosophy

> Code has a personality. Every codebase tells a story about the people who built it — their experience, their time pressure, their ambitions, their compromises. **wtf-vibe** reads that story and tells it back to you.

Blunt. Warm. Specific. Never generic.

"Consider adding more comments" is useless. "Line 47 of `auth.js` does something unhinged and tells no one about it — a comment would be an act of mercy" is a **wtf-vibe**.

---

## FAQ

**Is this a real code quality tool?**
Yes, wrapped in personality. Every score maps to real patterns — cyclomatic complexity, abstraction depth, error handling coverage, naming clarity. It just doesn't bore you about it.

**Does it work with any language?**
Yes. Code vibes are universal. Spaghetti Python feels the same as spaghetti Java.

**Will my team actually use this?**
They'll use it once out of curiosity. Then they'll compete for scores. Then it becomes a ritual. That's the loop.

**Why does the scoreboard look "animated"?**
Because Claude streams text character-by-character in your terminal. Each line of the scoreboard appears in sequence as it's typed. No scripts, no setup — just the natural way the agent renders text.

---

## Cross-platform

Standard `.md` skill format. Just markdown — works anywhere skills work.

| Agent | Status |
|-------|--------|
| Claude Code | ✅ Native |
| Cursor | ✅ |
| Codex CLI | ✅ |
| Gemini CLI | ✅ |
| Windsurf | ✅ |
| Copilot | ✅ |

---

## Contributing

The five dimensions are opinionated. If you think there should be more (or fewer), open a PR.

The bar: **would you screenshot this score and share it?**

---

## License

MIT — vibe freely.

---

<p align="center">
  <strong>stop checking code quality. start checking code vibes.</strong>
</p>

<p align="center">
  <a href="https://star-history.com/#CYNERGY-APP/wtf-vibe&Date">
    <img src="https://api.star-history.com/svg?repos=CYNERGY-APP/wtf-vibe&type=Date" width="600" />
  </a>
</p>
