#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull shahana2022/aws-ci-cd-project:latest
# Run the Docker image as a container
docker run -d -p 5000:5000 shahana2022/aws-ci-cd-project:latest
