import tweepy

def main():
    API_key = 'pbjlYX8YI8IV9PdEQ4sg4eF3x'
    API_secret_key = 'nm3vnqFv0E9e91p3c8ZVfVVmxnRrJd9MGxnQiKWTNMXgxnErR1'
    token = '1261448913996992515-ZQYLXsliyCxhKxLEY4UaBBUWYfEuLA'
    token_secret = '8oUQqhBUtflLFu0eKM5QB1hk2F32tXYMRyLYHZOemUkZ5'

    tweeper = Tweeper(API_key, API_secret_key, token, token_secret)
    tweeper.printUser()

class Tweeper:
    def __init__(self, API_key, API_secret, token, token_secret):
        auth = tweepy.OAuthHandler(API_key, API_secret)
        auth.set_access_token(token, token_secret)
        
        self.api = tweepy.API(auth)
        self.user = self.api.get_user("twitter")

    def printUser(self):
        print(self.user.followers_count)


if(__name__ == "__main__"):
    main()

