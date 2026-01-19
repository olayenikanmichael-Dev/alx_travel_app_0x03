Deployed link on render:  https://alx-travel-app-0x03-h4po.onrender.com

## 📌 Project Overview

`alx_travel_app_0x03` is an extension of the previous travel booking application that introduces **asynchronous background task processing** using **Celery** and **RabbitMQ**.
The primary goal of this project is to handle **email notifications for bookings asynchronously**, improving application performance and user experience.

This project demonstrates how to:

* Configure Celery with RabbitMQ
* Create and execute background tasks
* Send booking confirmation emails asynchronously in Django

---

## 🎯 Objectives

* Configure **Celery** with **RabbitMQ** as the message broker
* Define a background task to send booking confirmation emails
* Trigger the email task upon booking creation
* Ensure email notifications are processed asynchronously

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **Django REST Framework**
* **Celery**
* **RabbitMQ**
* **SMTP / Django Email Backend**

---

## 📁 Project Structure

```
alx_travel_app_0x03/
│
├── alx_travel_app/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── listings/
│   ├── tasks.py
│   ├── views.py
│   ├── models.py
│   └── serializers.py
│
├── manage.py
└── README.md
```

---

## ⚙️ Configuration Steps

### 1️⃣ Duplicate Project

The project was duplicated from:

```
alx_travel_app_0x02 → alx_travel_app_0x03
```

---

### 2️⃣ Celery Configuration

#### `alx_travel_app/celery.py`

* Initializes the Celery app
* Loads Django settings
* Auto-discovers tasks

#### `settings.py`

Celery and RabbitMQ configurations:

```python
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

---

### 3️⃣ Email Backend Configuration

Configured in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

---

## 📩 Background Email Task

### `listings/tasks.py`

A shared Celery task is defined to send booking confirmation emails:

* Uses Django’s email backend
* Runs asynchronously
* Sends booking confirmation details to the user

```python
@shared_task
def send_booking_confirmation_email(email, booking_details):
    send_mail(
        subject='Booking Confirmation',
        message=booking_details,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
```

---

## 🔁 Triggering the Task

### `listings/views.py`

The email task is triggered in the `BookingViewSet` when a booking is created:

```python
send_booking_confirmation_email.delay(user.email, booking_info)
```

This ensures:

* Booking creation is not blocked
* Email is sent in the background

---

## 🧪 Testing the Background Task

### Steps to Test

1. Start **RabbitMQ**

   ```bash
   sudo service rabbitmq-server start
   ```

2. Start the **Celery worker**

   ```bash
   celery -A alx_travel_app worker -l info
   ```

3. Run the Django server

   ```bash
   python manage.py runserver
   ```

4. Create a booking via API or frontend

5. Verify:

   * Booking is created successfully
   * Email is sent asynchronously
   * Celery worker logs show task execution

---

## ✅ Expected Outcome

* Booking creation works normally
* Confirmation email is sent in the background
* No delay or blocking during booking requests
* Celery and RabbitMQ handle tasks efficiently

---

## 📌 Repository Information

* **GitHub Repository:** `alx_travel_app_0x03`
* **Main Directory:** `alx_travel_app`
* **Key Files:**

  * `alx_travel_app/settings.py`
  * `alx_travel_app/celery.py`
  * `listings/tasks.py`
  * `listings/views.py`
  * `README.md`

---

## 👨‍💻 Author

**ALX Backend Engineering Student**


