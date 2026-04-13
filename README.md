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

`wtf-vibe` is a Claude Code skill that rates your codebase's emotional energy across **5 dimensions** — Chaos, Ego, Trust, Karma, and Energy. It tells you what no tool ever tells you: **the vibe**.

Not a linter. Not a test suite. The friend who reviews your code and somehow makes the feedback entertaining.

---

## Before / After

You asked for a code review. Here's what you got:

<table>
<tr>
<th width="50%">🥱 Normal Code Review</th>
<th width="50%">🔥 wtf-vibe</th>
</tr>
<tr>
<td>

```
The authentication module could benefit
from additional error handling. Consider
refactoring the nested conditionals for
improved readability. The JWT
implementation follows standard patterns
but may need additional validation.
Some functions exceed recommended
complexity thresholds.
```

</td>
<td>

```
╔══════════════════════════════════════╗
║         WTF VIBE REPORT             ║
╠══════════════════════════════════════╣
║                                      ║
║  Chaos Index:   78/100  😰          ║
║  Ego Score:     23/100  🤝          ║
║  Trust Factor:  29/100  😬          ║
║  Karma:         41/100  😐          ║
║  Energy:        ⛈️ Stormy            ║
║                                      ║
╠══════════════════════════════════════╣
║  Overall Vibe:  needs a hug          ║
╚══════════════════════════════════════╝

💀 auth.js — 47 nested ifs. The JWT
   secret is "secret123". It's trying
   its best. Its best is not enough.

🧬 "This codebase is a haunted house.
    There are rooms nobody has entered
    in years. The tests pass, but at
    what cost?"
```

</td>
</tr>
</table>

Same code. One you'll ignore. One you'll screenshot.

---

## Install

One line. No setup. No config.

| Agent | Command |
|-------|---------|
| **Claude Code** | `mkdir -p .claude/skills/wtf-vibe && curl -o .claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md` |
| **Cursor** | Copy `SKILL.md` to `.cursor/skills/wtf-vibe/SKILL.md` |
| **Codex CLI** | Copy `SKILL.md` to `.codex/skills/wtf-vibe/SKILL.md` |
| **Gemini CLI** | Copy `SKILL.md` to `.gemini/skills/wtf-vibe/SKILL.md` |
| **Any agent** | Place `SKILL.md` in your agent's skills directory |

Global install (all projects):
```bash
mkdir -p ~/.claude/skills/wtf-vibe && curl -o ~/.claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

Then just type `/wtf-vibe` and watch.

---

## Dimensions

Five scores. No other tool measures these. That's the point.

```
╔═══════════════════════════════════════════════════════════╗
║                    THE FIVE DIMENSIONS                    ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  CHAOS INDEX    ████████████░░░░░░░░  how tangled is it?  ║
║  EGO SCORE      ████░░░░░░░░░░░░░░░░  is it showing off?  ║
║  TRUST FACTOR   ██████░░░░░░░░░░░░░░  3am deploy safe?    ║
║  KARMA          ████████████████░░░░  kind to next dev?   ║
║  ENERGY         ⛈️  overall weather                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

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
 ☀️  Sunny      Clean, calm, confident. A joy to work in.
 🌤️  Clear      Solid, professional. Gets the job done.
 🌥️  Cloudy     Works, but something feels off.
 ⛈️  Stormy     Tension everywhere. Storms incoming.
 🌀  Hurricane  Active disaster. Every change breaks something.
```

---

## Examples

### Example 1: The Startup MVP

> `/wtf-vibe`

```
 ╔══════════════════════════════════════════════════╗
 ║               WTF VIBE REPORT                    ║
 ╠══════════════════════════════════════════════════╣
 ║                                                  ║
 ║  Chaos Index:   67/100  😰                      ║
 ║  Ego Score:     12/100  🤝                      ║
 ║  Trust Factor:  34/100  😬                      ║
 ║  Karma:         52/100  😐                      ║
 ║  Energy:        ⛈️ Stormy                        ║
 ║                                                  ║
 ╠══════════════════════════════════════════════════╣
 ║  Overall Vibe:  shipping fast, praying faster    ║
 ╚══════════════════════════════════════════════════╝
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
 ╔══════════════════════════════════════════════════╗
 ║               WTF VIBE REPORT                    ║
 ╠══════════════════════════════════════════════════╣
 ║                                                  ║
 ║  Chaos Index:   41/100  🏚️                      ║
 ║  Ego Score:     89/100  🌌                      ║
 ║  Trust Factor:  71/100  😌                      ║
 ║  Karma:         22/100  😤                      ║
 ║  Energy:        🌥️ Cloudy                       ║
 ║                                                  ║
 ╠══════════════════════════════════════════════════╣
 ║  Overall Vibe:  impressive and exhausting        ║
 ╚══════════════════════════════════════════════════╝
```

**🏆 Vibe Leaders**
- `src/core/auth/tokens.ts` — tight, focused, well-tested. No nonsense. Chef's kiss.

**💀 Vibe Killers**
- `src/core/di/container.ts` — a dependency injection framework... for 6 services. This is like hiring a bouncer for a house party of 6 people.
- `src/core/base/AbstractBaseEntityServiceProviderFactory.ts` — the file name alone is 52 characters. If you need a factory to create a provider to create a service to create an entity... you've gone too far.

**🧬 Vibe Summary**

> "This codebase is a fresh bootcamp grad who learned every design pattern in one weekend and used ALL of them. The enthusiasm is admirable. The abstractions are not."

**💊 Vibe Prescription**
1. Delete `AbstractBaseEntityServiceProviderFactory.ts`. I don't know what it does. Neither does anyone else. Delete it and see what breaks. If nothing breaks, you have your answer.
2. The DI container is solving a problem that doesn't exist yet. Replace with direct imports. You're a startup, not Spring Boot.
3. Rename things so a human can read them. `UserService` > `AbstractUserServiceImpl`.

---

### Example 3: The Clean One

> `/wtf-vibe`

```
 ╔══════════════════════════════════════════════════╗
 ║               WTF VIBE REPORT                    ║
 ╠══════════════════════════════════════════════════╣
 ║                                                  ║
 ║  Chaos Index:   14/100  🧘                      ║
 ║  Ego Score:     18/100  🤝                      ║
 ║  Trust Factor:  82/100  😴                      ║
 ║  Karma:         88/100  🎁                      ║
 ║  Energy:        ☀️ Sunny                         ║
 ║                                                  ║
 ╠══════════════════════════════════════════════════╣
 ║  Overall Vibe:  immaculate                       ║
 ╚══════════════════════════════════════════════════╝
```

**🏆 Vibe Leaders**
- Honestly? The whole thing. Consistent naming, small files, clear boundaries. Whoever wrote this cares.

**💀 Vibe Killers**
- `scripts/deploy.sh` — the only file that radiates chaos. 200 lines, no comments, nested if-else from hell. Every codebase has one cursed shell script. This is yours.

**🧬 Vibe Summary**

> "This codebase is a senior dev who's been through three rewrites and just wants things to work. It's tired, but reliable. Buy it a coffee."

**💊 Vibe Prescription**
1. Fix `deploy.sh`. It's the one dark room in an otherwise well-lit house.
2. That's it. You're doing great. Seriously.

---

## Usage

```
/wtf-vibe                        # Check the whole codebase
/wtf-vibe src/auth               # Check a specific directory
/wtf-vibe src/utils/format.ts    # Deep-check a single file
```

**What you get:**
1. **The Scoreboard** — five scores, one glance. Screenshot it. Share it. Compete.
2. **Vibe Leaders** — the good code. Devs rarely hear what they're doing RIGHT.
3. **Vibe Killers** — the bad code. Named, shamed, and roasted with love.
4. **Vibe Summary** — your codebase described as a person. In 2 sentences.
5. **Vibe Prescription** — specific fixes. Not "add comments." Real fixes.

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

**Can I use this in CI/CD?**
Not yet. But imagine: `PR blocked: Chaos Index exceeded 80. Fix the vibe before merging.`

**Will my team actually use this?**
They'll use it once out of curiosity. Then they'll compete for scores. Then it becomes a ritual. That's the loop.

**How is this different from a linter?**
A linter tells you semicolons are missing. **wtf-vibe** tells you your codebase is having an existential crisis. Different tools. Different jobs.

---

## Cross-platform

Standard `.md` skill format. Works everywhere:

| Agent | Status |
|-------|--------|
| Claude Code | ✅ Native |
| Cursor | ✅ |
| Codex CLI | ✅ |
| Gemini CLI | ✅ |
| Windsurf | ✅ |
| Copilot | ✅ |
| Any `.md` skill agent | ✅ |

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
