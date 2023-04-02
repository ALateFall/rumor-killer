from flask import Blueprint
from database.utils import *
from spider.spider import *

tweet_blueprint = Blueprint('tweets', __name__, url_prefix="/tweets", template_folder="../../templates")


@tweet_blueprint.route('/getTrendingTweets', methods=["post"])
def getTrendingTweets():
    result = query_tweet(0, 20)
    return result


@tweet_blueprint.route('/makeScrape', methods=['get'])
def make_scrape():
    tweet = get_trending_tweets()
    tweets_to_mysql(tweet)
    return "done!"
