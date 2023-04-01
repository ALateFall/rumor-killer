from app import db
from database.model.tweets import Tweets
from app import app


def insert_tweet(keywords, tweet_text, tweet_id, user_name, user_id, user_followers_count, user_friends_count, image_url
                 , create_time, retweet_count, likes_count):
    with app.app_context():
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
        except:
            status = 'Failed to insert the record of tweet id {}'.format(t.tweet_id)
    return status
