# FastAPI URL Shortener

🐍 Basic example of a URL shortener project developed using FastAPI, a modern Python web framework.

## Description

This URL shortener allows users to input a long URL and generate an equivalent short URL. Users can then use the generated short URL to quickly access the original URL.

## TODO
- [x] Shortens long URLs into short URLs.
- [x] Get original URLs by short URL.
- [x] tests apis.
- [] test use case.
- [] Implement frontend.
- [] Add some cache mechanism.

## Local run
````pip install -r requirements.txt```` or ````pip install -r requirements-tests.txt````
___
````uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload````

### Run test
````python -m pytest````

````python -m pytest --cov=src````

# Ruff commands
Check linters errors
````ruff check src````

Check format errors
````ruff format -- check src````

Fix imports order

````ruff --fix src````

Fix file format

````ruff format src````