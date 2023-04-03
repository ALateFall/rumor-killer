from flask import Blueprint
from database.utils import *
from rumor_model.evaluate import *

detection_blueprint = Blueprint('detection', __name__, url_prefix="/detection", template_folder="../../templates")


@detection_blueprint.route('/detectionTweet', methods=["post"])
def detectionTweet():
    result = query_tweet(0, 20)
    # print(result)
    for item in result:
        if (',' not in item['images_url']) and (item['images_url']) != "" :
            test(item['tweet_text'], item['images_url'])
    # return result

