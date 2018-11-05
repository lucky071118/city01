import read_file
import pprint
import home_recommendation

nonvisitor_threshold = 10

def analysis():
    user_data = read_file.read_checkins_file("unknown_user")
    user_dic = {}
    for user_id,total_location in user_data.items():
        user_dic[user_id] = []
        for daily_location in total_location:
            for single_location in daily_location:
                user_dic[user_id].append(single_location["location"])

    home_dic = home_recommendation.get_home_location()
    
    result = {}
    result["home"] = []
    result["visitor"] = []
    result["non_visitor"] = []

    for user_id,user_location in user_dic.items():
        for single_location in user_location:
            for location_id,location_content in home_dic.items():
                if user_id not in result["home"]:
                    if single_location == location_id:
                        result["home"].append(user_id)
    
    for user_id,total_location in user_data.items():
        if user_id not in result["home"]:
            if len(total_location) > nonvisitor_threshold:
                result["non_visitor"].append(user_id)
            else:
                result["visitor"].append(user_id)

    #pprint.pprint(result)
    return result

if __name__ == '__main__':
    analysis()