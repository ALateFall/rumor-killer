from database.database import db
from database.model.tweets import Tweets
import traceback
# from app import app


def insert_tweet(keywords, tweet_text, tweet_id, user_name, user_id, user_followers_count, user_friends_count, image_url
                 , create_time, retweet_count, likes_count):
    # with app.app_context():
    t = Tweets()
    t.keywords = keywords
    t.tweet_text = tweet_text
    t.tweet_id = tweet_id
    t.user_name = user_name
    t.user_id = user_id
    t.user_followers_count = user_followers_count
    t.user_friends_count = user_friends_count
    t.images_url = image_url
    t.create_time = create_time
    t.retweet_count = retweet_count
    t.likes_count = likes_count
    status = "Insert a record successfully, tweet id is {}.".format(t.tweet_id)
    try:
        db.session.add(t)
        db.session.commit()
    except Exception as e:
        print(e.encode('utf-16'))
        db.session.rollback()
        status = 'Failed to insert the record of tweet id {}'.format(t.tweet_id)
    return status


def query_tweet(start, count):
    result = db.session.query(Tweets).order_by(Tweets.images_url.desc(), Tweets.create_time.desc()).filter().slice(start, start + count).all()
    result = [r.to_dict() for r in result]
    return result

