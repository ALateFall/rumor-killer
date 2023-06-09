#!/usr/bin/env python3

from typing import Union
from .scraping_utilities import Scraping_utilities
import logging
from urllib.parse import quote, unquote
import os
import json

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Keywords_api:
    def __init__(self, query: str, proxy: Union[str, None],
                 tweets_count: int) -> None:
        self.query = query
        self.proxy = proxy
        self.tweets_count = tweets_count
        self.x_guest_key = ''
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.posts_data = {}

    def parse_tweets(self, tweets, users):
        for key in tweets.keys():
            user = users[tweets[key]['user_id_str']]
            tweet = tweets[key]
            self.posts_data[key] = {
                "tweet_url": "https://twitter.com/{}/status/{}".format(user['screen_name'], key),
                "tweet_details": tweet,
                "user_details": user
            }

    def find_cursor(self, timeline):
        cursor = None
        try:
            cursor = timeline["instructions"][-1]["replaceEntry"]["entry"]["content"]["operation"]["cursor"]["value"]
        except KeyError:
            cursor = timeline["instructions"][0]["addEntries"]["entries"][-1]["content"]["operation"]["cursor"]["value"]
        return cursor

    def scrap(self):
        try:
            self.x_guest_key \
                = Scraping_utilities.find_x_guest_token(self.authorization_key, proxy=self.proxy)
            logger.setLevel(logging.INFO)
            headers = Scraping_utilities.build_keyword_headers(
                self.x_guest_key, self.authorization_key, quote(self.query))
            retry = 5
            response = Scraping_utilities.make_http_request(
                'https://api.twitter.com/1.1/search/tweets.json?q=' + self.query,
                headers=headers, proxy=self.proxy)
            my_json = []
            if response:
                for tweet in response['statuses']:
                    my_tweet = {}
                    my_tweet['keyword'] = unquote(self.query)
                    my_tweet['tweet_text'] = tweet['text']
                    my_tweet['tweet_id'] = tweet['id_str']
                    my_tweet['user_name'] = tweet['user']['name']
                    my_tweet['user_id'] = tweet['user']['id_str']
                    my_tweet['user_followers_count'] = tweet['user']['followers_count']
                    my_tweet['user_friends_count'] = tweet['user']['friends_count']
                    images_url = []
                    if 'media' in tweet['entities']:
                        for media in tweet['entities']['media']:
                            images_url.append(media['media_url'])
                    my_tweet['images_url'] = images_url
                    my_tweet['create_time'] = tweet['created_at']
                    my_tweet['retweet_count'] = tweet['retweet_count']
                    my_tweet['likes_count'] = tweet['favorite_count']
                    my_json.append(my_tweet)
                logger.info('Successfully Get Tweets of Query Keywords.')
            elif retry <= 0:
                logger.info("Can't Find more Post")
            else:
                logger.warning('Failed to make request!')
            return my_json
        except Exception as ex:
            logger.warning('Error at scrap : {}'.format(ex))


def scrape_keyword_with_api(query: str, proxy: Union[str, None] = None,
                            tweets_count: int = 10,
                            output_filename: Union[str, None] = None,
                            output_dir: Union[str, None] = os.getcwd()):
    """Function to scrape tweets from Twitter API using provided query.

    Args:
        query (str): query to search.
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        tweets_count (int, optional): Number of Tweets to scrape. Defaults to 10.
        output_filename (Union[str, None], optional): Name of the output JSON file. Defaults to None.
        output_dir (Union[str, None], optional): Directory where to save the file. Defaults to os.getcwd().

    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    keyword_scraper = Keywords_api(query, proxy, tweets_count)
    data = keyword_scraper.scrap()
    if output_filename and len(data) > 0:
        path = os.path.join(output_dir, "{}.json".format(output_filename))
        mode = 'w'
        if os.path.exists(path):
            logger.setLevel(logging.INFO)
            logger.info('The File has been Existed. Update it.')
        # with open(path, 'w', encoding='utf-8') as file_in_write_mode:
        #     json.dump(data, file_in_write_mode)
        #     logger.info('Data was saved to {}'.format(path))
        return data
    else:
        return data
