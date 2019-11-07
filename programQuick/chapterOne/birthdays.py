birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter name:(blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        boday = input()
        birthdays[name] = boday
        print('Birthday database updated.')
print(birthdays)
