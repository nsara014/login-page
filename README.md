# Flask MongoDB CRUD Application

This project is a Flask-based application that performs CRUD operations on a MongoDB database for a User resource via REST API endpoints. The application is containerized using Docker and includes testing via Postman.

## Table of Contents

- [Features](#Features)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Scalability](#scalability)

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

```bash
git clone https://github.com/nsara014/login-page.git
```

### 2.Navigate to the project directory:

```bash
cd login-page
```

### 3.Run the provided run.bat script to start the Flask application in Docker.

```bash
./run.bat
```

## 4.In a separate terminal, install Newman globally and run the Postman test collection:

```bash
Copy code
npm install -g newman
newman run "./test/CoRiderAssign.postman_collection.json"
```

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

## Scalability

- Pagination - Pagination is used to limit the number of users returned per request. This is essential for improving performance when handling large datasets.
- Indexing - MongoDB indexes are used to optimize query performance, particularly for fields - id.
- Cacheing - Simple Cache was used. SimpleCache is used to store frequently accessed data (like user lists) in memory, significantly reducing the number of database calls for data that doesn't change often. However, If this were production Simplecache has to be changed to redis cache with a new docker image for redis.

Others that needs to be considered to make the app more scalable can be Celery for Asynchronous Tasks. We can use Celery to handle long-running tasks asynchronously, such as sending emails after user registration.
