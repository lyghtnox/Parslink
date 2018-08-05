#!/usr/bin/python3
import requests
import getopt
import sys
import subprocess
import configparser

#Disable warning for no subjectAltName in TLS certificate
#import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def main(argv):
    usage = "Usage: client.py \nJust launch it"
    config=configparser.ConfigParser()
    config.read("client.conf")

#Arguments handling

    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()

    if len(args) == 0:
        startGame(config)
        subprocess.Popen(["parsec", "server_id={}".format(config['Core']['ParsecServerID'])])
        sys.exit()
    else:
        print(usage)

def startGame(config):
    core = config['Core']
    headers = {'x-access': core['Password']}  #Provides password

    try:
        r = requests.post('https://{}:{}/start_game'.format(core.get('IP'), core.get('Port', '4242')), verify=config['TLS'].get('RootCA', False), headers=headers)
    except requests.RequestException as err:
        print("An error occured:", err)
        sys.exit(2)

#Warn user if an incorrect password is submitted       

    if r.status_code == 200:
        print("Steam started!")
    elif r.status_code == 403:
        print("Invalid password")
    else:
        print("Unexpected status code returned:", r.status_code)


if __name__ == "__main__":
   main(sys.argv[1:])
