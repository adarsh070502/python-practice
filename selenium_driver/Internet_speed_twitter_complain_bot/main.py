from internetspeedtwitterbot import InternetSpeedTwitterBot

netspeed = InternetSpeedTwitterBot()
twitter = InternetSpeedTwitterBot()

download_speed = netspeed.net_speed_bot()

if download_speed < 25:
    twitter.twitter_bot(download_speed)





