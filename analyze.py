import csv
from collections import OrderedDict
# import time
people = ["Hilary", "Obama", "Trump", "Pence", "Putin", "Peloski", "Paul Ryan", "Bernie Sanders", "Barack Obama"]
groups = ["BLM", "Black Lives Matter", "Republicans", "Democrats", "GOP", "KKK"]
ideology = ["Liberal", "Conservative", "Progressive", "Nazi", "Facism", "Totalitarianism", "Nationalism"]
places = ["America", "USA" "Europe", "UK", "Russia", "Britain", "England"]
topics = ["American", "Anti American", "Anti-American", "guns", "gun control", "abortion"]
terrorism = ["terrorists", "killing", "bombing", "ISIS"]
insults = ["snowflake"]
religion = ["Muslim", "Islam", "Christian", "God", "prayer", "Allah", "Lord"]

keywords = people + groups + ideology + topics + places + terrorism + insults + religion

with open('tweets.csv', 'r') as tweets_csv:
  reader = csv.reader(tweets_csv)
  tweets_aslist = list(reader)

field_names = tweets_aslist.pop(0)
tweets_asdict = []
for tweet in tweets_aslist:
    tweets_asdict.append(OrderedDict(zip(field_names, tweet)))

heatmap = {}
for kw in keywords:
    heatmap[kw] = 0
unique_dates = 0
high_range = 0
for tweet in tweets_asdict:
    date = tweet['created_str'][:10]
    if not heatmap.get(date):
        unique_dates = unique_dates +1
        heatmap[date] = { "total": 0}
        for kw in keywords:
            heatmap[date][kw] = 0

    for kw in keywords:
        if kw.lower() in tweet['text'].lower():
            heatmap[date]["total"] = heatmap[date]["total"] + 1
            heatmap[kw] = heatmap[kw] + 1
            heatmap[date][kw] = heatmap[date][kw] + 1
            if heatmap[date][kw] > high_range:
                high_range = heatmap[date][kw]

# print(heatmap)
for item in heatmap:
    if item in keywords:
        print(item, heatmap[item])
print("Unique Dates:", unique_dates)
print("Highest Range:", high_range)

# column_names = "user_id","user_key","created_at","created_str","retweet_count","retweeted","favorite_count","text","tweet_id","source","hashtags","expanded_urls","posted","mentions","retweeted_status_id","in_reply_to_status_id"
