import os

from flask import Flask, Blueprint
from services.logger.internal.console_logger import ConsoleLogger
print("my os ==", os.getenv("ENVIRONMENT"))

app = Flask(__name__)
blueprint = Blueprint('', __name__, url_prefix='')
blueprint.add_url_rule(
    '/', '', view_func=lambda: "<h1> Start your development.. </h1>")

app.register_blueprint(blueprint)
