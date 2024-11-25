# Use the official Python image with version 3.10
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Set the default command to run the app
CMD ["bash", "./run.sh"]
