def palindrom(s: str):
    i = 0
    length = len(s)
    if length % 2 != 0:
        return False
    else:
        if s[i] == s[-i-1] and i < length//2:
            i += 1
        else:
            return False
    return True


print(palindrom('Helloworld'))
print(palindrom('HelloolleH'))
