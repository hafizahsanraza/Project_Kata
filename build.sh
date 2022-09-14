#!/usr/bin/env bash

## simplest building structure

set -e

printf "LOG - running docker build\n"

# building service
docker build -t kata-service:v1.0 ./kata_service/.

# building ui
docker build -t kata-ui:v1.0 ./kata-react/.

