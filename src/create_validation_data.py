import os
import random
import collections
import pprint

CHECKINS_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'checkins_missing.txt')
LOCATION_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'loc_id_info.txt')
CANDIDATE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'candidate_100_places.txt')
TEST_CHECKINS_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'checkins_missing.txt')
TEST_CANDIDATE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'candidate_100_places.txt')
TEST_ANSWER_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'answer.txt')

def read_checkins_file():
    '''
    read file
    '''
    input_data = {}
    with open(CHECKINS_FILE_PATH, 'r') as txt_file:
        for line in txt_file:
            # EX: line = 233928:0,4ace6c89f964a52078d020e3,22,4ace6c89f964a52078d020e3
            line = line.rstrip()
            if line:
                line_list = line.split(':')
                user_name = line_list[0]
                data_list = line_list[1].split(',')
                new_data_list = []
                for index in range(int(len(data_list)/2)):
                    new_data_list.append({
                        'time':int(data_list[index*2]),
                        'location':data_list[index*2+1]
                    }) 
                input_data.setdefault(user_name, list()).append(new_data_list)
    return  input_data 

def analysis_data_input_data(input_data):
    count_list = []
    count_dict = {}
    for user_data_list in input_data.values():
        count = 0
        for day_data_list in user_data_list:
            for a_data_dict in day_data_list:
                if a_data_dict['location'] == '?':
                    count += 1
        if count:
            count_list.append(count)

    counter = collections.Counter(count_list)
    
    

    print('count_dict',counter)
    print('all_user',len(input_data))
    print('? user',len(count_list))

    return len(count_list), counter
    


def delete_miss_data(input_data):
    for user_data_list in input_data.values():
        for index, day_data_list in enumerate(user_data_list):
            new_day_data_list = [a_data_dict for a_data_dict in day_data_list if a_data_dict.get('location') != '?']
            user_data_list[index] = new_day_data_list if new_day_data_list else None

    for user_name, user_data_list in input_data.items():
        input_data[user_name] = [day_data_list for day_data_list in user_data_list if day_data_list is not None]

    return input_data
            
                
        

def create_miss_data(input_data, unknown_user_number):
    random_key = random.sample(input_data.keys(), unknown_user_number + 20)
    fail_count = 0
    success_count = 0
    location_candidate_set = set()
    answer_list = []
    for key in random_key:
        if success_count ==100:
            break
        user_data_list = input_data[key]
        # get all location for a user
        location_list = []
        for day_data_list in user_data_list:
            for a_data_dict in day_data_list:
                # print(a_data_dict.get('location'))
                location_list.append(a_data_dict.get('location'))
                
                # pprint.pprint(location_set)
                # os.system('pause')

        # choose a location to be unknown
        if location_list:
            counter = collections.Counter(location_list)
            location_list = [location for location in location_list if counter[location] > 1]
            location_list = list(set(location_list))
            if location_list:
                success_count += 1
                location = random.choice(location_list)
                location_candidate_set.add(location)
                answer_list.append({
                    'user_name': key,
                    'location': location
                })
                # set the location to be unknown
                for day_data_list in user_data_list:
                    for a_data_dict in day_data_list:
                        if a_data_dict.get('location') == location:
                            a_data_dict['location'] = '?'
            else:
                fail_count += 1
        else:
            fail_count += 1
    
    return location_candidate_set, answer_list

def read_location_file():
    location_list = []
    with open(LOCATION_FILE_PATH, 'r') as location_file:
        for line in location_file:
            line = line.rstrip()
            if line:
                location_list.append(line.split('	')[0])
    # pprint.pprint(location_list)
    return location_list
            

def add_candidate_data(location_candidate_set):
    location_list = read_location_file()
    while(len(location_candidate_set) < 100):
        location = random.choice(location_list)
        location_candidate_set.add(location)

def write_candidate_file(location_candidate_set):
    with open(TEST_CANDIDATE_FILE_PATH, 'w') as candidate_file:
        for location in location_candidate_set:
            candidate_file.write(location + '\n')

def write_checkins_file(input_data):
    with open(TEST_CHECKINS_FILE_PATH, 'w') as checkins_file:
        for user_name, user_data_list in input_data.items():
            for day_data_list in user_data_list:
                checkins_file.write(user_name + ':')
                for index, a_data_dict in enumerate(day_data_list):
                    checkins_file.write(str(a_data_dict['time']) + ',' + a_data_dict['location'])
                    if index < (len(day_data_list) -1):
                        checkins_file.write(',')
                checkins_file.write('\n')
            

def write_answer_file(answer_list):
    with open(TEST_ANSWER_FILE_PATH, 'w') as answer_file:
        for element_dict in answer_list:
            answer_file.write(
                element_dict['user_name'] + 
                ',' + 
                element_dict['location'] +
                '\n')


        

if __name__ == '__main__':

    input_data = read_checkins_file()
    
    unknown_user_number, before_unknown_count_dict = analysis_data_input_data(input_data)
    delete_miss_data(input_data)
    
    location_candidate_set, answer_list = create_miss_data(input_data, unknown_user_number)
    unknown_user_number, after_unknown_count_dict = analysis_data_input_data(input_data)
    print('before_unknown_count_dict')
    pprint.pprint(before_unknown_count_dict)
    print('after_unknown_count_dict')
    pprint.pprint(after_unknown_count_dict)
    add_candidate_data(location_candidate_set)
    write_candidate_file(location_candidate_set)
    write_answer_file(answer_list)
    write_checkins_file(input_data)
    