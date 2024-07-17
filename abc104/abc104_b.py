def isAC(S):
    if S[0] != "A":
        return False
    
    if S[2:-1].count("C") != 1:
        return False
    
    if sum(1 for c in S if c.isupper()) != 2:
        return False
    
    return True

print("AC" if isAC(input()) else "WA")
