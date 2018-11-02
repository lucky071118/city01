import os
import collections
import pprint
from geopy import distance
import read_file

def recommend():
    home_dict = get_home_location()
    user_home_location_dict = get_user_home(home_dict)
    candidate_location_distance_dict = compute_distance(user_home_location_dict)
    result_rank = rank_candidate_location(candidate_location_distance_dict)
    print('The number of users that have home',len(result_rank))
    return result_rank

def get_home_location():
    location_dict = read_file.read_location_file()
    home_dict = {}
    for location, data in location_dict.items():
        if data['type'] == 'Home (private)':
            home_dict[location] = data
    return home_dict



def get_user_home(home_dict):
    unknown_user_checkins_dict = read_file.read_checkins_file('unknown_user')
    home_list = list(home_dict.keys())
    user_home_location_dict = {}
    for user_name, user_dict in unknown_user_checkins_dict.items():
        home_location = have_home(user_dict, home_list)
        if home_location:
            
            user_home_location_dict[user_name] = home_dict[home_location]
    # print('user_home_location_dict',len(user_home_location_dict))
    return user_home_location_dict

    

def have_home(user_dict, home_list):
    for day_dict in user_dict:
        for data_dict in day_dict:
            if data_dict['location'] in home_list:
                return data_dict['location']
    return None

def compute_distance(user_home_location_dict):
    candidate_list = read_file.read_candidate_file()
    location_info_dict = read_file.read_location_file()
    candidate_location_distance_dict = {}
    for user_name, home_location in user_home_location_dict.items():
        candidate_location_distance_dict[user_name] ={}
        for candidate_location in candidate_list:
            # candidate location
            candidate_position = (
                location_info_dict[candidate_location]['latitude'],
                location_info_dict[candidate_location]['longitude']
            )

            # user home location
            home_position = (
                home_location['latitude'],
                home_location['longitude']
            )
            distance_number = distance.distance(candidate_position, home_position).miles
            candidate_location_distance_dict[user_name][candidate_location] = distance_number
    return candidate_location_distance_dict

def rank_candidate_location(candidate_location_distance_dict):
    result_rank = {}
    for user_name, location_distance_dict in candidate_location_distance_dict.items():
        result_rank[user_name] = []
        new_rank_list = collections.Counter(location_distance_dict).most_common()
        for location_tuple in new_rank_list[::-1]:
            result_rank[user_name].append(location_tuple[0])
    
    return result_rank
            


if __name__ == '__main__':
    result_rank = recommend()
    pprint.pprint(result_rank)
                
        
    
