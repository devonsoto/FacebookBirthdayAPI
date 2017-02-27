#Author: Devon Soto
#Description: To comment and like happy birthday facebook posts on your wall

#TODO: Can use a limit to stay under certain post
#TODO: Keep in mind pagination
#TODO: Possibly do a timestamp page pagination
#TODO: Add function that actually posts a thank you or something
#TODO: Add comment to post on fb


import requests
import datetime
from pprint import pprint

#get user api key from facebook developers webstie
api_key = "EAAE47dSjxosBAD6tqACdZA2MptQe7B5Kp3ZCZBwITHcdYIAuinb4m7R7agSIkVNoZAvOHhkAZBrEmfeZBKqX6HiJYb4QbzoQD7FUE8FLOL62lLvJev9sxCzFfVGPJKEiDHtCJpuTQOybqqxYmeZCAKS8Tq1XJGoU4sbHrQLdKyLvefOtkUql3DWKENlutnnH0sZD"

#Birthday must be in this format since this is how the created_time is on json
birthday = "2016-03-15"

#list of key words.
birthday_words = ["Happy", "happy", "birthday", "bday", "feliz", "cumpleaños", "cumpleanos", "great day", "good day"]
basic_words = ["hey", "family", "added", "president", "remember"]



#This gets the users information(name and id).
'''
request_url = "https://graph.facebook.com/me?access_token=" + api_key
r = requests.get(request_url)
data = r.json()
pprint(data)
'''


#Function that returns true if the post are on the same day
#has to give data['feed']['data'][n] to work
def get_date(post, birthday):
    time = post['created_time']
    time = time[:10]
    if(birthday == time[:10]):
        return True

    return False

#function to see if the post contains a birthday key word
#has to give data['feed']['data'][n]
def has_keyword(post):
    try:
        message = post['message']
        message = message.split(' ')
        i = 0
        for word in birthday_words:
            if(message[i] == word):
                return True
            i+=1
        return False
    except KeyError:
        return True

def bday_post_list(post,birthday):
    birthday_post = []
    for post in post['data']:
        if(get_date(post,birthday) and has_keyword(post)):
            birthday_post.append(post['id'])

    return birthday_post


#Get user feed data
request_url = "https://graph.facebook.com/me/feed?access_token=" + api_key
r = requests.get(request_url)
data = r.json()

#running code and printing out which post
birthday_post = bday_post_list(data,birthday)
print(birthday_post)
