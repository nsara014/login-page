@echo off

:: Start Docker Desktop if not already running (Windows)
start "" "%ProgramFiles%\Docker\Docker\Docker Desktop.exe"

:: Wait for Docker Daemon to be ready
:wait_for_docker
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo Waiting for Docker to start...
    timeout /t 5 >nul
    goto wait_for_docker
)

echo Docker is ready!


:: Run Docker container using Docker Compose
start "" docker-compose up --build

timeout /t 10 >nul

echo Running Postman tests using Newman...

:: Install Newman globally if not already installed
npm install -g newman

:: Run Postman tests with Newman
start "" newman run "./test/CoRiderAssign.postman_collection.json"

docker-compose down