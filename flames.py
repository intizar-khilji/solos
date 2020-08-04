your_name = input('Enter your name : ').lower()
your_partner_name = input('Enter Your Partner Name : ').lower()
flames = 'FLAMES'
l = [x for x in your_name if x not in your_partner_name]
m = [x for x in your_partner_name if x not in your_name]
l.extend(m)
a = b = len(l)
while len(flames) > 1:
    while True:
        if a > len(flames):
            a -= len(flames)
        else:
            break
    flames = flames.replace(flames[a-1], '')
    a = a+b-1
if flames == 'F':
    print('Friendship')
elif flames == 'L':
    print('Love')
elif flames == 'A':
    print('Affection')
elif flames == 'M':
    print('Marriage')
elif flames == 'E':
    print('Enemy')
elif flames == 'S':
    print('Sibling')