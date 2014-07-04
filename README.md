dockerCS
========

Utility to build and run docker images containing Circuitscape.

## Building the Docker image

- Configure if required:
-- user and group ids mentioned in `Dockerfile`
-- version number and image name mentioned in `Makefile`
- Run `make image`

## Running Circuitscape from the Docker image
- Place configuration files and data files in a folder
- Change directory to the above mentioned folder
- Run `<path>/docker_csrun.py <circuitscape config file>`
