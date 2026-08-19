import sys
import time
from datetime import datetime


DIGITS = {
    "0": ["█████", "█   █", "█   █", "█   █", "█   █", "█   █", "█████"],
    "1": ["  █  ", " ██  ", "  █  ", "  █  ", "  █  ", "  █  ", "█████"],
    "2": ["█████", "    █", "    █", "█████", "█    ", "█    ", "█████"],
    "3": ["█████", "    █", "    █", "█████", "    █", "    █", "█████"],
    "4": ["█   █", "█   █", "█   █", "█████", "    █", "    █", "    █"],
    "5": ["█████", "█    ", "█    ", "█████", "    █", "    █", "█████"],
    "6": ["█████", "█    ", "█    ", "█████", "█   █", "█   █", "█████"],
    "7": ["█████", "    █", "    █", "   █ ", "  █  ", " █   ", "█    "],
    "8": ["█████", "█   █", "█   █", "█████", "█   █", "█   █", "█████"],
    "9": ["█████", "█   █", "█   █", "█████", "    █", "    █", "█████"],
    ":": ["     ", "  █  ", "  █  ", "     ", "  █  ", "  █  ", "     "],
}

# Standard terminal color codes; no additional packages are required.
COLORS = [31, 32, 33, 36, 35, 34]


def make_large_time(value):
    """Convert a time such as 03:24:18 into seven rows of large digits."""
    return "\n".join(
        "  ".join(DIGITS[character][row] for character in value)
        for row in range(7)
    )


try:
    # Clear the screen and hide the cursor while the clock is running.
    sys.stdout.write("\033[2J\033[?25l")

    while True:
        current_time = datetime.now()
        clock_text = current_time.strftime("%I:%M:%S").lstrip("0")
        period = current_time.strftime("%p")
        color = COLORS[int(time.time()) % len(COLORS)]

        display = make_large_time(clock_text)
        display_width = len(display.splitlines()[0])
        sys.stdout.write(
            f"\033[H\033[{color}m{display}\n\n"
            f"{period:^{display_width}}\033[0m\033[J"
        )
        sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    # Restore the normal terminal color and cursor before exiting.
    sys.stdout.write("\033[0m\033[?25h\n")
    sys.stdout.flush()
