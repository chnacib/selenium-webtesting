#!/bin/bash
docker network create testing
docker pull selenium/standalone-chrome
docker run --name selenium --network testing -dp 4444:4444 selenium/standalone-chrome
docker build -t test-script .
docker run --network testing test-script
