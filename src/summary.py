import os
import collections
import pprint
import configparser

config = configparser.ConfigParser()
config.read('setting.config')
HOME_INDEPENDENT_VARIABLE_DICT = config['HOME_PARAMETER']
NON_VISITOR_INDEPENDENT_VARIABLE_DICT = config['NON_VISITOR_PARAMETER']
VISITOR_INDEPENDENT_VARIABLE_DICT = config['VISITOR_PARAMETER']
INDEPENDENT_VARIABLE_DICT = {
    'home':HOME_INDEPENDENT_VARIABLE_DICT,
    'visitor':VISITOR_INDEPENDENT_VARIABLE_DICT,
    'non_visitor':NON_VISITOR_INDEPENDENT_VARIABLE_DICT
}






def sum(all_recommendation_rank_dict, user_category_dict):
    all_user_score = {}
    for category, user_list in user_category_dict.items():
        category_user_score = compute_score(all_recommendation_rank_dict, category, user_list)
        all_user_score.update(category_user_score)
    sum_result = create_output_rank(all_user_score)
    return sum_result


    

def compute_score(all_recommendation_rank_dict, category, user_list):
    category_user_score = {}
    
    for key, rank_dict in all_recommendation_rank_dict.items():
        for user_name, rank_list in rank_dict.items():
            if user_name in user_list:
                sum_score_dict = category_user_score.setdefault(user_name, {})
                for index, location in enumerate(rank_list):
                    score = 100 - index
                    sum_score = sum_score_dict.get(location,0)
                    sum_score = sum_score + score * int(INDEPENDENT_VARIABLE_DICT[category][key])
                    sum_score_dict[location] = sum_score
    return category_user_score

def create_output_rank(all_user_score):
    result = {}
    for user_name, sum_score_dict in all_user_score.items():
        rank = []
        counter = collections.Counter(sum_score_dict)
        sorted_location_list = counter.most_common(len(sum_score_dict))
        # pprint.pprint(sorted_location_list)
        # os.system('pause')
        for location_tuple in sorted_location_list:
            rank.append(location_tuple[0])
        result[user_name] = rank
    return result

if __name__ == '__main__':
    pass