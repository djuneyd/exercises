def anagram(s, t):
    if len(s) == len(t) and set(s) == set(t):
        for i in range(len(s)):
            if s[i] in t:
                continue
            else:
                return False
        return True
    else:
        return False
print(anagram('anagram', 'magaran'))