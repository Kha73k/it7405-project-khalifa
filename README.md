# Khalifa Polish - Car Detailing & E-Commerce Platform

A professional car polishing and detailing service website built with Django and MongoDB.

## Features

- 🚗 **Service Booking System** - Customers can book appointments for car detailing services
- 🛒 **E-Commerce Shop** - Browse and purchase car care products
- ⭐ **Customer Reviews** - Submit and view customer testimonials
- 👤 **User Authentication** - Secure login/registration system
- 📦 **Order Management** - Track orders and view order history
- 📅 **Appointment Management** - View and manage service appointments
- 🛍️ **Shopping Cart** - Add products and checkout seamlessly

## Technologies Used

- **Backend:** Django
- **Database:** MongoDB (via Djongo)
- **Frontend:** Bootstrap, Custom CSS
- **Authentication:** Django's built-in auth system
- **Media Storage:** File-based storage for product images

## Installation

### Prerequisites
- Python 3.11.14
- MongoDB 8.2 or higher

Database Configuration
-This project uses **MongoDB Atlas** for cloud database hosting.
The MongoDB Atlas connection is already configured in `settings.py`. The database includes:
   - Sample products
   - Services
   - Customer reviews
   - User accounts


STEP-BY-STEP SETUP:

1. INSTALL MONGODB
   - Install MongoDB Server 8.2
   - Make sure MongoDB service is running

 2. SETUP PYTHON PROJECT
   - Copy the 'project' folder to your desired location (e.g., Desktop)
   - Open terminal in the project folder
   - Create virtual environment: python -m venv car_polish_env
   - Activate it:
     Windows: car_polish_env\Scripts\activate
     Mac/Linux: source car_polish_env/bin/activate
   - Install packages: pip install -r requirements.txt

3. RUN THE WEBSITE
   - python manage.py runserver
   - Open browser: http://127.0.0.1:8000


