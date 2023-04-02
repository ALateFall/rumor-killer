from flask import Flask
from api.tweets.tweets import tweet_blueprint


def register_tweet_blueprint(app):
    app.register_blueprint(tweet_blueprint)