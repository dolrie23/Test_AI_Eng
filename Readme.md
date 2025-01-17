# Test Case - Daniel Dolrie Simanjuntak
This repository contains Yolov8 nano model deployed in docker-cpu that allows user to run 
my model in CLI and return the path of detected image.

## Introduction
The goal of this project is to implement:
1. Use of docker to make model containerized and ready for deployment
2. Predict my model using CLI from docker
3. Run on CPU

## Table of Contents
- **[Introduction](#Introduction)**
- **[Steps](#Step)**
- **[Answers](#Answers)**

## Installation Step
### Clone this Repository to your local
If you have git, use this code:
```shell
git clone https://github.com/dolrie23/Test_AI_Eng.git
cd Dicoding-Clustering-and-Classification-Final-Project
```

### Run this command on terminal
#### To create the docker image file
```shell
docker build -t yolov8-inference_CLI .
```
#### To run the docker image 
```shell
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output yolo-inference_CLI \
    --input /app/input/input.jpg --output /app/output/output.jpg
```

## To run on GPU?
I'm new to docker but my finding over the internet told me to do this:
- Create new Dockerfile and copy and paste below docker code to new dockerfile
```shell
FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip
RUN pip install ultralytics

COPY . /app

CMD ["python", "inference_CLI.py"]
```

### Run Yolov8 straight from CLI
To run code straight from CLI without docker. Make sure ultralytics and opencv is in the virtual environment
```shell
python -m virtualenv [venv_name]
pip install ultralytics
pip install opencv-python
python inference_CLI.py --input [$Your_Image_Path].jpg --output [$Your_Output_Image_Path].jpg
```

Answer of the questions:
1. I create solution by :
- create my git repository
- choose yolov8 nano model to optimize memory usage on my local
- build code that compatible for image and videos with reference from internet
- create requirements.txt that contains required libraries
- find reference on the internet of which base image that contain all that I need for running YOLOv8
- run the docker image
2. The base image that I select is python 3.9 slim version, but in this scenario I can't run the dockerfile
due to my low PC memory. Another base image that I would suggest python 3.9-alpine because it's lightweight on docker image.
Then, it would significantly reduce the docker image size. 
3. I can't test the yolov8 nano model against my images and videos due to limited memory on my pc 
and the need for docker for ultralytics is very high. But I got the solution by running the CLI manually from my local.
4. To optimize my solution, I will use ONNX model to reduce the memory usage on my model. And for deployment I will 
optimize the image for lightweight and scalable runtime.
