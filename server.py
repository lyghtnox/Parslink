import subprocess
import http.server
import ssl
import psutil
import time
import configparser

def startSteam(config):
    if [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'steam' in p.info['name']]:   #Kill steam if already running
        subprocess.Popen([config['Core'].get('SteamPath', 'C:\Program Files (x86)\Steam\Steam.exe'), "-shutdown"])
        time.sleep(3)
                    
    subprocess.Popen([config['Core'].get('SteamPath', 'C:\Program Files (x86)\Steam\Steam.exe'), "-tenfoot"])    #Start Big Picture

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        global config
        if self.headers.__getitem__('x-access') == config['Core']['Password']:  #Checks for correct password
            if self.path == '/start_game':
                startSteam(config)

            self.send_response(200)
            
        else:
            print('Invalid password!')
            self.send_response(403)

        self.end_headers()

config = configparser.ConfigParser()
config.read("server.conf")

tls = config['TLS']

httpd = http.server.HTTPServer(('0.0.0.0', config['Core'].getint('Port', 4242)), MyHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=tls.get('CertFile', None), keyfile=tls.get('KeyFile', None), server_side=True)
httpd.serve_forever()
