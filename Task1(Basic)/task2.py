def first_non_repeating_letter(s):
    s = s.lower()
    for ch in s:
        length = len(s)
        s = s.replace(ch, "")
        if len(s) == length-1:
            return ch
    return None


if __name__ == "__main__":
    print("Test \'stress\':", first_non_repeating_letter("stress"))
    print("Test \'sTreSS\':", first_non_repeating_letter("sTreSS"))
    print("Test \'heellooh\':", first_non_repeating_letter("heellooh"))
