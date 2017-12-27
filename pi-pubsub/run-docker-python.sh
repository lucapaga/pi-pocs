#!/bin/bash

docker run -d --restart always --device /dev/gpiomem:/dev/gpiomem:rw --device /dev/mem:/dev/mem:rw -p"5000:5000" lucapaga/angular-leg-mgr-python:0.0.2

