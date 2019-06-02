from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

handle = input('Nome da conta do twitter: ')
ctr = int(input('quantidade de tweets: '))
res=requests.get('https://twitter.com/'+ handle)
bs=BeautifulSoup(res.text,'html.parser')
all_tweets = bs.find_all('#timeline li.stream-item')

timeline = bs.select('#timeline li.stream-item')

temp = pd.DataFrame(columns = ["id",'tweet','horário do tweet',"data do tweet"])
for k,tweet in enumerate(timeline):
    info_data = tweet.select('a.js-tooltip')[0]
    #get twitter hora
    tweet_hora = re.search(r'[0-9][0-9]:[0-9][0-9]*[0-9]',str(info_data)).group()
    #get dia/mes/ano
    tweet_mesano = re.search(r'[0-9]+ de [a-z]+ de [0-9]{4}',str(info_data)).group()
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()

    temp.set_value(value=tweet_id,col='id',index=k)
    temp.set_value(value=tweet_text,col='tweet',index=k)
    temp.set_value(value=tweet_hora,col='horário do tweet',index=k)
    temp.set_value(value=tweet_mesano,col='data do tweet',index=k)
