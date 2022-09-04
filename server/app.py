from flask import Flask, Blueprint
from services.logger.logger_service import LoggerService

# Loading logger services
logger = LoggerService.get_logger()
logger.info(message="Logger service is loaded !")

app = Flask(__name__)
blueprint = Blueprint('', __name__, url_prefix='')
blueprint.add_url_rule(
    '/', '', view_func=lambda: "<h1> Start your development.. </h1>")

app.register_blueprint(blueprint)
