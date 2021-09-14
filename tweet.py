import pandas as pd
import tweepy


def _get_api():
    df_key = pd.read_json("key.json")

    # 認証に必要なキーとトークン
    API_KEY = df_key.loc[0, "API Key"]
    API_SECRET = df_key.loc[0, "API Key Secret"]
    ACCESS_TOKEN = df_key.loc[0, "Access Token"]
    ACCESS_TOKEN_SECRET = df_key.loc[0, "Access Token Secret"]

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api


def main():
    api = _get_api()

    # キーワードからツイートを取得
    tweets = api.search(q=["Python"], count=10)

    for tweet in tweets:
        print("-----------------")
        print(tweet.text)

    public_tweets = api.home_timeline()
    # つぶやく
    api.update_status("test1")
    api.update_with_media(
        status="test_media", filename="スクリーンショット 2021-09-14 192825.png"
    )

    return


if __name__ == "__main__":
    main()
