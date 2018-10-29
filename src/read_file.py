import os
import pprint
import configparser

config = configparser.ConfigParser()
config.read('setting.config')
READ_FILE_DIR = config['READ_FILE_DIR']
CHECKINS_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), READ_FILE_DIR['checkins_dir'], 'checkins_missing.txt')
LOCATION_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'loc_id_info.txt')
CANDIDATE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), READ_FILE_DIR['candidate_dir'], 'candidate_100_places.txt')


def read_checkins_file(condition = None):
    '''
    read checkins file

    Argument
        condition (String): 1.None = return all data
                            2.known_user = return known users
                            3.unknown_user = return unknown users
    '''
    result = None
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

    if condition is None:
        result = input_data
    else:
        result = delete_some_data(input_data, condition)
    
    return  result

def delete_some_data(input_data, condition = "unknown_user"):

    if condition != 'unknown_user' and condition != 'known_user':
        return input_data

    new_input_data = {}
    
    for user_name, user_data_list in input_data.items():
        
        if condition == "unknown_user":
            is_add = False
            if is_unknown(user_data_list):
                is_add = True
        else:
            is_add = True
            if is_unknown(user_data_list):
                is_add = False      
                         
        if is_add:
            new_input_data[user_name] = user_data_list
    
    return new_input_data
        
def is_unknown(user_data_list):
    for day_data_list in user_data_list:
        for a_data_dict in day_data_list:
            if a_data_dict['location'] == '?':
                return True
    return False

def read_candidate_file():
    candidate_list = []
    with open(CANDIDATE_FILE_PATH, 'r') as candidate_file:
        for line in candidate_file:
            line = line.rstrip()
            if line:
                candidate_list.append(line)
    return candidate_list

def read_known_location():
    location_dict = read_location_file()
    location_list = list(location_dict.keys())
    candidate_list = read_candidate_file()
    
    known_location_list = [location for location in location_list if location not in candidate_list]
    return known_location_list

def read_location_file():
    location_dict = {}
    with open(LOCATION_FILE_PATH, 'r') as location_file:
        for line in location_file:
            data_dict = {}
            line = line.rstrip()
            if line:
                data_list = line.split()
                data_dict['country'] = data_list[-1]
                data_dict['latitude'] = float(data_list[1])
                data_dict['longitude'] = float(data_list[2])
                data_dict['type'] = ' '.join(data_list[3:-1])
                location_dict[data_list[0]] = data_dict
            
            
    return location_dict

if __name__ == '__main__':
    # location_dict = read_location_file()
    # pprint.pprint(location_dict)
    # candidate_list = read_candidate_file()
    # pprint.pprint(candidate_list)
    # input_data = read_checkins_file()
    # print(len(input_data))
    # input_data = read_checkins_file('unknown_user')
    # pprint.pprint(input_data)
    # input_data = read_checkins_file('known_user')
    # print(len(input_data))
    # known_location_list = read_known_location()
    # print(len(known_location_list))
    # index = known_location_list.find('3fd66200')
    # numpy[user,index]
    pass