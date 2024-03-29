# -*- coding: utf-8 -*-
"""
Created on Thu May 17 17:13:16 2012
STATISTICS and user taxonomy
@author: YINGZHENLI KDD@SYSU
"""
import cPickle
import IMPORT
from new_statistics import *

DATA = IMPORT.IMPORT(['user_profile', 'rec_log_train', 'user_key_word', 
                      'user_sns'])

userIDList = DATA['user_profile'].keys()
result = sta_tweet_and_user(userIDList, DATA['user_profile'])
PDF = percentage(result)
divide = {}
for percentage in range(1,101):
    temp = DivideLine(PDF, float(percentage) * 0.01)
    divide[percentage] = temp

user_Class = dict()
for userID in userIDList:
    tweet = get_tweet_number(userID, DATA['user_profile'])
    if tweet == 0:
	user_Class[userID] = -1
    else:
	for ii in range(1, 101):
	    if divide[ii] > tweet:
		user_Class[userID] = ii - 1
		break
print user_Class
f = open('data_user_class', 'w')
f.write(cPickle.dumps(user_Class))
f.close()

f = open('data_percentage', 'w')
f.write(cPickle.dumps(divide))
f.close()

# write user class in data_user_class
