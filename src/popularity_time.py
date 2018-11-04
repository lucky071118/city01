import read_file
import pprint
from collections import Counter

def total_popularity():
    read_data = {}
    read_data = read_file.read_checkins_file()
    total_location = read_data.values()
    popularity = {}
    for daily_data in total_location:
        for daily_location in daily_data:
            for location_data in daily_location:
                if popularity.get(location_data["location"]) != None:
                    popularity[location_data["location"]] +=1
                else:
                    popularity[location_data["location"]] = 1

    return popularity

def candidate_popularity():
    candidates = [] 
    candidates = read_file.read_candidate_file()
    popularity = {}
    popularity = total_popularity()
    result = {}
    for single_candidate in candidates:
        if popularity.get(single_candidate) != None:
            result[single_candidate] = popularity.get(single_candidate)
        else:
            result[single_candidate] = 0

    location_sum = result.items()
    location_list = []
    candidate_list = []
    for location_data in location_sum:
        location_list.append([location_data[1],location_data[0]])
    location_list.sort(reverse=True)
    for i in range(0,len(location_list)):
        candidate_list.append(location_list[i][1])
    
    return candidate_list
def total_time_popularity():
    read_data = {}
    read_data = read_file.read_checkins_file()
    total_location = read_data.values()
    popularity = {}
    for daily_data in total_location:
        for daily_location in daily_data:
            for location_data in daily_location:
                if popularity.get(location_data["time"]) == None:
                    popularity[location_data["time"]] = {}
                if popularity[location_data["time"]].get(location_data["location"]) != None:
                    popularity[location_data["time"]][location_data["location"]] +=1
                else:
                    popularity[location_data["time"]][location_data["location"]] = 1

    #pprint.pprint(popularity)

    return popularity

def candidate_time_popularity():
    candidates = [] 
    candidates = read_file.read_candidate_file()
    popularity = {}
    popularity = total_time_popularity()
    result = {}
    
    for popularity_time,popularity_value in popularity.items():
        result[popularity_time] = {}
        for single_candidate in candidates:
            if popularity_value.get(single_candidate) != None:
                result[popularity_time][single_candidate] = popularity_value.get(single_candidate)
            else:
                result[popularity_time][single_candidate] = 0

    #pprint.pprint(result)
    candidate_dic = {}
    for result_time,result_values in result.items():
        candidate_dic[result_time] = []
        location_list = []
        candidate_list = []
        for result_location,result_num in result_values.items():
            location_list.append([result_num,result_location])
        location_list.sort(reverse = True)
        for i in range(0,len(location_list)):
            candidate_list.append(location_list[i][1])
        candidate_dic[result_time] = candidate_list

    #pprint.pprint(candidate_dic)    
    return candidate_dic
    
def get_unknown_user():
    user_data = read_file.read_checkins_file("unknown_user")
    user_dic = {}
    for user_id,user_total_location in user_data.items():
        user_time_list = []
        for user_daily_location in user_total_location:
            for user_location in user_daily_location:
                if user_location["location"] == "?":
                    user_time_list.append(user_location["time"])
        user_dic[user_id] = user_time_list
    #pprint.pprint(user_dic)
    return user_dic

def get_unknown_user_time():
    user_data = get_unknown_user()
    user_new_data = {}
    for user_id,user_time in user_data.items():
        user_time_list = []
        for single_time in user_time:
            if single_time == 0:
                user_time_list.append(24)
            else:
                user_time_list.append(single_time)
        user_new_data[user_id] = user_time_list

    user_result = {}
    for user_id,user_time in user_new_data.items():
        most_common,num_most_common = Counter(user_time).most_common(1)[0]
        if num_most_common > 1:
            if most_common == 24:
                user_result[user_id] = 0
            else:
                user_result[user_id] = most_common
        else:
            if max(user_time) - min(user_time) > 3:
                user_result[user_id] = 25
            else:
                user_time.sort()
                middleIndex = int((len(user_time) - 1)/2)
                user_result[user_id] = user_time[middleIndex]

    #pprint.pprint(user_result)
    return user_result

def recommend():
    user_result = get_unknown_user_time()
    result = {}
    candidate_list = candidate_popularity()
    time_candidate = candidate_time_popularity()
    for user_id,user_time in user_result.items():
        if user_time == 25:
            result[user_id] = []
            for candidate in candidate_list:
                result[user_id].append(candidate)
        else:
            result[user_id] = time_candidate[user_time]
    
    #pprint.pprint(result)
    return result

if __name__ == '__main__':
    #total_popularity()
    #candidate_popularity()
    #get_unknown_user()
    #recommend()
    pass