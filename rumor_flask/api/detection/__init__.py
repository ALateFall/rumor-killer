from api.detection.detection import detection_blueprint


def register_detection_blueprint(app):
    app.register_blueprint(detection_blueprint)