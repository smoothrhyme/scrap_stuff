import tweepy
import pandas as pd
import numpy as np
from tweepy import OAuthHandler

# The consumer key and secret will be generated for you after
consumer_key="Uu25IPRoImSYocGL2nxW08koA"
consumer_secret="KpZrbRBeAU6O8AIvSRnjeIEmYpU6vqdBUEKAgAnABqIUEsdEY7"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="830935517361532932-CjSOJKdcQVpPDlfJp1Y4JsDTh1UYR8t"
access_token_secret="hxOHKJeC8Jm95btbHBOrVABwnFpW6fRmJLe3CU6qKmyEn"

#seta as credenciais de acesso pela API
def cred_twitt():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

cred = cred_twitt()

##EX: Extrair info sobre um subject numa lingua especifica
## com o objeto 'extract' é possível fazer uma busca e tweets random
## sobre o subject q{aqui "eminem"} na linguagem que desejar.
#for tweet in Cursor(api.search, q="eminem", lang="pt-br").items():
#    print (tweet.text)

#EX2:
#A função user_timeline do objeto com credenciais "cred" permite extrair Tweets
# de um perfil específico  com N tweets.
def extract_tweets(cred=cred,username=None,number_of_tweets=100):
    tweets = cred.user_timeline(screen_name=username, count=number_of_tweets,
                                tweet_mode='extended')

    df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns =['Tweets'])
    df['Tweet_Length']  = np.array([len(tweet.full_text) for tweet in tweets])
    df['ID']   = np.array([tweet.id for tweet in tweets])
    df['Date_Posted'] = np.array([tweet.created_at for tweet in tweets])
    df['OS'] = np.array([tweet.source for tweet in tweets])
    df['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    df['Retweets']    = np.array([tweet.retweet_count for tweet in tweets])
    df['weekday_name']  = gean['Date_Posted'].dt.weekday_name
    df['weekday_day'] =gean['Date_Posted'].dt.weekday
    df['Month'] =gean['Date_Posted'].dt.month

    return df
