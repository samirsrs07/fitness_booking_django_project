# Fitness Booking API
How to Run the Django Fitness Booking Project Locally
Step 1: Unzip the Project
--------------------------------------
1. Unzip the downloaded 'fitness_booking_django_project.zip' to your desired location.
Step 2: Open Terminal or Command Prompt
--------------------------------------
1. Navigate to the project directory:
cd path/to/fitness_booking_django_project
Step 3: Create Virtual Environment (if not already created)
--------------------------------------
python -m venv env
env\Scripts\activate (for Windows)
source env/bin/activate (for Mac/Linux)
Step 4: Install Dependencies
--------------------------------------
pip install -r requirements.txt
Step 5: Run Migrations
--------------------------------------
python manage.py makemigrations
python manage.py migrate
Step 6: Create Superuser for Admin Panel
--------------------------------------
python manage.py createsuperuser
(Enter username, email, password)
Step 7: Collect Static Files (if needed)
--------------------------------------
python manage.py collectstatic
(Type 'yes' when prompted)
Step 8: Run the Server
--------------------------------------
python manage.py runserver
Step 9: Access the Application
--------------------------------------
Home Page: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
API Docs: http://127.0.0.1:8000/docs/
API Schema: http://127.0.0.1:8000/schema/
Get Classes: http://127.0.0.1:8000/api/classes/
Book Class (POST): http://127.0.0.1:8000/api/book/
Bookings by Email: http://127.0.0.1:8000/api/bookings/?email=your_email
All APIs are also available in Swagger UI under /docs/ route.