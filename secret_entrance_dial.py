"""Secret Entrance dial password (Advent of Code 2025, Day 1).

A safe dial starts pointing at 50. It receives a sequence of rotations,
each a direction (L = left/lower, R = right/higher) followed by a
distance in clicks. The dial wraps: turning left from 0 reaches 99,
turning right from 99 reaches 0.

The password equals the count of times the dial points exactly at 0
after any rotation.

Usage:
    python secret_entrance_dial.py <url>

The URL must return the rotation sequence as comma-separated tokens,
e.g. "L68, L30, R48, L5, R60, L55, L1, L99, R14, L82".
"""

import os
import sys
import urllib.request

DIAL_SIZE = 100
START_POSITION = 50


def fetch_rotations(url: str) -> list[str]:
    session = os.environ.get("AOC_SESSION")
    headers = {"Cookie": f"session={session}"} if session else {}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        text = response.read().decode("utf-8")
    return [token.strip() for token in text.replace(",", "\n").splitlines() if token.strip()]


def compute_password(rotations: list[str]) -> int:
    position = START_POSITION
    password = 0
    for rotation in rotations:
        direction, distance = rotation[0], int(rotation[1:])
        if direction == "L":
            position = (position - distance) % DIAL_SIZE
        elif direction == "R":
            position = (position + distance) % DIAL_SIZE
        else:
            raise ValueError(f"Unknown direction in rotation: {rotation!r}")
        if position == 0:
            password += 1
    return password


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python secret_entrance_dial.py <url>")
        sys.exit(1)

    rotations = fetch_rotations(sys.argv[1])
    print(compute_password(rotations))
