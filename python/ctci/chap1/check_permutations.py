def are_permutations(s: str, t: str) -> bool:
    """
    Checks whether s and t are permutations of esch other.
    Assumes that spaces matter and matching is case sensitive.
    Assumes that only ASCII characters are allowed in s and t.
    """
    if len(s) != len(t):
        return False

    counts = [0] * 128
    for c in s:
        counts[ord(c)] += 1

    for c in t:
        counts[ord(c)] -= 1

        if counts[ord(c)] < 0:
            return False

    return True


if __name__ == "__main__":
    assert(not are_permutations("a", "ab"))
    assert(not are_permutations("a", "A"))
    assert(not are_permutations("  ", "   "))
    assert(are_permutations("a", "a"))
    assert(are_permutations("   ", "   "))
    assert(are_permutations("cobweb", "bbewco"))
    assert(are_permutations("taco cat", "atco cta"))
    assert(are_permutations("baseddeds", "deadsbsed"))
