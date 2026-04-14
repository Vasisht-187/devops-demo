FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer —
# so re-builds are faster if only code changed, not deps)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Tell Docker our app listens on port 5000
EXPOSE 5000

# The command to start the app when the container runs
CMD ["python", "app/main.py"]