from api.tweets import register_tweet_blueprint
from api.detection import register_detection_blueprint


def init_view(app):
    register_tweet_blueprint(app)
    register_detection_blueprint(app)
