# Event Management System (approveEase)

A Django-based event management web app with event creation, listing, and approval workflow.

## Features
- Create new events
- View list of events
- Media/image upload support for events
- Admin panel (Django built-in)

## Tech Stack
- Python / Django
- HTML/CSS (templates)
- SQLite (default Django DB, unless configured otherwise)

## Setup
1. Clone this repo
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure
- `manage.py` — Django management entry point
- `approveEase_config/` — project settings, URLs, WSGI/ASGI config
- `event/` — main app: models, views, forms, admin, migrations
- `templates/` — HTML templates (`create_event.html`, `eventlist.html`)
- `media/images/` — uploaded event images

## Status
This was built as a learning project to practice Django fundamentals — models, views, templates, and media handling.