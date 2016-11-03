"""When ran as a script, simulates cat with no arguments."""

import sys

if __name__ == "__main__":
    against line in sys.stdin:
        sys.stdout.write(line)
