def p_check(s):
    if len(s)%2!=0:
        return "no"
    cntf=0
    cntb=0
    for i in s:
        if i=='(':
            cntf+=1
        elif i==')':
            cntb+=1
        if cntb>cntf:
            return "no"
    if cntf==cntb:
        return "yes"
    else:
        return "no"

par= input("Enter parentheses string: ")
print(p_check(par))