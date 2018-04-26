def meetsReqs(pw):
    return bool([c for c in pw if c.isupper()]) and bool([c for c in pw if c.islower()]) and bool([c for c in pw if c.isdigit()])

print meetsReqs('aB1')

def rating(pw):
    chars = '.?!&#,;:-_*'
    cs = [c for c in pw if c.isupper()]
    ls = [c for c in pw if c.islower()]
    ns = [c for c in pw if c.isdigit()]
    ss = [c for c in pw if c in chars]

    r = 1

    if cs:
        r += 1
    if ls:
        r += 1
    if ns:
        r += 1
    if ss:
        r += 1

    return 2*r

print rating('Ab1')
