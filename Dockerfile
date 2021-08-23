# Set base image (host OS)
FROM python:3.6-stretch

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /cont

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY run.py .
ADD app ./app

# Specify the command to run on container start
CMD [ "python", "./run.py" ]
