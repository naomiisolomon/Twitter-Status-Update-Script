#Script by Naomi Solomon
#This program allows you to send tweets via python using the twitter API and tweepy

import tweepy

APIKey = "Enter your API Key here"
APISecretKey = "Enter your API Secret Key here"
AccessToken = "Enter your Access Token here"
AccessTokenSecret = "Enter your Access Token Secret here"

#validates the API keys before moving forward.
authenticate = tweepy.OAuthHandler(APIKey, APISecretKey)
#access twitter after being validated. needs to be in this order
authenticate.set_access_token(AccessToken, AccessTokenSecret)

#accessing the API after checking if access token and apikey is correct. security measure.
twitterAPI = tweepy.API(authenticate)


mytweet = " tweeting via visual studio "
twitterAPI.update_status(status = (mytweet)) #update_status is a twitter object not tweepy. status is also twitter API 
print ("sent")
