# Exercise-Viewer

A very simple Flask web application used by OpenStax researchers to view OpenStax Exercises in a more user friendly way.

## How to Use

The `exercice-viewer` is currently deployed at:

    https://abtpvg7emg.execute-api.us-east-1.amazonaws.com/dev/<exercise_id>


Replace `<exercise_id>` with the exercise id in Exercises.

Example:

https://abtpvg7emg.execute-api.us-east-1.amazonaws.com/dev/12345


## Development with Docker

You can use Docker to quickly get the application running on your machine.


### Install Docker and Docker Compose

> Follow the instructions on the [Docker website](https://docs.docker.com/install/).

### Build and run the docker container

    $ docker-compose up

## Deploying to AWS Lambda

> Note: You'll want to make sure you have your AWS credentials file at `~/.aws/credentials` filled out for deployment user `exercise-viewer`

The [Zappa](https://github.com/Miserlou/Zappa) project is used to package up the application and deploy it to AWS Lambda.

For deployment to AWS Lambda you'll want to run commands locally so the recommended method is to create a virtualenv and install the deploy requirements locally.

### Create a virtualenv

    $ python3 -m venv .venv

### Activate the virualenv

    $ source .venv/bin/activate

### Install the deploy requirements

    $ pip install -r requirements-deploy.txt

### Deploy the application

    $ zappa deploy dev
