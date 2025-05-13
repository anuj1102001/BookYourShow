# 🎬 BookYourShow

BookYourShow is a full-featured Django-based web application that replicates the core functionality of platforms like BookMyShow. It allows users to browse movies, log in, book tickets, choose seatings, make payments through Stripe, and track their booking history — all in a sleek and intuitive UI.

---

## 🚀 Features

- 🎞️ **Movie Listings**: Browse all currently available movies with posters and descriptions.
- 🔐 **User Authentication**: Register, log in, and manage your account securely.
- 🎟️ **Movie Ticket Booking**: Click on a movie → choose show timing → select seats → proceed to payment.
- 💳 **Stripe Integration**: Secure and smooth payment gateway for ticket purchases.
- 👤 **User Profile**: View and manage your past and current ticket orders.
- 🧾 **Order History**: Track bookings and payment statuses anytime.
- ⚙️ **Admin Panel**: Manage movies, showtimes, and bookings from the Django admin dashboard.

---

## 🛠️ Built With

- [Django]– High-level Python web framework
- [HTML/CSS/JS] – For responsive frontend
- [Bootstrap] – For sleek UI components
- [Stripe API](https://stripe.com/docs/api) – For handling payments securely

---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/anuj1102001/BookYourShow.git
   cd BookYourShow
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your Stripe API keys in .env or settings

env
Copy
Edit
STRIPE_PUBLIC_KEY=your_public_key
STRIPE_SECRET_KEY=your_secret_key
Run migrations and start server

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
📂 Project Structure
bash
Copy
Edit
BookYourShow/
├── static/
├── templates/
├── movies/              # Main app for movies and bookings
├── users/               # Handles authentication and profile
├── payments/            # Stripe payment processing
├── manage.py
└── requirements.txt
✅ Future Improvements
🎬 Admin movie upload with trailers

📱 Progressive Web App (PWA) for mobile users

🧾 Downloadable ticket PDFs

📧 Email confirmation after booking

🌐 SEO & meta tag enhancements

🙌 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

📬 Contact
Made by Anuj M

DM me on LinkedIn or drop a mail at anujleo46@gmail.com if you'd like to collaborate!


