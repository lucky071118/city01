import os
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


def read_candidate_file():
    candidate_list = []
    with open(CANDIDATE_FILE_PATH, 'r') as candidate_file:
        for line in candidate_file:
            line = line.rstrip()
            if line:
                candidate_list.append(line)
    return candidate_list


def read_location_file():
    location_dict = {}
    with open(LOCATION_FILE_PATH, 'r') as location_file:
        for line in location_file:
            data_dict = {}
            line = line.rstrip()
            if line:
                data_list = line.split()
                data_dict['country'] = data_list[-1]
                data_dict['latitude'] = data_list[1]
                data_dict['longitude'] = data_list[2]
                data_dict['type'] = ' '.join(data_list[3:-1])
                location_dict[data_list[0]] = data_dict
            
            
    return location_dict

if __name__ == '__main__':
    location_dict = read_location_file()
    pprint.pprint(location_dict)
    # candidate_list = read_candidate_file()
    # pprint.pprint(candidate_list)
    # input_data = read_checkins_file()
    # pprint.pprint(input_data)
