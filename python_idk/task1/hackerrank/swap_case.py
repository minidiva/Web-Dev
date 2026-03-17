def swap_case(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += i.upper()
        elif 'A' <= i <= 'Z':
            result += i.lower()
        else:
            result += i
    return result

print(swap_case("Nigga"))