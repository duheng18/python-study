import re

# ['str1', 'str2', 'str3']
# print(re.split(':', 'str1:str2:str3'))

DATA = ('Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA',
        )
for data in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', data))
