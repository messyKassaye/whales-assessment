# Dockerfile

# Use official Python image from DockerHub
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make the entrypoint.sh executable
RUN chmod +x entrypoint.sh

# Expose the port
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
