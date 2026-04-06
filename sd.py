def soundex(name):
    name = name.upper()

    codes = {'B':1,'F':1,'P':1,'V':1,
             'C':2,'G':2,'J':2,'K':2,'Q':2,'S':2,'X':2,'Z':2,
             'D':3,'T':3,
             'L':4,
             'M':5,'N':5,
             'R':6}

    first = name[0]
    nums = [str(codes.get(ch,0)) for ch in name]

    result = first
    prev = nums[0]

    for n in nums[1:]:
        if n != prev and n != '0':
            result += n
        prev = n

    result = result[:4].ljust(4,'0')
    return result


for w in ["Robert","Rupert","Ruia"]:
    print(w, "->", soundex(w))
