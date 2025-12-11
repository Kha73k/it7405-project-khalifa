# Khalifa Polish - Car Detailing & E-Commerce Platform

A professional car polishing and detailing service website built with Django and MongoDB, Connected using Djongo connector

## Features

- **Service Booking System** - customers can book appointments for car detailing services
- **E-Commerce Shop** - purchase car care products
- **Customer Reviews** - submit and view customer reviews
- **User Authentication** - secure login/registration system
- **Order Management** - track orders and view order history
- **Appointment Management** - view and manage service appointments
- **Shopping Cart** - add products and checkout smoothly

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
   - products
   - Services
   - customer reviews
   - user accounts


STEP-BY-STEP SETUP:

1. INSTALL MONGODB
   - Install MongoDB Server 8.2
   - Make sure MongoDB service is running in the services tab

 2. SETUP PYTHON PROJECT
   - clone the project folder from github to your desired location
   - create an environment in anaconda navigator, make sure you choose python 3.11
   - open a powershel terminal in anaconda navigator and type: cd Your/folder/location/here
   - type:  code .
   - once in vscode open a terminal
   - Activate environment: conda activate YourEnvironmentName
   - Install packages: pip install -r requirements.txt

3. RUN THE WEBSITE
   - python manage.py runserver
   - Open browser: http://127.0.0.1:8000

4. TO USE MONGODB COMPASS TO VIEW DATA.
   - Click the green button to add a new connection
   - go to 'Advanced Connection Options'
   - in the 'Connection String Scheme' click 'mongodb+srv'
   - replace the URI above with this: 'mongodb+srv://kha73k:yuA7m9I3bSDycuY6@khalifacluster.enykws4.mongodb.net/'

5. TO USE THE ADMIN PAGE.
   - type in the terminal : python manage.py createsuperuser
   - choose a username
   - you can ignore the email part by just clicking enter
   - choose a secure password and confirm it
   - open the brower and enter the admin page http://127.0.0.1:8000/admin
   - make sure to save if you modify something


   ENJOY......
   
