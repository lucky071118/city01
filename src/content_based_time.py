import read_file
import pprint
import json
import popularity_recommendation
import popularity_time

def get_person_location_type():
    user_data = read_file.read_checkins_file("unknown_user")
    location_data = read_file.read_location_file()
    user_location_dic = {}
    for user_id,user_location in user_data.items():
        user_location_dic[user_id] = []
        for daily_location in user_location:
            for location in daily_location:
                if location["location"] != "?":
                    location_type = location_data[location["location"]]["type"]
                    if "\x1a\x1a" in location_type:
                        location_type = "Café"
                    user_location_dic[user_id].append(location_type)

    for user_id,user_location_type in user_location_dic.items():
        user_location_dic[user_id] = {}
        for single_location_type in user_location_type:
            user_location_dic[user_id][single_location_type] = user_location_type.count(single_location_type)

    #pprint.pprint(user_location_dic)
    return user_location_dic

def load_category():
    with open('crawler/category.json','r',encoding = "utf-8") as f:
        data = json.load(f)
    #pprint.pprint(data)
    return data
def get_candidate_category():
    candidate_data = read_file.read_candidate_file()
    location_data = read_file.read_location_file()
    candidate_category_dic = {}
    for single_candidate in candidate_data:
        for location_key, location_value in location_data.items():
            if single_candidate == location_key:
                candidate_category_dic[single_candidate] = location_value["type"]

    category_data = load_category()
    result_dic = {}
    for candidate_key,candidate_value in candidate_category_dic.items():
        for high_category in category_data["response"]["categories"]:
            for mid_category in high_category["categories"]:
                if candidate_value == mid_category["name"]:
                    result_dic[candidate_key] = {} 
                    result_dic[candidate_key]["category"] = high_category["name"]
                if mid_category["categories"] != []:
                    for low_category in mid_category["categories"]:
                        if candidate_value == low_category["name"]:
                            result_dic[candidate_key] = {}
                            result_dic[candidate_key]["category"] = mid_category["name"]
                        if low_category["categories"] != []:
                            for last_category in low_category["categories"]:
                                if candidate_value == last_category["name"]:
                                    result_dic[candidate_key] = {}
                                    result_dic[candidate_key]["category"] = low_category["name"]
    
    candidate_popularity_list = popularity_recommendation.candidate_popularity()
    for single_result_key,single_result_value in result_dic.items():
        count = 0
        for candidate_popularity in candidate_popularity_list:
            count += 1
            if single_result_key == candidate_popularity:
                result_dic[single_result_key]["popularity"] = count

    #pprint.pprint(result_dic)
    return result_dic

def user_location_category():
    user_location_category = {}
    category_data = load_category()
    user_location = get_person_location_type()
    for user_id,single_user_location in user_location.items():
        user_location_category[user_id] = {}
        for location_type,location_num in single_user_location.items():
            for high_category in category_data["response"]["categories"]:
                if high_category["categories"] != []:
                    for mid_category in high_category["categories"]:
                        if location_type == mid_category["name"]:
                            if high_category["name"] in user_location_category[user_id]:
                                user_location_category[user_id][high_category["name"]]["total"] += location_num
                            else:
                                user_location_category[user_id][high_category["name"]] = {}
                                user_location_category[user_id][high_category["name"]]["total"] = location_num
                        if mid_category["categories"] != []:
                            for low_category in mid_category["categories"]:
                                if location_type == low_category["name"]:
                                    if high_category["name"] in user_location_category[user_id]:
                                        user_location_category[user_id][high_category["name"]]["total"] += location_num
                                    else:
                                        user_location_category[user_id][high_category["name"]] = {}
                                        user_location_category[user_id][high_category["name"]]["total"] = location_num
        
                                    if mid_category["name"] in user_location_category[user_id][high_category["name"]]:
                                        user_location_category[user_id][high_category["name"]][mid_category["name"]]["total"] += location_num
                                    else:
                                        user_location_category[user_id][high_category["name"]][mid_category["name"]] = {}
                                        user_location_category[user_id][high_category["name"]][mid_category["name"]]["total"] = location_num
                                if low_category["categories"] != []:
                                    for last_category in low_category["categories"]:
                                        if location_type == last_category["name"]:
                                            if high_category["name"] in user_location_category[user_id]:
                                                user_location_category[user_id][high_category["name"]]["total"] += location_num
                                            else:
                                                user_location_category[user_id][high_category["name"]] = {}
                                                user_location_category[user_id][high_category["name"]]["total"] = location_num
                
                                            if mid_category["name"] in user_location_category[user_id][high_category["name"]]:
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]]["total"] += location_num
                                            else:
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]] = {}
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]]["total"] = location_num
                                            
                                            if low_category["name"] in user_location_category[user_id][high_category["name"]][mid_category["name"]]:
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]][low_category["name"]]["total"] += location_num
                                            else:
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]][low_category["name"]] = {}
                                                user_location_category[user_id][high_category["name"]][mid_category["name"]][low_category["name"]]["total"] = location_num
                                            
                
    #pprint.pprint(user_location_category)
    return user_location_category
    
def get_user_like_category():
    total_dic = {}
    user_location_dic = user_location_category()
    for location_dic_key,location_dic_value in user_location_dic.items():
        total_list = []
        high_temp_list = [] 
        for high_location_key,high_location_value in location_dic_value.items(): 
            high_temp_list.append([high_location_value["total"],high_location_key])
        high_temp_list.sort(reverse = True)
        high_list = []
        
        for i in range(0,len(high_temp_list)):
            high_list.append(high_temp_list[i][1])
        
        for high_key in high_list:
            mid_temp_list = []
            for mid_location_key,mid_location_value in location_dic_value[high_key].items():
                if mid_location_key != "total":
                    mid_temp_list.append([mid_location_value["total"],mid_location_key])
            mid_list = []
            for i in range(0,len(mid_temp_list)):
                mid_list.append(mid_temp_list[i][1])
            for mid_key in mid_list:
                low_temp_list = []
                for low_location_key,low_location_value in location_dic_value[high_key][mid_key].items():
                    if low_location_key != "total":
                        low_temp_list.append([low_location_value["total"],low_location_key])
                    low_temp_list.sort(reverse = True)

                for i in range(0,len(low_temp_list)):
                    total_list.append(low_temp_list[i][1])
                total_list.append(mid_key)
            total_list.append(high_key)
        total_dic[location_dic_key] = total_list

    return total_dic

def recommend():
    user_like_category = get_user_like_category()
    candidate_data = get_candidate_category()
    user_time_data = popularity_time.get_unknown_user_time()
    time_popularity_data = popularity_time.candidate_time_popularity()
    result_dic = {}
    for single_user_category_key,single_user_category_value in user_like_category.items():
        result_list = []
        for single_category in single_user_category_value:
            temp_category_list = []
            popularity_list = []
            category_list = []
            for single_candidate_key,single_candidate_value in candidate_data.items():
                if single_candidate_value["category"] == single_category:
                    temp_category_list.append(single_candidate_key)
            user_time = user_time_data[single_user_category_key]
            if user_time == 25:
                for single_temp in temp_category_list:
                    popularity_list.append([candidate_data[single_temp]["popularity"],single_temp])
                popularity_list.sort()

                for i in range(0,len(popularity_list)):
                    category_list.append(popularity_list[i][1])
                for single_category_result in category_list:
                    result_list.append(single_category_result)
            else:
                time_popularity_list = time_popularity_data[user_time]
                for single_time_popularity in time_popularity_list:
                    for single_temp_category in temp_category_list:
                        if single_time_popularity == single_temp_category:
                            result_list.append(single_temp_category)

        result_dic[single_user_category_key] = result_list

        remain_popularity_list = []
        for candidate_key,candidate_value in candidate_data.items():
            if candidate_key not in result_dic[single_user_category_key]:
                remain_popularity_list.append([candidate_value["popularity"],candidate_key])
        remain_popularity_list.sort()

        for i in range(0,len(remain_popularity_list)):
            result_dic[single_user_category_key].append(remain_popularity_list[i][1])        

    
    return result_dic

if __name__ == '__main__':
    #a = get_person_location_type()
    #b = user_location_category()
    #c = get_user_like_category()
    #get_candidate_category()
    d = recommend()
    pprint.pprint(d["99008"])
    #pprint.pprint(d["9448"])
    pass
    