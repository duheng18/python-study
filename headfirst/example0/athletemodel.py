import pickle


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set(sanitize(t) for t in self))[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return AthleteList(temp1.pop(0), temp1.pop(0), temp1)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

# print(james.name + "'s fastest times are:" + str(james.top3()))
# print(julie.name + "'s fastest times are:" + str(julie.top3()))
# print(mikey.name + "'s fastest times are:" + str(mikey.top3()))
# print(sarah.name + "'s fastest times are:" + str(sarah.top3()))


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        # ['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18',
        # '2:55', '2:55', '2:22', '2-21', '2.22']
        # ['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01',
        # '3:10', '2-22', '2-01', '2.01', '2:16']
        # ['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22',
        # '2.49', '2:38', '2:40', '2.22', '2-31']
        # ['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10',
        # '3.21', '3-21', '3.01', '3.02', '2:59']
        # print(ath)
        all_athletes[ath.name] = ath
        # Sarah Sweeney
        # James Lee
        # Mikey McManus
        # Julie Jones
        # print(ath.name)
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    # print(all_athletes)
    return (all_athletes)



def get_from_store():
    all_athletes = []
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return all_athletes

# ['AthleteList', '__annotations__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'get_coach_data', 'get_from_store', 'james', 'julie',
# 'mikey', 'pickle', 'put_to_store', 'sanitize', 'sarah']
print(dir())
the_files=['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data=put_to_store(the_files)
# {'Sarah Sweeney': ['2:58', '2.58', '2:39', '2-25', '2-55', '2:54',
# '2.18', '2:55', '2:55', '2:22', '2-21', '2.22'], 'James Lee':
# ['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10',
# '2-22', '2-01', '2.01', '2:16'], 'Mikey McManus': ['2:22', '3.01',
# '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38', '2:40',
# '2.22', '2-31'], 'Julie Jones': ['2.59', '2.11', '2:11', '2:23',
# '3-10', '2-23', '3:10', '3.21', '3-21', '3.01', '3.02', '2:59']}
# print(data)

for each_athlete in data:
    # Sarah Sweeney 2002-6-17
    # James Lee 2002-3-14
    # Mikey McManus 2002-2-24
    # Julie Jones 2002-8-17
    print(data[each_athlete].name+' '+data[each_athlete].dob)

data_copy=get_from_store()
for each_athlete in data_copy:
    # Julie Jones 2002-8-17
    # Sarah Sweeney 2002-6-17
    # James Lee 2002-3-14
    # Mikey McManus 2002-2-24
    # Julie Jones 2002-8-17
    print(data_copy[each_athlete].name+' '+data_copy[each_athlete].dob)

