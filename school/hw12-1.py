import re


def demo(s: str) -> tuple:
    lower = len(re.findall(r'[a-z]', s))
    upper = len(re.findall(r'[A-Z]', s))
    number = len(re.findall(r'\d', s))
    other = len(s) - lower - upper - number
    return lower, upper, number, other
