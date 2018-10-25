import os
import collections
import pprint

INDEPENDENT_VARIABLE_DICT = {
    'user-based collaborative filtering' : 1,
    'item-based collaborative filtering' : 1,
    'geographical clustering phenomenon' : 1,
    'content-based filtering' : 1,
    'popularity' : 1
}


def sum(all_recommendation_rank_dict):
    all_user_score = compute_score(all_recommendation_rank_dict)
    sum_result = create_output_rank(all_user_score)
    return sum_result

def compute_score(all_recommendation_rank_dict):
    all_user_score = {}
    
    for key, rank_dict in all_recommendation_rank_dict.items():
        for user_name, rank_list in rank_dict.items():
            sum_score_dict = all_user_score.setdefault(user_name, {})
            for index, location in enumerate(rank_list):
                score = 100 - index
                sum_score = sum_score_dict.get(location,0)
                sum_score = sum_score + score * INDEPENDENT_VARIABLE_DICT[key]
                sum_score_dict[location] = sum_score
    return all_user_score

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