.PHONY: docs

docs:
	black pysaal & isort pysaal & cd docs && make html