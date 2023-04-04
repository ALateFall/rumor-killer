from flask import Blueprint, request
from database.utils import *
from rumor_model.evaluate import *

detection_blueprint = Blueprint('detection', __name__, url_prefix="/detection", template_folder="../../templates")


@detection_blueprint.route('/detectionTweet', methods=["post"])
def detectionTweet():
    data = request.get_json()
    # print(data)
    result = test(data['tweet_text'], data['image_url'])
    return result

