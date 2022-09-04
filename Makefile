mypy:
	pipenv run mypy --config-file mypy.ini services
runserver:
	pipenv run gunicorn  'server.app:app' --reload

vulture:
	pipenv run vulture