"""Convert a whole number into its written-out English words.

Examples:
    1       -> one
    31      -> thirty-one
    1000000 -> one million

Supports 0 through 1,000,000. Anything higher prints "Too high".
"""

ONES = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]

TENS = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
    "eighty", "ninety",
]


def _below_thousand(n: int) -> str:
    if n < 20:
        return ONES[n]
    if n < 100:
        tens_word = TENS[n // 10]
        ones_word = ONES[n % 10]
        return f"{tens_word}-{ones_word}" if n % 10 else tens_word
    hundreds_word = f"{ONES[n // 100]} hundred"
    remainder = n % 100
    return f"{hundreds_word} {_below_thousand(remainder)}" if remainder else hundreds_word


def number_to_words(n: int) -> str:
    if n > 1_000_000:
        return "Too high"
    if n == 1_000_000:
        return "one million"
    if n == 0:
        return "zero"

    parts = []
    thousands, remainder = divmod(n, 1000)
    if thousands:
        parts.append(f"{_below_thousand(thousands)} thousand")
    if remainder:
        parts.append(_below_thousand(remainder))
    return " ".join(parts)


if __name__ == "__main__":
    import sys

    value = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Enter a number: "))
    print(number_to_words(value))
