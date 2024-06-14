# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt in the folder you are, create a requirements.txt in you Work Dir - . = requirements.txt
COPY requirements.txt . 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# For documentation only, it shows taht the port 5000 is the one intended for the app.
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]