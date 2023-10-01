# Building the docker image
docker build -t containerizedapps:latest .

# Running the docker container
docker run -e HF_HOME=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 -p 5000:80 containerizedapps:latest

# chmod +x run_container.sh => gives the necessary permissions (+x => add execute permission)
# needed to run the script