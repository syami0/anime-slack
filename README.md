# anime-slack
今日のアニメの情報をslackに投げるプログラムです

# しくみ
AWS Lambda上で作動し、しょぼいカレンダー(http://cal.syoboi.jp/ )のAPIを利用してその日のアニメ情報を取得、SlackのWebHookよりテキストを投稿します。

# 使い方
環境変数に適切な値を入れる必要があります。
