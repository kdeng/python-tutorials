#!/usr/bin/env bash

docker run --rm -it -v $(PWD):/app -w /app python:3.6.4 sh -c "/app/build.sh"
