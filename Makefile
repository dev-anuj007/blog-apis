DIR=services/

mypy:
	pipenv run mypy --config-file mypy.ini services
runserver:
	pipenv run gunicorn  'server.app:app' --reload
test:
	pipenv run pytest ${DIR}
vulture:
	pipenv run vulture
