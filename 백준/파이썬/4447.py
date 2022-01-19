n = int(input())

for i in range(n):
    hero = input()
    gc = hero.count('g') + hero.count('G')
    bc = hero.count('b') + hero.count('B')

    if gc > bc:
        print(f"{hero} is GOOD")
    
    elif gc < bc:
        print(f"{hero} is A BADDY")

    else:
        print(f"{hero} is NEUTRAL")