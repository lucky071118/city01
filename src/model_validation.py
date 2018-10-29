import collections
import os
import pprint
from numpy import percentile

RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.txt')
ANSWER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'answer.txt')


def test_result():
    output_result_dict, answer_dict = read_file()
    sum_score, sum_hit, index_list = validation(output_result_dict, answer_dict)
    index_counter = collections.Counter(index_list)
    print('score',sum_score/10000)
    print('First hit',sum_hit/100)
    quartiles = percentile(index_list,[25,50,75])
    print('25',quartiles[0])
    print('50',quartiles[1])
    print('75',quartiles[2])
    print('*'*10 + 'index_counter' + '*'*10)
    print('hit rank : number of users')
    pprint.pprint(index_counter.most_common())

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
    sum_score = 0
    sum_hit = 0
    index_list = []
    for user_name, rank_location_list in output_result_dict.items():
        answer_location = answer_dict.get(user_name)
        index, score, hit = get_score(answer_location, rank_location_list)
        sum_score += score
        sum_hit += hit
        index_list.append(index+1)
    return sum_score, sum_hit, index_list


        

def get_score(answer_location, rank_location_list):
    score = 0
    hit = 0
    for index, location in enumerate(rank_location_list):
        if location == answer_location:
            score = 100- index
            if index == 0:
                hit = 1
            break
    return index, score, hit





if __name__ == '__main__':
    pass 