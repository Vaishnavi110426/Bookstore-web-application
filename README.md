📚 Bookstore – Django Web Application
🧩 Overview

The Bookstore is a full-stack web application built using Django that allows users to browse, manage, and purchase books online.
It provides an intuitive admin panel, user authentication, and a clean, responsive interface for managing book data efficiently.

🚀 Features

✅ User Authentication – Signup, Login, and Logout with Django’s built-in auth system.
✅ Book Management – Add, edit, delete, and view detailed book records.
✅ Category Filtering – Organize books by genre, author, or category.
✅ Responsive UI – Optimized layout for desktop and mobile.
✅ Admin Dashboard – Django Admin interface for managing inventory and orders.
✅ Search & Pagination – Easily find books with search functionality and smooth navigation.
✅ Requirements File – Quickly install dependencies using requirements.txt.

🛠️ Tech Stack

Backend: Django, Python

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default) or PostgreSQL (optional)

Version Control: Git & GitHub

⚙️ Installation

Clone the repository

git clone https://github.com/<your-username>/bookstore.git
cd bookstore


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the server

python manage.py runserver


Access the app

🌐 App: http://127.0.0.1:8000/

🔑 Admin Panel: http://127.0.0.1:8000/admin/

📂 Project Structure
bookstore/
├── bookstore/           # Main Django configuration
├── templates/           # HTML templates
├── static/              # CSS, JS, and image files
├── books/               # Core app (models, views, urls)
├── requirements.txt     # Dependencies
└── manage.py            # Django management script

✨ Future Enhancements

🛒 Shopping cart & checkout system

💳 Payment gateway integration

📊 User analytics & recommendations

🌙 Dark mode and enhanced UI animations

👨‍💻 Author

Pragathi Vaishnavi
Aspiring Developer | Django & AI Enthusiast
