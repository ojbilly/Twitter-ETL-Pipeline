import tweepy
import pandas as pd
from datetime import datetime
import s3fs
import os


def run_twitter_etl():
    # Load Twitter API credentials from environment variable
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        raise ValueError(
            "Bearer token not found. Please set the TWITTER_BEARER_TOKEN environment variable.")

    # Initialize Tweepy client
    client = tweepy.Client(bearer_token=bearer_token)

    # Specify the Twitter username (exclude the '@' symbol)
    username = "elonmusk"

    # Get user ID from username
    user = client.get_user(username=username)
    user_id = user.data.id

    # Fetch the latest tweets from the user
    response = client.get_users_tweets(
        id=user_id,
        max_results=10,
        tweet_fields=["created_at", "public_metrics", "text"]
    )

    tweets = response.data
    tweet_list = []

    if tweets:
        for tweet in tweets:
            metrics = tweet.public_metrics
            refined = {
                "user": username,
                "text": tweet.text,
                "favorite_count": metrics["like_count"],
                "retweet_count": metrics["retweet_count"],
                "created_at": tweet.created_at
            }
            tweet_list.append(refined)

    # Convert to DataFrame and save to S3
    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://twitter_ozigi_pipeline/refined_tweets.csv", index=False)

    print("Tweets extracted successfully.")
    print(df.head())


# For testing locally, you can uncomment this line
# run_twitter_etl()
# Note: Ensure you have the required packages installed:
# pip install tweepy pandas s3fs
