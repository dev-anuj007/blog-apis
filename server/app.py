import os

from flask import Blueprint, Flask

from services.logger.logger_service import LoggerService

# Loading logger services
logger = LoggerService.get_logger()
logger.info(message="Logger service is loaded !")

# Check for mypy config
is_ok = os.system("pipenv run mypy --config-file mypy.ini services")
assert not is_ok

# Check for vulture config
is_ok = os.system("pipenv run vulture")
assert not is_ok

# Check pants
is_ok = os.system("./pants --pants-config-files=pants.toml --changed-since=origin/main lint")
assert not is_ok, f"please user `make pants-fmt` to fix this error"

app = Flask(__name__)
blueprint = Blueprint("", __name__, url_prefix="")
blueprint.add_url_rule("/", "", view_func=lambda: "<h1> Start your development.. </h1>")

app.register_blueprint(blueprint)
