def other(c):
    if c == 'A':
        return 'B'
    elif c == 'B':
        return 'A'
    else:
        raise RuntimeError(f'Expected A or B only, got {c}')
    
def locate_ogre_by_pig(line):
    words = line.split()
    claim = words[-1][:-1]

    if words[2] == 'not':
        return other(claim)
    else:
        return claim
    
def locate_ogre(a, b, c):
    ansA = locate_ogre_by_pig(a)
    ansB = locate_ogre_by_pig(b)
    ansC = locate_ogre_by_pig(c)

    if ansA == ansB == ansC:
        return ansA
    else:
        return 'INCONSISTENT'

if __name__ == '__main__':
    print(
        locate_ogre(
            'He is in Castle A.',
            'He is in Castle B.',
            'He is not in Castle A.'
        )
    )