# Set the base image to the official Python 3 image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest
RUN pip install --no-cache-dir pytest

# Run the test suite
RUN pytest

# Run the command to start the application
CMD [ "python", "isbn_valid.py" ]
