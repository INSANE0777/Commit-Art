"""
GitHub Contribution Matrix Generator

This script converts a user-provided text (ASCII letters) into a 7-row GitHub-contribution-style
matrix where `#` means "commit" and `.` means "no commit".

Usage:
    python github_matrix_generator.py

Features:
- Uses a 5x7 pixel font for A-Z and 0-9 plus some punctuation and space.
- Supports configurable spacing between letters and an optional scale factor to enlarge letters.
- Outputs a `matrix` string you can drop into your commit-generator script.
- Prints a visual preview using █ for filled pixels.

"""

from typing import List

# 5x7 font: each letter is 7 strings of 5 chars: '#' for filled, '.' for empty
FONT = {
    "A": [
        ".###.",
        "#...#",
        "#...#",
        "#####",
        "#...#",
        "#...#",
        "#...#",
    ],
    "B": [
        "####.",
        "#...#",
        "#...#",
        "####.",
        "#...#",
        "#...#",
        "####.",
    ],
    "C": [
        ".###.",
        "#...#",
        "#....",
        "#....",
        "#....",
        "#...#",
        ".###.",
    ],
    "D": [
        "####.",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "####.",
    ],
    "E": [
        "#####",
        "#....",
        "#....",
        "###..",
        "#....",
        "#....",
        "#####",
    ],
    "F": [
        "#####",
        "#....",
        "#....",
        "###..",
        "#....",
        "#....",
        "#....",
    ],
    "G": [
        ".###.",
        "#...#",
        "#....",
        "#.###",
        "#...#",
        "#...#",
        ".###.",
    ],
    "H": [
        "#...#",
        "#...#",
        "#...#",
        "#####",
        "#...#",
        "#...#",
        "#...#",
    ],
    "I": [
        "#####",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "#####",
    ],
    "J": [
        "..###",
        "...#.",
        "...#.",
        "...#.",
        "#..#.",
        "#..#.",
        ".##..",
    ],
    "K": [
        "#...#",
        "#..#.",
        "#.#..",
        "##...",
        "#.#..",
        "#..#.",
        "#...#",
    ],
    "L": [
        "#....",
        "#....",
        "#....",
        "#....",
        "#....",
        "#....",
        "#####",
    ],
    "M": [
        "#...#",
        "##.##",
        "#.#.#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
    ],
    "N": [
        "#...#",
        "##..#",
        "#.#.#",
        "#..##",
        "#...#",
        "#...#",
        "#...#",
    ],
    "O": [
        ".###.",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        ".###.",
    ],
    "P": [
        "####.",
        "#...#",
        "#...#",
        "####.",
        "#....",
        "#....",
        "#....",
    ],
    "Q": [
        ".###.",
        "#...#",
        "#...#",
        "#...#",
        "#.#.#",
        "#..#.",
        ".##.#",
    ],
    "R": [
        "####.",
        "#...#",
        "#...#",
        "####.",
        "#.#..",
        "#..#.",
        "#...#",
    ],
    "S": [
        ".###.",
        "#...#",
        "#....",
        ".###.",
        "....#",
        "#...#",
        ".###.",
    ],
    "T": [
        "#####",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
    ],
    "U": [
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        ".###.",
    ],
    "V": [
        "#...#",
        "#...#",
        "#...#",
        "#...#",
        ".#.#.",
        ".#.#.",
        "..#..",
    ],
    "W": [
        "#...#",
        "#...#",
        "#...#",
        "#.#.#",
        "#.#.#",
        "##.##",
        "#...#",
    ],
    "X": [
        "#...#",
        ".#.#.",
        "..#..",
        "..#..",
        ".#.#.",
        "#...#",
        "#...#",
    ],
    "Y": [
        "#...#",
        ".#.#.",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
    ],
    "Z": [
        "#####",
        "....#",
        "...#.",
        "..#..",
        ".#...",
        "#....",
        "#####",
    ],
    " ": [
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
    ],
    "0": [
        ".###.",
        "#...#",
        "#..##",
        "#.#.#",
        "##..#",
        "#...#",
        ".###.",
    ],
    "1": [
        "..#..",
        ".##..",
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        ".###.",
    ],
    "2": [
        ".###.",
        "#...#",
        "....#",
        "...#.",
        "..#..",
        ".#...",
        "#####",
    ],
    "3": [
        "####.",
        "....#",
        "...#.",
        "..##.",
        "....#",
        "#...#",
        ".###.",
    ],
    "4": [
        "...#.",
        "..##.",
        ".#.#.",
        "#..#.",
        "#####",
        "...#.",
        "...#.",
    ],
    "5": [
        "#####",
        "#....",
        "####.",
        "....#",
        "....#",
        "#...#",
        ".###.",
    ],
    "6": [
        ".###.",
        "#....",
        "#....",
        "####.",
        "#...#",
        "#...#",
        ".###.",
    ],
    "7": [
        "#####",
        "....#",
        "...#.",
        "..#..",
        ".#...",
        ".#...",
        ".#...",
    ],
    "8": [
        ".###.",
        "#...#",
        "#...#",
        ".###.",
        "#...#",
        "#...#",
        ".###.",
    ],
    "9": [
        ".###.",
        "#...#",
        "#...#",
        ".####",
        "....#",
        "....#",
        ".###.",
    ],
    "!": [
        "..#..",
        "..#..",
        "..#..",
        "..#..",
        ".....",
        "..#..",
        ".....",
    ],
    ".": [
        ".....",
        ".....",
        ".....",
        ".....",
        ".....",
        "..#..",
        ".....",
    ],
}


def scale_row(row: str, scale: int) -> str:
    """Scale a single 5-char row horizontally."""
    return ''.join(ch * scale for ch in row)


def scale_font(letter_rows: List[str], scale: int) -> List[str]:
    """Scale a 5x7 letter to (5*scale)x(7*scale)."""
    scaled = []
    for r in letter_rows:
        scaled_row = scale_row(r, scale)
        for _ in range(scale):
            scaled.append(scaled_row)
    return scaled


def text_to_matrix(text: str, spacing: int = 1, scale: int = 1, pad_top: int = 0, pad_bottom: int = 0) -> str:
    """
    Convert text to a matrix string where '#' => commit and '.' => no commit.

    - spacing: number of blank columns between letters
    - scale: integer multiplier for pixel size (1 = original 5x7)
    - pad_top/pad_bottom: number of empty rows added above/below to fit 7-row grid
    """
    text = text.upper()
    letters = []

    # prepare scaled letters
    for ch in text:
        if ch in FONT:
            letters.append(scale_font(FONT[ch], scale))
        else:
            # unknown char -> substitute with blank same-size
            blank = ['.' * (5 * scale) for _ in range(7 * scale)]
            letters.append(blank)

    if not letters:
        return ''

    # height of the output
    height = len(letters[0])  # 7*scale

    # build lines
    lines = []
    for row in range(height):
        line_parts = []
        for i, letter in enumerate(letters):
            line_parts.append(letter[row])
            if i != len(letters) - 1:
                line_parts.append('.' * spacing * scale)
        lines.append(''.join(line_parts))

    # add top/bottom padding rows if requested
    pad_row = '.' * len(lines[0]) if lines else ''
    for _ in range(pad_top):
        lines.insert(0, pad_row)
    for _ in range(pad_bottom):
        lines.append(pad_row)

    # Surround with extra empty rows to match GitHub's 7-row expectations if scale==1
    # But user can control via pad_top/pad_bottom
    return "\n".join(lines)


def matrix_to_github_block(matrix: str) -> str:
    """Replace '.' with '.' and '#' with '#' (already in correct format)"""
    # Ensure matrix uses '#' and '.' characters
    return matrix


def pretty_print(matrix: str) -> None:
    """Print a human-friendly preview using █ for '#' and space for '.'"""
    for line in matrix.split('\n'):
        print(''.join('█' if ch == '#' else ' ' for ch in line))


def generate_and_show(text: str, spacing: int = 1, scale: int = 1):
    # For GitHub we want 7 rows ideally; when scale=1 height=7
    pad_top = 0
    pad_bottom = 0
    matrix = text_to_matrix(text, spacing=spacing, scale=scale, pad_top=pad_top, pad_bottom=pad_bottom)

    # Convert font 1/0 style to '#' '.' style (font already uses '#' and '.')
    # But ensure characters are exactly '#' or '.'
    matrix = matrix.replace('1', '#').replace('0', '.')

    print("\n=== Preview ===\n")
    pretty_print(matrix)
    print("\n=== matrix string (drop this into your commit script) ===\n")
    print('"""')
    print(matrix)
    print('"""')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate GitHub contribution matrix from text')
    parser.add_argument('text', nargs='?', help='Text to render (quoting with spaces)', default=None)
    parser.add_argument('--spacing', '-s', type=int, default=1, help='Blank columns between letters (default 1)')
    parser.add_argument('--scale', '-k', type=int, default=1, help='Scale factor for pixels (integer >=1). Larger = wider letters')

    args = parser.parse_args()

    if args.text is None:
        args.text = input('Enter text to render (A-Z, 0-9, space, . !): ')

    generate_and_show(args.text, spacing=args.spacing, scale=max(1, args.scale))
