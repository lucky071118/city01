import collections
import os
import pprint
import configparser
from numpy import percentile
import matplotlib.pyplot as plt

config = configparser.ConfigParser()
config.read('setting.config')
READ_FILE_DIR = config['READ_FILE_DIR']['file_dir']

RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.txt')
ANSWER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), READ_FILE_DIR, 'answer.txt')


def test_result():
    output_result_dict, answer_dict = read_file()
    index_list, user_rank_dict = validation(output_result_dict, answer_dict)
    index_counter = collections.Counter(index_list)
    print('avg. rank index',sum(index_list)/100)
    quartiles = percentile(index_list,[25,50,75])
    print('25 Q1 =',quartiles[0])
    print('50 Q2 = ',quartiles[1])
    print('75 Q3 = ',quartiles[2])
    print('*'*10 + 'index_counter' + '*'*10)
    print('hit rank : number of users')
    counter_list = index_counter.most_common()
    for counter_tuple in counter_list:
        print('rank index = ', counter_tuple[0], end='   ')
        print('number of people = ', counter_tuple[1], end='   ')
        print('name = ', user_rank_dict[counter_tuple[0]])
        
    # pprint.pprint(counter_list)
    index_dict = {}
    x_list= []
    y_list = []
    for counter_tuple in counter_list:
        index_dict[counter_tuple[0]] = counter_tuple[1]
    
    x_list = list(index_dict.keys())
    x_list.sort()
    for rank_index in x_list:
        y_list.append(index_dict[rank_index])

    plt.plot(x_list, y_list, color='red')
    plt.show()

def read_file():
    output_result_dict = {}
    answer_dict = {}
    with open(RESULT_FILE, 'r') as result_file:
        for line in result_file:
            line = line.rstrip()
            line_list = line.split(':')
            user_name = line_list[0]
            location_list = line_list[1].split(',')
            output_result_dict[user_name] = location_list

    with open(ANSWER_FILE, 'r') as answer_file:
        for line in answer_file:
            line = line.rstrip()
            user_name = line.split(',')[0]
            answer_location = line.split(',')[1]
            answer_dict[user_name] = answer_location
    
    return output_result_dict, answer_dict

def validation(output_result_dict, answer_dict):
    index_list = []
    user_rank_dict ={} 
    for user_name, rank_location_list in output_result_dict.items():
        answer_location = answer_dict.get(user_name)
        index = get_score(answer_location, rank_location_list)
        index_list.append(index)
        user_rank_dict.setdefault(index,[]).append(user_name)
    return index_list, user_rank_dict


        

def get_score(answer_location, rank_location_list):
    score = 0
    for index, location in enumerate(rank_location_list):
        if location == answer_location:
            break
    return index+1





if __name__ == '__main__':
    pass 