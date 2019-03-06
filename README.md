# AulaCommunication Server
The server needed to run the AulaCommunication Client

# Get started
## Run the server locally
1. Clone this repository
2. Run python3 main.py in the Source folder
## Run the server with docker
1. Run docker create pboehler/aulacommunivation:latest to download the server image and create a new container
2. run "docker run -it -p 33000:33000/tcp --name serverAulaeComm pboehler/aulacommunication:latest" to start the server interactive, allocate port 33000 for the new container and name it serverPi

# Help
## The command line arguments for this programm
* -p or --Port => Sets up the port for the session (default is port 33000 if no arg is parsed)
* -h or --help => Opens the help section of the proheam

# Future
* The server will be put inside a docker container

