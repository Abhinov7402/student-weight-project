FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir numpy pandas scikit-learn

# Copy the rest of your code
COPY . .

# Use -u to see the output in real-time
CMD ["python", "-u", "app.py"]