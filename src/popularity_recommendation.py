import read_file
import pprint

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
    
def recommend():
    user_data = read_file.read_checkins_file("unknown_user")
    user_list = user_data.keys()
    candidate_list = candidate_popularity()
    result = {}
    for user in user_list:
        result[user] = []
        for candidate in candidate_list:
            result[user].append(candidate)
    #pprint.pprint(result)
    return result

if __name__ == '__main__':
    #recommend()
    pass