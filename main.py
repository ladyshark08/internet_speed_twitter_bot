from Speed import InternetSpeedTwitter

PROMISED_DOWN = 1500
PROMISED_UP = 200
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

speed = InternetSpeedTwitter(PROMISED_DOWN, PROMISED_UP)
result = speed.get_internet_speed()
if result is not None:
    speed.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, result)
