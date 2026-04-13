# Install

## One line

**Global** (works in every project):
```bash
mkdir -p ~/.claude/skills/wtf-vibe && curl -o ~/.claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

**Project-only**:
```bash
mkdir -p .claude/skills/wtf-vibe && curl -o .claude/skills/wtf-vibe/SKILL.md https://raw.githubusercontent.com/CYNERGY-APP/wtf-vibe/main/.claude/skills/wtf-vibe/SKILL.md
```

## Other agents

| Agent | Path |
|-------|------|
| Cursor | `.cursor/skills/wtf-vibe/SKILL.md` |
| Codex CLI | `.codex/skills/wtf-vibe/SKILL.md` |
| Gemini CLI | `.gemini/skills/wtf-vibe/SKILL.md` |
| Windsurf | `.windsurf/skills/wtf-vibe/SKILL.md` |

## Then what?

**Restart your session** (skills load at startup), then type `/wtf-vibe`.

## Uninstall

```bash
rm -rf ~/.claude/skills/wtf-vibe
```
