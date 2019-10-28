import feedparser
import re
import requests
import json
import os

#Global Var
#slack_url = "slackのWebHookURL"
#search = "探したいアニメのタイトル" e.g."鬼頭明里のsmiley pop,まちカドまぞく,鬼滅の刃"
#syoboiurl = "http://cal.syoboi.jp/rss2.php?usr=***ここにしょぼいカレンダーのID***&titlefmt=$(StTime)%20[$(ChName)]%20$(Mark)%20$(Title)%20$(SubTitleB)"

def lambda_handler(event, context):
    searchs = '|' .join(os.environ['search'].split(','))
    print(searchs)
    feed = feedparser.parse(os.environ['syoboiurl'])
    message = ""
    for entrie in feed['entries']:
        if re.search(searchs,entrie['title']):
            message += entrie['title'] + "\n"
    payload = { "text" : message }
    data = json.dumps(payload)
    requests.post(os.environ['slack_url'], data)
    return message