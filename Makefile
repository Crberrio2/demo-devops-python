IMAGE ?= demo-devops-python:local

.PHONY: install test lint security coverage docker-build docker-run k8s-deploy k8s-delete

install:
	pip install -r requirements-dev.txt

test:
	python manage.py test

lint:
	flake8 .

security:
	bandit -r api demo -ll

coverage:
	coverage run manage.py test && coverage report

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run --rm -p 8000:8000 -e DJANGO_SECRET_KEY=local-secret $(IMAGE)

k8s-deploy:
	kubectl apply -k k8s/
	kubectl -n demo-devops rollout status deployment/demo-devops-python

k8s-delete:
	kubectl delete -k k8s/
