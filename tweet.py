import pandas as pd
import tweepy


def main():
    df_key = pd.read_json("key.json")

    # 認証に必要なキーとトークン
    API_KEY = df_key.loc[0, "API Key"]
    API_SECRET = df_key.loc[0, "API Key Secret"]
    ACCESS_TOKEN = df_key.loc[0, "Access Token"]
    ACCESS_TOKEN_SECRET = df_key.loc[0, "Access Token Secret"]

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # キーワードからツイートを取得
    api = tweepy.API(auth)
    tweets = api.search(q=["Python"], count=10)

    for tweet in tweets:
        print("-----------------")
        print(tweet.text)
    return


if __name__ == "__main__":
    main()
