# Hotel Management System API

A professional REST API built with Django for hotel receptionists to manage rooms and guest reservations.

## Key Technical Features

- JWT Authentication: Secure staff login using JSON Web Tokens.
- Dynamic Room Inventory: Supports letter-based blocks (e.g., "Block A") and categorized room types.
- Reservation Logic: Real-time booking management with automated date validation.

## Project Organization

Refactored into a flat, professional structure for high discoverability:

- `accounts/`: Staff user management.
- `rooms/`: Inventory and category logic.
- `reservations/`: Booking management.
- `Booking_system/`: Core configuration.

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`
