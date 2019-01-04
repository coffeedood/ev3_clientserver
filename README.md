# ev3_clientserver

This project demonstrates running client and server code on the mindstorm/brickpi ev3

The client.py listens for a button press and sends messages "stop" and "go" over port 8089

The server.py listens for messages "stop" and "go" on port 8089 and turns a motor in response

The colors.py is similar to server.py but it changes colors on the mindstorm
