# Parslink
A simple python server/client script to turn a raspberry pi into a SteamLink-like device.

# Description
This script is intended to let you start Steam Big Picture and connect to a Parsec server from your raspberry pi. I created it because I couldn't afford a SteamLink device (I'm a broken student) and I couldn't use Nvidia GameStream because of my unsupported graphic card.
This is an extremely simple script and it's my first python project so please don't be rude.

**BE SURE TO RUN IT WITH PYTHON 3**

# Get started
Just clone or download this rep to get started.

```bash
git clone https://github.com/lyghtnox/parslink
```
Copy the server files on your Windows machine and the client files on the raspberry pi.

Install the dependencies:

On the client:
```bash
pip install requests
```

On the server:
```bash
pip install psutil
```

# Configuration
Edit the server.conf and client.conf to match your own configuration. Commented lines aren't mandatory, you can let them as they are or delete them. Be sure to uncomment them if you edit them.

```
ParsecServerID = 	#Your Parsec server ID
IP = 	#Your server IP
Password = 	#A password to be a bit secured
```

Now you are ready to go! Just be sure to start the server BEFORE the client.
I advice you to run the server and Parsec on startup (Google is your friend).

# TLS
I've added a TLS support if you want to add a security to the communications (wich you really should, go look at MITM attacks you will be surprised of how easy it is).

You can find how to generate the files [here](https://gist.github.com/fntlnz/cf14feb5a46b2eda428e000157447309).
Once you've done that, copy your rootCA file on the raspberry and add its path to the client.conf file under the `RootCA` option.
The key file and the certificate have to be on your server, add them to the server.conf file.

# Advanced usage
The server.py file is just a simple http server. That means that you can use another software to send the http request. Here is an example for cURL:

```bash
curl -X POST -H "x-access: <Your password>" http://<Server IP>:<Port>/start_game
```

Default port is 4242.
