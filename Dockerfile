# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY app.py .

# Run the script with the -u flag to ensure output isn't buffered 
# (Important for interactive terminal prompts in Docker)
CMD ["python", "-u", "app.py"]