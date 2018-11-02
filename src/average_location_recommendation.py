import os
import collections
import pprint
from geopy import distance
import read_file

def recommend():
    unknown_user_checkins_dict = read_file.read_checkins_file('unknown_user')
    location_info_dict = read_file.read_location_file()
    average_location_dict = get_average_location(unknown_user_checkins_dict, location_info_dict)
    candidate_location_distance_dict = compute_distance(average_location_dict, location_info_dict)
    result_rank = rank_candidate_location(candidate_location_distance_dict)
    return result_rank

def get_average_location(unknown_user_checkins_dict, location_info_dict):
    average_location_dict = {}
    all_location_dict = {}
    for user_name, days_list in unknown_user_checkins_dict.items():
        all_location_dict[user_name] = {
            'latitude':list(),
            'longitude':list(),
        }
        for a_day_list in days_list:
            for data_dict in a_day_list:
                if data_dict['location'] != '?':
                    location = location_info_dict.get(data_dict['location'], None)
                    if location:
                        latitude = location['latitude']
                        longitude = location['longitude']
                        all_location_dict[user_name]['latitude'].append(latitude)
                        all_location_dict[user_name]['longitude'].append(longitude)

    for user_name, location_dict in all_location_dict.items():
        # print(user_name)
        sum_latitude = sum(location_dict['latitude'])
        sum_longitude = sum(location_dict['longitude'])
        average_latitude = sum_latitude/len(location_dict['latitude'])
        average_longitude = sum_longitude/len(location_dict['longitude'])
        average_location_dict[user_name] = (average_latitude, average_longitude)

    return average_location_dict
                    
    



def compute_distance(average_location_dict, location_info_dict):
    candidate_list = read_file.read_candidate_file()
    candidate_location_distance_dict ={}
    for user_name, average_location in average_location_dict.items():
        candidate_location_distance_dict[user_name] = {}
        for candidate_location in candidate_list:
            # candidate location
            candidate_position = (
                location_info_dict[candidate_location]['latitude'],
                location_info_dict[candidate_location]['longitude']
            )
            distance_number = distance.distance(candidate_position, average_location).miles
            candidate_location_distance_dict[user_name][candidate_location] = distance_number
    return candidate_location_distance_dict
    



def rank_candidate_location(candidate_location_distance_dict):
    result_rank = {}
    for user_name, location_distance_dict in candidate_location_distance_dict.items():
        result_rank[user_name] = []
        new_rank_list = collections.Counter(location_distance_dict).most_common()
        for location_tuple in new_rank_list[::-1]:
            # print(location_tuple)
            # os.system('pause')
            result_rank[user_name].append(location_tuple[0])
    
    return result_rank
            


if __name__ == '__main__':
    result_rank = recommend()
    pprint.pprint(result_rank)
                
        
    
