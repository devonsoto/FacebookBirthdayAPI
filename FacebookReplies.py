#Author: Devon Soto
#Description: To comment and like happy birthday facebook posts on your wall

#TODO: Can use a limit to stay under certain post
#TODO: Keep in mind pagination
#TODO: Possibly do a timestamp page pagination
#TODO: Add function that actually posts a thank you or something
#TODO: Add comment to post on fb


import requests
import datetime
import random
from pprint import pprint

#get user api key from facebook developers webstie
api_key = "Your key here"

#Birthday must be in this format since this is how the created_time is on json
birthday = "2017-03-15"

#list of key words.
birthday_words = ["Happy", "happy", "birthday", "bday", "feliz", "cumpleaños", "cumpleanos", "great day", "good day"]
basic_words = ["hey", "family", "added", "president", "remember"]
message_reply = ["Thank you :)", "Thanks buddy, I appreciate it!", "Thanks haha. :)", "Thank you :)", "Thanks hope to see you soon haha", "Aww Thanks buddy"]

#number of birthday post
num_post = 0
birthday_post = []
getFeeds = True



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
    print("This is the time: {}".format(time))
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
    #print("This is the paging ----- {} \n".format(post['paging']['next']))
    #pprint((requests.get(post['paging']['next'])).json())
    for post in post['data']:


        print(post['created_time'])
        if(get_date(post,birthday) and has_keyword(post)):
            num_post += 1
            print(post['message'])
            birthday_post.append(post['id'])





    return birthday_post

def reply_to_post(posts):
    for post in posts:
        post_url = 'https://graph.facebook.com/%s/comments' % post['post_id']
        random_num = random.randint(a, len(message_reply))
        post_message = message_reply(random_num)
        parameters = {'access_token': api_key, 'message': post_message}
        post = requests.post(post_url, data = parameters )


#Get user feed data
request_url = "https://graph.facebook.com/me/feed?access_token=" + api_key + "&limit=3"
r = requests.get(request_url)
data = r.json()


#running code and printing out which post
pprint(data)
birthday_post = bday_post_list(data,birthday)
print(birthday_post)
