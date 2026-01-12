# ALX Travel App – 0x00

## Overview
This project defines core database models, serializers, and a seeding mechanism
for the ALX Travel App.

## Features
- Listings, Bookings, and Reviews models
- REST serializers for API representation
- Management command for database seeding
- Swagger-ready API structure

## Models
- Listing
- Booking
- Review

## Seeder

python manage.py seed
# ALX Travel App – Chapa Payment Integration

## Overview
This project integrates the Chapa payment gateway to handle booking payments.

## Features
- Payment initiation via Chapa API
- Payment verification
- Payment status tracking
- Secure API key handling

## Payment Status Flow
- Pending → Completed / Failed

## API Endpoints
- POST /api/payment/initiate/
- GET /api/payment/verify/

## Tech Stack
- Django
- Django REST Framework
- Chapa API
- Celery
# ALX Travel App – Celery Background Tasks

## Overview
This project integrates Celery with RabbitMQ to handle background tasks asynchronously.
A booking confirmation email is sent without blocking the main request flow.

## Technologies
- Django
- Celery
- RabbitMQ
- Django Email Backend

## Features
- Asynchronous email notifications
- Background task processing
- Improved performance and UX

## Workflow
1. User creates a booking
2. Booking is saved immediately
3. Email task is queued via Celery
4. Celery worker sends confirmation email

## How to Run
- Start RabbitMQ
- Run Celery worker
- Run Django server
