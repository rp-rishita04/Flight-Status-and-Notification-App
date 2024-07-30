# Flight-Status-and-Notification-App


This project provides real-time flight status updates and notifications to passengers. It features a frontend built with React.js, a backend powered by Python, and a PostgreSQL database. Notifications are managed using Firebase Cloud Messaging.

## Features

- **Real-time Updates**: Display current flight status including delays, cancellations, and gate changes.
- **Push Notifications**: Send notifications for flight status changes via SMS, email, or app notifications.
- **Integration with Airport Systems**: Pull data from airport databases for accurate information.

## Technologies Used

- **Frontend**: React.js, HTML, CSS
- **Backend**: Python
- **Database**: PostgreSQL
- **Notifications**: Firebase Cloud Messaging or Kafka

## Project Structure

flight-status-system/
├── backend/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ └── FlightStatus.js
│ │ ├── App.js
│ │ └── index.js
│ ├── Dockerfile
│ ├── package.json
│ └── yarn.lock
├── database/
│ ├── Dockerfile
│ ├── init.sql
├── docker-compose.yml
└── README.md

## Prerequisites

- Docker
- Docker Compose

Access the application:

Frontend: Open your browser and go to http://localhost:3001
Backend: The backend is accessible at http://localhost:5001
Database: PostgreSQL runs on port 5432 of your host machine

