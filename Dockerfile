# Dockerfile
FROM python:3.9

WORKDIR /app

# Copy all contents to the container
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
