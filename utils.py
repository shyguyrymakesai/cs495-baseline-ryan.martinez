def lower_concat(strings: list[str]) -> str:
    ret = ""
    for x in strings:
        ret += x.lower()
    return ret
