# Django Product Scraper

[![Django CI](https://github.com/ashfakmohamed/django-product-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/ashfakmohamed/django-product-scraper/actions/workflows/ci.yml)

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
$env:DJANGO_SECRET_KEY="replace-with-a-long-random-secret"
$env:DJANGO_DEBUG="True"
python manage.py migrate
python manage.py runserver
```

Use `.env.example` as the configuration reference. The application reads settings from environment variables and does not load `.env` files automatically.

## Checks

```bash
python manage.py check
python manage.py test
```

Local databases, Python caches, secrets, and virtual environments are excluded from Git.
