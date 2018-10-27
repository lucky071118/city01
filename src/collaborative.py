#encoding:utf-8
import read_file
import os
import pprint
import numpy as np

def knownUser_unKnownLocation():
	# 3884 known users with 100 unknown location
	# 100 unknown users with 533736 known location
	new_dic={}
	known_user_data = read_file.read_checkins_file("known_user")
	known_user_list=list(known_user_data.keys())
	loc_list=[]
	pprint.pprint("test")

	for keyname, valuename in known_user_data.items():
		for dailyvalue in valuename:
			for eachvalue in dailyvalue:
				eachloc = eachvalue["location"]
				loc_list.append(eachloc)
		new_dic[keyname]=loc_list
	pprint.pprint("test2")
	#pprint.pprint(new_dic)

	pprint.pprint("test3")


	unknown_loc=read_file.read_candidate_file()
	knownUser_unknownLoc=(len(known_user_data),len(unknown_loc)) #(2,3,4)变为3维
	maxtrix_knownUser_unknownLoc = np.zeros(knownUser_unknownLoc)
	#pprint.pprint(np.zeros(knownUser_unknownLoc))

	for username, localist in new_dic.items():
		userindex = known_user_list.index(username)

		for location in localist:
			try:
				locationindex = unknown_loc.index(location)
			except:
				continue
			maxtrix_knownUser_unknownLoc[userindex,locationindex]+=1
		pprint.pprint("test4")
	#pprint.pprint(maxtrix_knownUser_unknownLoc)
	a = np.array([1, 2, 3, 4, 5])
	np.savetxt("b.txt",a)
	np.savetxt("matrix.txt", maxtrix_knownUser_unknownLoc);


def unknownUser_knownLocation():
	# 100 unknown users with 533736 known location
	new_dic={}
	unknown_user_data = read_file.read_checkins_file("unknown_user")
	unknown_user_list=list(unknown_user_data.keys())
	loc_list=[]

	for keyname, valuename in unknown_user_data.items():
		for dailyvalue in valuename:
			for eachvalue in dailyvalue:
				eachloc = eachvalue["location"]
				loc_list.append(eachloc)
		new_dic[keyname]=loc_list

	pprint.pprint(new_dic)


	known_loc=read_file.read_known_location()
	unknownUser_knownLoc=(len(unknown_user_data),len(known_loc)) #(2,3,4)变为3维
	maxtrix_unknownUser_knownLoc = np.zeros(unknownUser_knownLoc)
	#pprint.pprint(np.zeros(unknownUser_knownLoc))

	for username, localist in new_dic.items():
		userindex = unknown_user_list.index(username)
		for location in localist:
			try:
				locationindex = known_loc.index(location)
			except:
				continue
			maxtrix_unknownUser_knownLoc[userindex,locationindex]+=1
	pprint.pprint(maxtrix_unknownUser_knownLoc)
	a = np.array([1, 2, 3, 4, 5])
	np.savetxt("b.txt",a)
	np.savetxt("matrix.txt", maxtrix_unknownUser_knownLoc);

def knownUser_knownLocation():
	# 3884 unknown users with 533736 known location
	new_dic={}
	known_user_data = read_file.read_checkins_file("known_user")
	known_user_list=list(known_user_data.keys())
	pprint.pprint(len(known_user_list))
	loc_list=[]

	for keyname, valuename in known_user_data.items():
		for dailyvalue in valuename:
			for eachvalue in dailyvalue:
				eachloc = eachvalue["location"]
				loc_list.append(eachloc)
		new_dic[keyname]=loc_list

	pprint.pprint(new_dic)

	known_loc=read_file.read_known_location()
	knownUser_knownLoc=(len(known_user_data),len(known_loc)) 
	maxtrix_knownUser_knownLoc = np.zeros(knownUser_knownLoc)
	pprint.pprint(np.zeros(maxtrix_knownUser_knownLoc))

	for username, localist in new_dic.items():
		userindex = known_user_list.index(username)
		for location in localist:
			try:
				locationindex = known_loc.index(location)
			except:
				continue
			maxtrix_knownUser_knownLoc[userindex,locationindex]+=1
	# pprint.pprint(maxtrix_knownUser_knownLoc)
	
if __name__ == '__main__':
	knownUser_unKnownLocation()
	#unknownUser_knownLocation()
	# knownUser_knownLocation()
