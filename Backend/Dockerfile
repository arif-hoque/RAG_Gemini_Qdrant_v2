# FROM python:3.10-slim
# WORKDIR /app

# COPY requirements.txt app/requirements.txt
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*
# RUN pip install --no-cache-dir -r ./app/requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ,"--reload"]

# Use the official Python image as a base image
FROM python:3.10-slim


# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .


# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]