#encoding:utf-8
import read_file
import os
import pprint
import numpy as np

def recommend():
	# 3884 known users with 100 unknown location
	new_dic={}
	unknown_dic = {}
	known_user_data = read_file.read_checkins_file("known_user")
	pprint.pprint("test")
	unknown_user_data = read_file.read_checkins_file("unknown_user")
	for keyname, valuename in known_user_data.items():
		loc_list=[]
		for dailyvalue in valuename:
			for eachvalue in dailyvalue:
				eachloc = eachvalue["location"]
				loc_list.append(eachloc)
		new_dic[keyname]=loc_list
	
	#pprint.pprint(new_dic)

	for keyname, valuename in unknown_user_data.items():
		loc_list=[]
		for dailyvalue in valuename:
			for eachvalue in dailyvalue:
				eachloc = eachvalue["location"]
				loc_list.append(eachloc)
		unknown_dic[keyname]=loc_list
	

	knn_rank_dic={}

	for cur_userid, cur_loclist in unknown_dic.items():
		rank_user_sim={}
		for next_userid, next_loclist in new_dic.items():
			count =0 
			for eachLoc in cur_loclist:
				for com_Loc in next_loclist:
					if(eachLoc==com_Loc):

						count+=1
			rank_user_sim[next_userid]=count
			#pprint.pprint(len(rank_user_sim))
		rank_list=[]
		for rankUser, rankValue in rank_user_sim.items():
			rank_list.append([rankValue,rankUser])
		rank_list.sort(reverse=True)
		knn_list=[]
		for time in range(0,5):
			knn_list.append(rank_list[time][1])
		knn_rank_dic[cur_userid]=knn_list
	#pprint.pprint(knn_rank_dic)    

	candidate_data = read_file.read_candidate_file()
	candidate_dic = {}
	
		
	for user_id,user_candidate in knn_rank_dic.items():
		candidate_dic[user_id] = {}
		for candidate in candidate_data:
			count = 0
			for user_data in user_candidate:
				for user_location in new_dic[user_data]:
					if candidate == user_location:
						count += 1
			candidate_dic[user_id][candidate] = count

	result = {}
	for user_id,user_candidate in candidate_dic.items():
		candidate_rank_list = []
		result_list = []
		for candidate_id,candidate_value in user_candidate.items():
			candidate_rank_list.append([candidate_value,candidate_id])
		candidate_rank_list.sort(reverse = True)
		for i in range(0, len(candidate_rank_list)):
			result_list.append(candidate_rank_list[i][1])
		result[user_id] = result_list
		
	pprint.pprint(result["95132"])
	return result


	
if __name__ == '__main__':
	recommend()
	#unknownUser_knownLocation()
	# knownUser_knownLocation()