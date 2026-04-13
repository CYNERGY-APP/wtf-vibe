# Install

## One line. That's it.

```bash
mkdir -p .claude/skills/wtf-vibe && curl -o .claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

## Global install (all your projects)

```bash
mkdir -p ~/.claude/skills/wtf-vibe && curl -o ~/.claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

## Other agents

| Agent | Where to put it |
|-------|----------------|
| Cursor | `.cursor/skills/wtf-vibe/SKILL.md` |
| Codex CLI | `.codex/skills/wtf-vibe/SKILL.md` |
| Gemini CLI | `.gemini/skills/wtf-vibe/SKILL.md` |
| Windsurf | `.windsurf/skills/wtf-vibe/SKILL.md` |

## Then what?

**Restart your session** (skills load at startup, not mid-session), then type `/wtf-vibe`.
