# Django Product Scraper

A Django project that runs a product scraper, stores the collected data, and exposes the workflow through a web view.

## Technology

- Python
- Django
- Requests
- Beautiful Soup

## Run locally

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Checks

```bash
python manage.py check
python manage.py test
```

Local databases, Python caches, secrets, and virtual environments are excluded from Git.
