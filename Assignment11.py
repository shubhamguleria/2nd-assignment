#Question1
'''
An access token is an object that describes the security context of a process or thread.


Consumer API keys
A2aI3gc3Ei06Gz1lPkVunmy1w (API key)
H7Ntlev4ME5UaXwxHFY6Vv1uZbmsaVpLRBIrseenbdrvDPmNB0 (API secret key)

Access token & access token secret
1032139265172561920-7sr7HxFEeYrJwvw2lsi70iTSCHtFGQ (Access token)
jxBvSiHBCq4BRJIKAaxMOmOSa4pjD4Ghy7OXfMZOjP5qe (Access token secret)
Read and write (Access level)

'''
#Question2
'''
import socket
print(socket.gethostbyname('google.com'))
'''
#Question3
'''
import tweepy
consumer_key="A2aI3gc3Ei06Gz1lPkVunmy1w"
consumer_secret_key="H7Ntlev4ME5UaXwxHFY6Vv1uZbmsaVpLRBIrseenbdrvDPmNB0"
access_key="1032139265172561920-7sr7HxFEeYrJwvw2lsi70iTSCHtFGQ"
access_secret_key="jxBvSiHBCq4BRJIKAaxMOmOSa4pjD4Ghy7OXfMZOjP5qe"
def get_tweets(username):
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_key, access_secret_key)
    api=tweepy.API(auth)
    num_of_tweets=20
    tweets=api.user_timeline(screen_name=username)
    tmp=[]
    tweets_for_csv=[tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    print(tmp)
if __name__=='__main__':
    get_tweets("twitter-handle")
'''
#Question4
'''
 A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects.

An API is an interface for other programs to interact with your program or library  without having direct access.
'''
#Question5: Sending mail using sendgrid.? Instead of spotify.
'''
import sendgrid
import os
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email("My Email: ")
to_email = Email("Reciever's email: ")
subject = "Assignment for AcadView."
content = Content("Completed my assignment.", "You will get it on github link. ")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

'''
