#!/usr/bin/env python3
"""
wtf-vibe slot machine reveal animation.

Usage:
    animate.py --chaos 67 --ego 23 --trust 41 --karma 58 --energy stormy \
               --summary "shipping fast, praying faster" \
               [--label "src/auth"]

Falls back to plain print when not running in a TTY.
"""

import argparse
import random
import sys
import time

# ──────────────────────────── ANSI ────────────────────────────

ESC = "\033["
HIDE_CURSOR = ESC + "?25l"
SHOW_CURSOR = ESC + "?25h"
RESET = ESC + "0m"
BOLD = ESC + "1m"
DIM = ESC + "2m"
CLEAR_LINE = ESC + "2K"
CR = "\r"
UP = lambda n: f"{ESC}{n}A"

MAGENTA = ESC + "38;5;205m"
YELLOW = ESC + "38;5;220m"
GREEN = ESC + "38;5;82m"
RED = ESC + "38;5;196m"
CYAN = ESC + "38;5;87m"
GRAY = ESC + "38;5;240m"
PINK = ESC + "38;5;213m"
WHITE = ESC + "15m"

# ───────────────────────── score config ────────────────────────

DIMENSIONS = [
    # name, key, low_is_good, scale
    ("Chaos Index ", "chaos", True),
    ("Ego Score   ", "ego", True),
    ("Trust Factor", "trust", False),
    ("Karma       ", "karma", False),
]

ENERGY_EMOJI = {
    "sunny": "☀️ ",
    "clear": "🌤️ ",
    "cloudy": "🌥️ ",
    "stormy": "⛈️ ",
    "hurricane": "🌀",
}

ENERGY_LABEL = {
    "sunny": "Sunny",
    "clear": "Clear",
    "cloudy": "Cloudy",
    "stormy": "Stormy",
    "hurricane": "Hurricane",
}


def score_emoji(score: int, low_is_good: bool) -> str:
    if low_is_good:
        score = 100 - score
    if score >= 81:
        return "🎁"
    if score >= 61:
        return "🙂"
    if score >= 41:
        return "😐"
    if score >= 21:
        return "😬"
    return "💀"


def score_color(score: int, low_is_good: bool) -> str:
    s = (100 - score) if low_is_good else score
    if s >= 70:
        return GREEN
    if s >= 40:
        return YELLOW
    return RED


def bar(score: int, width: int = 12) -> str:
    filled = int(round(score / 100 * width))
    return "█" * filled + "░" * (width - filled)


# ───────────────────────── animation ───────────────────────────


def get_tty():
    """Return a writable handle to the user's terminal, or stdout."""
    try:
        return open("/dev/tty", "w")
    except OSError:
        return sys.stdout


def supports_animation() -> bool:
    return sys.stdout.isatty() or (
        hasattr(sys.stdout, "fileno") and sys.stdout.isatty()
    )


def write(out, s: str) -> None:
    out.write(s)
    out.flush()


def spin_reel(out, label: str, final_score: int, low_is_good: bool, duration: float = 0.9):
    """Spin one reel, then lock in the final score."""
    start = time.time()
    interval = 0.04
    decel = 0
    while True:
        elapsed = time.time() - start
        if elapsed >= duration and decel >= 5:
            break
        if elapsed >= duration:
            decel += 1
            interval += 0.04
        spin_score = random.randint(0, 100)
        spin_color = random.choice([MAGENTA, PINK, CYAN, YELLOW])
        line = (
            f"  {GRAY}{label}{RESET}  "
            f"{spin_color}{bar(spin_score)}{RESET}  "
            f"{spin_color}{spin_score:3d}/100{RESET}  ?"
        )
        write(out, CR + CLEAR_LINE + line)
        time.sleep(interval)

    # Lock-in flash
    for _ in range(2):
        write(out, CR + CLEAR_LINE +
              f"  {BOLD}{YELLOW}{label}  {bar(final_score)}  {final_score:3d}/100  ★{RESET}")
        time.sleep(0.08)
        write(out, CR + CLEAR_LINE)
        time.sleep(0.05)

    # Final settled line
    color = score_color(final_score, low_is_good)
    emoji = score_emoji(final_score, low_is_good)
    write(out, CR + CLEAR_LINE +
          f"  {DIM}{label}{RESET}  {color}{bar(final_score)}{RESET}  "
          f"{BOLD}{color}{final_score:3d}/100{RESET}  {emoji}\n")


def reveal_energy(out, energy: str):
    """Cycle through weather emojis then settle."""
    label = "Energy      "
    cycle = ["☀️ ", "🌤️ ", "🌥️ ", "⛈️ ", "🌀"]
    final_emoji = ENERGY_EMOJI.get(energy, "🌥️ ")
    final_label = ENERGY_LABEL.get(energy, "Cloudy")

    start = time.time()
    interval = 0.08
    decel = 0
    while True:
        elapsed = time.time() - start
        if elapsed >= 0.9 and decel >= 4:
            break
        if elapsed >= 0.9:
            decel += 1
            interval += 0.06
        e = random.choice(cycle)
        write(out, CR + CLEAR_LINE +
              f"  {GRAY}{label}{RESET}  {CYAN}{e}{RESET}  ?")
        time.sleep(interval)

    # Lock-in flash
    for _ in range(2):
        write(out, CR + CLEAR_LINE +
              f"  {BOLD}{YELLOW}{label}  {final_emoji} {final_label} ★{RESET}")
        time.sleep(0.08)
        write(out, CR + CLEAR_LINE)
        time.sleep(0.05)

    write(out, CR + CLEAR_LINE +
          f"  {DIM}{label}{RESET}  {final_emoji} {BOLD}{CYAN}{final_label}{RESET}\n")


def typewriter(out, text: str, color: str = WHITE, delay: float = 0.025):
    for ch in text:
        write(out, f"{color}{ch}{RESET}")
        time.sleep(delay)
    write(out, "\n")


def render_static(scores: dict, energy: str, summary: str, label: str = ""):
    """Plain non-animated output for non-TTY environments."""
    title = "WTF VIBE REPORT"
    if label:
        title += f"  ·  {label}"
    print()
    print(" ╔══════════════════════════════════════════════════╗")
    print(f" ║{title.center(50)}║")
    print(" ╠══════════════════════════════════════════════════╣")
    print(" ║                                                  ║")
    for label_text, key, low_is_good in DIMENSIONS:
        s = scores[key]
        e = score_emoji(s, low_is_good)
        line = f"  {label_text}  {bar(s)}  {s:3d}/100  {e}"
        print(f" ║{line.ljust(50)} ║")
    energy_line = f"  Energy        {ENERGY_EMOJI.get(energy,'🌥️ ')} {ENERGY_LABEL.get(energy,'Cloudy')}"
    print(f" ║{energy_line.ljust(50)} ║")
    print(" ║                                                  ║")
    print(" ╠══════════════════════════════════════════════════╣")
    summary_line = f"  Overall Vibe:  {summary}"
    print(f" ║{summary_line.ljust(50)} ║")
    print(" ╚══════════════════════════════════════════════════╝")
    print()


def render_animated(scores: dict, energy: str, summary: str, label: str = ""):
    out = get_tty()
    try:
        write(out, HIDE_CURSOR)

        # Header
        write(out, "\n")
        title = "🎰  W T F   V I B E  🎰"
        if label:
            title += f"   ·  {label}"
        write(out, f"  {BOLD}{PINK}{title}{RESET}\n")
        write(out, f"  {GRAY}{'─' * 50}{RESET}\n\n")
        time.sleep(0.3)

        # Spin each dimension
        for label_text, key, low_is_good in DIMENSIONS:
            spin_reel(out, label_text, scores[key], low_is_good)
            time.sleep(0.15)

        # Energy
        reveal_energy(out, energy)
        time.sleep(0.4)

        # Verdict
        write(out, f"\n  {GRAY}{'─' * 50}{RESET}\n")
        write(out, f"  {BOLD}{YELLOW}overall vibe:{RESET} ")
        typewriter(out, summary, color=BOLD + PINK, delay=0.03)
        write(out, "\n")
    finally:
        write(out, SHOW_CURSOR)
        if out is not sys.stdout:
            out.close()


# ────────────────────────────── main ─────────────────────────────


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chaos", type=int, required=True)
    p.add_argument("--ego", type=int, required=True)
    p.add_argument("--trust", type=int, required=True)
    p.add_argument("--karma", type=int, required=True)
    p.add_argument("--energy", type=str, required=True,
                   choices=["sunny", "clear", "cloudy", "stormy", "hurricane"])
    p.add_argument("--summary", type=str, required=True)
    p.add_argument("--label", type=str, default="")
    p.add_argument("--no-animate", action="store_true")
    args = p.parse_args()

    scores = {
        "chaos": args.chaos,
        "ego": args.ego,
        "trust": args.trust,
        "karma": args.karma,
    }

    use_animation = not args.no_animate
    try:
        with open("/dev/tty", "w"):
            pass
    except OSError:
        use_animation = False

    if use_animation:
        try:
            render_animated(scores, args.energy.lower(), args.summary, args.label)
        except KeyboardInterrupt:
            sys.stdout.write(SHOW_CURSOR)
            sys.exit(130)
    else:
        render_static(scores, args.energy.lower(), args.summary, args.label)


if __name__ == "__main__":
    main()
