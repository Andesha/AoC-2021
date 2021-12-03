import sys

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eyes = ['amb','blu','brn','gry','grn','hzl','oth']
extra = 'cid'

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
blanks = [0]
blanks.extend([i for i, x in enumerate(content) if x == ''])

blocks = zip(blanks, blanks[1:])
valid = 0
for l,r in blocks:
    passport = ' '.join(content[l:r+1])
    passport_dict = dict(x.split(':',2) for x in passport.split())

    print(passport_dict)

    if not all(x in passport for x in required):
        continue

print('Valid: ', valid)
