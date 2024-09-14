# Flask MongoDB CRUD Application

This project is a Flask-based application that performs CRUD operations on a MongoDB database for a User resource via REST API endpoints. The application is containerized using Docker and includes testing via Postman.

## Table of Contents

- [Features](#Features)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)

## Features

- RESTful API for CRUD operations on a MongoDB database.
  = User resource includes id, name, email, and password fields.
  = Dockerized for seamless deployment and scalability.
- Postman testing collection provided for API validation.

## Prerequisites

Make sure you have the following installed

- Docker
- Python
- Node.js (for running Newman via npm)
- npm (Node Package Manager)

## Installation

### 1. Clone the repository:

````bash
git clone https://github.com/nsara014/login-page.git

### 2.Navigate to the project directory:

```bash
cd login-page

### 3.Run the provided run.bat script to start the Flask application in Docker.

```bash
./run.bat

## 4.In a separate terminal, install Newman globally and run the Postman test collection:
```bash
Copy code
npm install -g newman
newman run "./test/CoRiderAssign.postman_collection.json"

## Running the Application
Once the run.bat script has been executed, the Flask application should be running inside a Docker container. By default, it will be accessible at http://localhost:5000.

## Testing
### Postman Collection:
A Postman collection file is included in the ./test/CoRiderAssign.postman_collection.json path.
Newman will run the Postman test collection via the command above to validate the CRUD operations.

## API Endpoints
- GET /users - Retrieves a list of all users.
- GET /users/<id> - Retrieves a specific user by ID.
- POST /users - Creates a new user.
- PUT /users/<id> - Updates an existing user by ID.
- DELETE /users/<id> - Deletes a user by ID.

## Project Structure
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── config.py
├── Dockerfile
├── run.bat
├── test/
│   └── CoRiderAssign.postman_collection.json
├── requirements.txt
└── README.md
````
