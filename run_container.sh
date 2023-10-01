#!/bin/bash

# Define the name of your Docker image
IMAGE_NAME="containerizedapps:latest"

# Check if the Docker image exists
if [ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]; then
    echo "Docker image $IMAGE_NAME not found. Building..."
    docker build -t $IMAGE_NAME .
else
    echo "Docker image $IMAGE_NAME found."
fi

# Start a new Docker container
echo "Starting a new Docker container..."
docker run -d -e HF_HOME=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 -p 5000:80 $IMAGE_NAME
echo "New Docker container started."

# # chmod +x run_container.sh => gives the necessary permissions (+x => add execute permission)
# # needed to run the script

