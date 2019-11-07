import re

phoneNumRegex = re.compile(r'((\(\d\d\d\)) (\d\d\d-\d\d\d\d))')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
# print('phone number found:' + mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group())
# print(mo.groups())

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
# print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
# print(mo3.group())
# print(mo3.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo4 = batRegex.search('The Adventures of Batman')
# print(mo4.group())
mo5 = batRegex.search('The Adventures of Batwoman')
# print(mo5.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())

# Batman
# Batwoman
# Batwowowowoman
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
mo3 = None

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
# print(mo1.group())
mo2 = haRegex.search('Ha')
# mo2==None

greedHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedHaRegex.search('HaHaHaHaHa')
# print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())

# ['415-555-9999', '212-555-0000']
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

namesRegex=re.compile(r'Agent \w+')
# CENSORED gave the secret documents to CENSORED.
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex=re.compile(r'Agent (\w)\w+')
agent=agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.
# print(agent)

phoneRegex=re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')