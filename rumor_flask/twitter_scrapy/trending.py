#!/usr/bin/env python3

from typing import Union
from .scraping_utilities import Scraping_utilities
import os
import logging
import json

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Trending_Location:
    def __init__(self, proxy: Union[str, None]) ->None:
        """

        :type proxy: object
        """
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.proxy = proxy

    def scrape(self):
        guest_token = Scraping_utilities.find_x_guest_token(
            authorization_key=self.authorization_key, proxy=self.proxy)
        headers = Scraping_utilities.build_keyword_headers(
            authorization_key=self.authorization_key, x_guest_token=guest_token)
        response = Scraping_utilities.make_http_request(
            "https://api.twitter.com/1.1/trends/available.json",
            headers=headers, proxy=self.proxy)
        if response:
            return response
        else:
            logger.debug('Failed to Make Request!')


class Trending:
    def __init__(self, proxy: Union[str, None]) ->None:
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.proxy = proxy

    def scrape(self):
        guest_token = Scraping_utilities.find_x_guest_token(
            authorization_key=self.authorization_key, proxy=self.proxy)
        headers = Scraping_utilities.build_keyword_headers(
            authorization_key=self.authorization_key, x_guest_token=guest_token)
        response = Scraping_utilities.make_http_request(
            "https://api.twitter.com/1.1/trends/place.json?id=1",
            headers=headers, proxy=self.proxy)
        if response:
            return response
        else:
            logger.debug('Failed to Make Request!')


def get_trendings(json_file_location: str, proxy: Union[str, None] = None, filename: str = "", directory: str = os.getcwd()):
    """Extract Trending tweets.

    Args:
        json_file_location (str) : Indicate where the location.json is.
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        filename (str, optional): Filename where to save the output. Defaults to "".
        directory (str, optional): Directory where to save the file. Defaults to os.getcwd().
    Returns:
        (dict | none): None if data was saved, else JSON String.
    """

    trending_location_bot = Trending_Location(proxy=proxy)
    data = trending_location_bot.scrape()

    if len(data) > 0:
        # json_file_location = os.path.join('trending_json', 'location.json')
        if os.path.exists(json_file_location):
            logger.setLevel(logging.INFO)
            logger.info('The Location File is Existed. Update Now.')
        with open(json_file_location, 'w', encoding='utf-8') as file_in_write_mode:
            json.dump(data, file_in_write_mode)
            logger.setLevel(logging.INFO)
            logger.info(
                'Location Data Successfully Saved to {}'.format(json_file_location))
        # return data
    else:
      return json.dumps(data)

    logger.setLevel(logging.INFO)
    logger.info('Sucessfully Get Location. Now Get Tweets from Trending.')

    trending_bot = Trending(proxy=proxy)
    data = trending_bot.scrape()

    if len(data) > 0:
        json_file_location = os.path.join(directory, filename + ".json")
        if os.path.exists(json_file_location):
            logger.setLevel(logging.INFO)
            logger.info('The Trending Tweets Json File has been Existed.')
        with open(json_file_location, 'w', encoding='utf-8') as file_in_write_mode:
            json.dump(data, file_in_write_mode)
            logger.setLevel(logging.INFO)
            logger.info(
                'Trending Data Successfully Saved to {}'.format(json_file_location))
        return data
    else:
        return json.dumps(data)

