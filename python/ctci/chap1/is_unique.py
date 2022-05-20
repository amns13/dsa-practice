def has_all_unique_characters(s: str) -> bool:
    if not isinstance(s, str):
        return False
    seen = set()

    for c in s:
        if c in seen:
            return False
        seen.add(c)

    return True


def has_all_unique_characters_using_bit_vector(s: str) -> bool:
    if not isinstance(s, str):
        return False
    checker = 0
    for c in s:
        pos = ord(c) - ord('a')
        if ((checker >> pos) & 1) != 0:
            return False
        checker |= (1 << pos)
    return True


if __name__ == "__main__":
    functions = [has_all_unique_characters, has_all_unique_characters_using_bit_vector]
    for func in functions:
        assert(func("ab"))
        assert(func(""))
        assert(func("a"))
        assert(not func(23))
        assert(not func("aa"))
        assert(not func("bcdfeaza"))
