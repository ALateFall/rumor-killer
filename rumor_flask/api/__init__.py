from api.tweets import register_tweet_blueprint


def init_view(app):
    register_tweet_blueprint(app)