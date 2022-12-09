"""
Übung_4 Bsp_1
Twitter Übung mit kleinem Jason file
Viktor Olenberg, is221035
"""
import json

class Tweet:

    # so viele Tweets sind vorhanden
    tweet_count = 0

    #defining an object for tweets
    def __init__(self, date, username, message):
        self.username = username
        self.message = message
        self.date = date
        Tweet.tweet_count += 1

    def __str__(self):
        return (f'Date: {self.date}, Username: {self.username}, Message: {self.message}')



try:
    with open('twitter_small.json', encoding='utf-8' ) as f:
        tweets_object = json.load(f)
except FileNotFoundError:
    print(f'ERROR: No such file or directory: {f}')
    #sys.exit(1)

# Test output of the dictonary that has the tweet data of the file
#print(tweets_object)

usernames = ''
date = ''
message = ''


#tweet_stack_dic = {}

# hashtag collection
hashtags = {}
hashZ = 1

# counter of the tweets
zTwe = 0
a = 0

# variable for all users
allusers = {}

date_full_stack = {}

# copying the file information into an Tweet class object
z = 0
for c in range(0, 40000):
    for i in tweets_object.values():

        # filtering the username
        username = i[z]['user']
        username = username.replace('http://twitter.com/', '')

        # checks if the user already tweated if yes ads amount if no adds user to dic
        if username in allusers:
            allusers[username] += 1
        else:
            allusers[username] = 1

        # filtering the date only
        date_full = i[z]['time'][0:10]

        if date_full in date_full_stack:
            date_full_stack[date_full] += 1
        else:
            date_full_stack[date_full] = 1



        date = date_full.replace('2009-06-11 ', '')

        # saving the message
        message = i[z]['message']
        #counting valid messages
        if message != '' and message != ' ':
            zTwe += 1
        else:
            pass

        #checking for hashes in the current message
        if '#' in message:

            #splitting the message and lowercase all what was found
            message1 = message # copying file to not edit original one
            message1 = message1.lower()
            message1 = message1.split()
            t = len(message1)


            # sorting out only the hashes
            for l in range(0,t-1):
                if '#' in message1[l]:

                    # checks if the hashtag is already found and counts or adds it
                    if message1[l] in hashtags:
                        hashtags[message1[l]] += 1
                        a += 1
                    else:
                        hashtags[message1[l]] = 1
                else:
                    pass




        #print(date, '\t', username, '\t\t', message)
        z += 1

        # writing the filtered data into a Tweet object
        tweet_stack = Tweet(date, username, message)

    # output the Tweet object
    print(tweet_stack)


def top_user(allusers):

    h1 = ''
    h2 = ''
    h3 = ''
    h4 = ''
    h5 = ''
    n = 0

    allusers_backup = allusers.copy()

    # finding the 5 most active users
    for i in allusers.keys():
        if allusers[i] > n:
            h1 = i
            n = allusers[i]
        else:
            pass

    del allusers[h1]
    n = 0
    for i in allusers.keys():
        if allusers[i] > n:
            h2 = i
            n = allusers[i]
        else:
            pass

    del allusers[h2]
    n = 0
    for i in allusers.keys():
        if allusers[i] > n:
            h3 = i
            n = allusers[i]
        else:
            pass

    del allusers[h3]
    n = 0
    for i in allusers.keys():
        if allusers[i] > n:
            h4 = i
            n = allusers[i]
        else:
            pass

    del allusers[h4]
    n = 0
    for i in allusers.keys():
        if allusers[i] > n:
            h5 = i
            n = allusers[i]
        else:
            pass



    # 5 most used hashtags
    print('The top five users:')
    print(f'1: {h1} = {allusers_backup[h1]}   2: {h2} = {allusers_backup[h2]}   3: {h3} = {allusers_backup[h3]}   4: {h4} = {allusers_backup[h4]}   5: {h5} = {allusers_backup[h5]}\n')


# finding the 5 mostly used hastags
def hashFinder(hashtags):
    # counter for the most used hashes
    h1 = ''
    h2 = ''
    h3 = ''
    h4 = ''
    h5 = ''
    n = 0

    # in the searching process hastags will be loosing items
    hashtags_backup = hashtags.copy()

    # finding the 5 most used hashtags
    for i in hashtags.keys():
        if hashtags[i] > n:
            h1 = i
            n = hashtags[i]
        else:
            pass

    del hashtags[h1]
    n = 0
    for i in hashtags.keys():
        if hashtags[i] > n:
            h2 = i
            n = hashtags[i]
        else:
            pass

    del hashtags[h2]
    n = 0
    for i in hashtags.keys():
        if hashtags[i] > n:
            h3 = i
            n = hashtags[i]
        else:
            pass

    del hashtags[h3]
    n = 0
    for i in hashtags.keys():
        if hashtags[i] > n:
            h4 = i
            n = hashtags[i]
        else:
            pass

    del hashtags[h4]
    n = 0
    for i in hashtags.keys():
        if hashtags[i] > n:
            h5 = i
            n = hashtags[i]
        else:
            pass

    # 5 most used hashtags
    print('The five mostly used hashtags:')
    print(f'1: {h1} = {hashtags_backup[h1]}   2: {h2} = {hashtags_backup[h2]}   3: {h3} = {hashtags_backup[h3]}   4: {h4} = {hashtags_backup[h4]}   5: {h5} = {hashtags_backup[h5]}\n')


def tweet_count(zTwe,a):
    # counting how many tweets and hashtags
    print(f'Tweets: {zTwe} \nHashtags: {a}')

def hashTagsAll(hashtags):
    a = 0
    #amount of the hashtags
    for i in hashtags:
        a += 1

    #hashtags output
    for k in hashtags.keys():
        print(f'Hashtag: {k} \n Usage: {hashtags[k]} \n\n')

#shows the top tweet day
def top_tweet_day(date_full_stack):

    #print(date_full_stack)

    h1 = ''
    n = 0

    for i in date_full_stack.keys():
        if date_full_stack[i] > n:
            h1 = i
            n = date_full_stack[i]

    # output of result date
    print('The date with the most active tweets:')
    print(f'Date: {h1}    Tweets on that day: {date_full_stack[h1]}')



# main menu start
inp = 'B'

while inp != 'exit':

    print('- 1 (tweet_count)')
    print('- 2 (top_hashtags)')
    print('- 3 (top_user)')
    print('- 4 (top_tweet_day)')
    print('- 5 (top_hashtag_user)')
    print('- 6 (all_hashtags)')
    #print('- 7 (all_data_filtered)')
    inp = input('Your Input: ')

    if inp == '1':
        # counting how many tweets and hashtags
        tweet_count(zTwe,a)
    elif inp == '2':
        # output of the top 5 hashtags
        hashFinder(hashtags)
    elif inp == '3':
        # output of the top 5 users
        top_user(allusers)
    elif inp == '4':
        # day with the most tweets
        top_tweet_day(date_full_stack)
    elif inp == '5':
        print('Not available yet.')
    elif inp == '6':
        hashTagsAll(hashtags)
    elif inp == '7':
        print('Not available yet.')
    elif inp == 'exit':
        break
    else:
        print('Your Input was wrong.')




#print(tweet_stack_dic)

