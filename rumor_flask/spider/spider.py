from twitter_scrapy import trending, scrape_keyword_with_api
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote
from database.utils import insert_tweet

trending_json_dir = "trending_json/"


def is_English(item):
    return all(ord(c) < 128 for c in item)


def get_trending_tweets() -> list:
    """
    Make a Scrapy Requst to Twitter , both Store the Results in Mysql and Json.
    :param: None    :return: A List of Tweets on Trending.
    """

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"trending_{timestamp}"
    trending_things = trending.get_trendings(proxy='127.0.0.1:7890', filename=trending_json_dir + filename)

    # with open('trending_json/' + filename + '.json', 'r') as f:
    #     trending_data = json.load(f)

    trending_keywords_languages = []

    # print(trending_things)
    for trends in trending_things[0]['trends']:
        trending_keywords_languages.append(trends['query'])

    trending_keywords_english = []

    for item in trending_keywords_languages:
        if is_English(unquote(item)):
            trending_keywords_english.append(item)

    result = []

    for keyword in trending_keywords_english:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(scrape_keyword_with_api, query=keyword, tweets_count=10, proxy='127.0.0.1:7890',
                                     output_filename='tweet_' + keyword, output_dir='trending_json')
            try:
                data = future.result(timeout=5)
                if data:
                    result.append(data)
            except TimeoutError:
                print('Time out in scrape the keyword :{}. continue.'.format(keyword))
                continue

    time.sleep(10)
    return result


def tweets_to_mysql(tweets: list) -> bool:
    for tweet_keyword in tweets:
        for record in tweet_keyword:
            images_url = ",".join(record["images_url"])
            print(insert_tweet(keywords=record['keyword'], tweet_text=record["tweet_text"], tweet_id=record["tweet_id"],
                               user_name=record["user_name"], user_id=record["user_id"],
                               user_followers_count=record["user_followers_count"],
                               user_friends_count=record["user_friends_count"], image_url=images_url,
                               create_time=record["create_time"], retweet_count=record["retweet_count"],
                               likes_count=record["likes_count"]))


tweet = get_trending_tweets()
tweets_to_mysql(tweet)