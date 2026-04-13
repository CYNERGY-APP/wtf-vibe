# Install

## One line

**Global** (works in every project):
```bash
git clone https://github.com/CYNERGY-APP/wtf-vibe ~/.claude/skills/wtf-vibe
```

**Project-only**:
```bash
git clone https://github.com/CYNERGY-APP/wtf-vibe .claude/skills/wtf-vibe
```

## Other agents

| Agent | Path |
|-------|------|
| Cursor | `.cursor/skills/wtf-vibe/` |
| Codex CLI | `.codex/skills/wtf-vibe/` |
| Gemini CLI | `.gemini/skills/wtf-vibe/` |
| Windsurf | `.windsurf/skills/wtf-vibe/` |

## Then what?

**Restart your session** (skills load at startup), then type `/wtf-vibe`.

## Requirements

Python 3 (already installed on macOS/Linux). Zero dependencies.

## Update

```bash
cd ~/.claude/skills/wtf-vibe && git pull
```

## Uninstall

```bash
rm -rf ~/.claude/skills/wtf-vibe
```
