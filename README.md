# BookYourShow

A movie ticket booking web app built with Django, modelled on the core flow of platforms like BookMyShow: browse movies, pick a theatre and showtime, choose seats, pay with Stripe (test mode) and see your past bookings.

Built in early 2025 during my Python full-stack bootcamp (QSpiders) as a learning project.

## Features

- **Movies:** listings with posters and details, filters, and reviews on the movie page
- **Accounts:** register and log in with email, or with Google (django-allauth)
- **Booking:** movie → theatre and showtime → seat selection
- **Payments:** Stripe checkout in test mode, with success and cancel pages
- **Orders:** a page listing your bookings and payment status
- **Admin:** manage movies, theatres, showtimes and bookings in the Django admin

## Tech stack

Python · Django 5.1 · Django REST framework · django-allauth · Stripe API · SQLite · HTML, CSS, JavaScript · Bootstrap 4 (crispy-forms)

## Run it locally

```bash
git clone https://github.com/anuj1102001/BookYourShow.git
cd BookYourShow
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # then add your own Stripe test keys
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then add movies, theatres and showtimes in the admin at `http://127.0.0.1:8000/admin/`.

All keys (Django secret key, Stripe, Google sign-in, Gmail SMTP) are read from environment variables or a local `.env` file, which is git-ignored. See [.env.example](.env.example).

## Project structure

```
Accounts/        custom user model, registration and login
Movies/          movie listings, details and filters
Theatre/         theatres, seats and showtimes
Bookings/        seat selection and bookings
Payment/         Stripe checkout
Dashboard/       a user's orders
Reviews/         movie reviews
book_your_show/  settings and URL configuration
templates/       HTML templates
static/          CSS, JavaScript and images
```

## Known gaps

- The orders page expects a `dashboard/home.html` template that isn't in the repository yet.
- Development settings only: not configured for production deployment.
