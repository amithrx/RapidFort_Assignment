# GitaGPT2: Unleashing the Wisdom of Krishna
## About
This is a GPT2 based chatbot trained on Bhagavad Gita which help user's to get answers to their questions from the wisdom of Krishna. 
## Available on: https://gitagpt2.streamlit.app/

![Image]()

### Folder Structure
The workspace contains the following folders/files:
`app.py` - Frontend application built using streamlit.  
`Dockerfile` - Dockerfile to build the docker image.  
`main.py` - Backend application built using flask.  
`README.md` - Readme file.  
`requirements.txt` - Contains libraries/dependencies required to build docker images.  
`run_container.sh` - Shell script to build docker image and run the container.  
`bb.yaml` - Contains the configuration for setting kubernetes cluster for hosting web server.


### Installation and Setup
1. Clone the repository `git clone https://github.com/amithrx/RapidFort_Assignment`
2. Download Docker Desktop for your operating system from the official website: [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)

### Note
If you encounter any issue during the installation or running of docker container, refer to the official documentation of docker: [Docker Documentation](https://docs.docker.com/)

### Build Docker Image
To run the backened server built using flask, follow the steps below:
1. Open the terminal and navigate to the project directory where dockerfile is present.
```cd <path to project directory>```
2. Give the execute permission to the shell scripts.
```chmod +x run_container.sh```
3. Run the following command to run the shell script.
```./run_container.sh```
4. The docker image will be built and the container will be started. The server will be running on port 5000 of the localhost and can be accessed using the url: http://localhost:5000/ and is mapped to port 80 of the container.

5. Alternatively:
- The docker image is made available on docker hub and can be pulled into the local using the following command:
```docker pull 1amithrx/chatbot```
- The container can be started using the following command:
```docker run -e HF_HOME=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 -p 5000:80 1amithrx/chatbot```

### Accessing the Application
1. Open the browser and navigate to the url: http://localhost:5000/ to access the backend server.  
2. The frontend is built using streamlit and can be accessed using the url: https://gitagpt2.streamlit.app/

### Cleaning up
1. To stop the container, run the following command:
```docker stop <container_id>```
2. Remove the container using the following command:
```docker rm <container_id>```
3. Remove the image using the following command:
```docker rmi <image_id>```

### Kubernetes Cluster
The backend server is hosted on kubernetes cluster using the following command:
```kubectl apply -f bb.yaml```
The server is exposed using the load balancer service and created 3 replicas of the pod.

### API Documentation
1. '/getResponse' : POST request
- Request Body: 
```
{
    "question": "What is the purpose of life?"
}
```
- Response Body:
```
{
    "answer": "The purpose of life is to attain liberation from the cycle of birth and death and attain the supreme abode of Lord Krishna."
}
```
2. '/' : GET request
- Response Body:
```
{
    "message": ""
}
```
- Response Body:
```
{
    "message": "Hello world"
}
```

### Milestones Achieved
1. Dockerized the applications. Created a docker image for the backend server built using flask.
2. Docker hub contains images for both the architectures: amd64 and arm64.
2. Deployed the frontend application on streamlit.
3. Added the github actions/pipelines to build the docker image and push it to docker hub.
4. Created a kubernetes manifest files to host the backend server on kubernetes cluster.
5. Created a bash script to build the docker image and run the container.

### References
1.https://ai.meta.com/blog/large-language-model-llama-meta-ai/  
2.https://github.com/facebookresearch/llama    
3.https://github.com/facebookresearch/llama-recipes    
4.https://huggingface.co/blog/llama2