"""
    Explain: This module provide an abstract interface to work with Tor Service. This can be used as a proxy for Downloader
"""
import logging
import os
import sys
import traceback
from requests import Session
from torrequest import TorRequest

# UTILITY FUNCTION
def print_exception():
    # Print error message in try..exception
    exec_info = sys.exc_info()
    traceback.print_exception(*exec_info)

class TorManager():
    port = 9050
    ctrl_port = 9051
    password = None
    host = '127.0.0.1'
    def __init__(self, host=None, port=None, ctrl_port=None, password=None):
        if port:
            self.port = port
        if ctrl_port:
            self.ctrl_port = ctrl_port
        if password:
            self.password = password
        if host:
            self.host = host
    
    def reset_tor_IP(self):
        """Change Tor IP"""
        try:
            # with TorRequest(proxy_port=self.port, ctrl_port=self.ctrl_port, password=self.password) as tr:
            with TorRequest() as tr:
                tr.reset_identity()
        except:
            print_exception()
            logging.error("Can't reset Tor Proxy. Tor Service might not be running")

            
    def apply_tor_proxy(self, session):
        """Apply Tor Proxy for requests sessions"""
        session.proxies = {'http':  f'socks5://{self.host}:{self.port}',
                        'https': f'socks5://{self.host}:{self.port}'}
        return session
    
    def apply_tor_proxy_for_firefox(self, firefox_profile):
        """Apply Tor Proxy for Firefox driver"""
        fp = firefox_profile
        PROXY_HOST = self.host
        PROXY_PORT = self.port
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.https",PROXY_HOST)
        fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl",PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))  
        fp.set_preference("network.proxy.ftp",PROXY_HOST)
        fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))   
        fp.set_preference("network.proxy.socks",PROXY_HOST)
        fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))


# MODULE TEST
if __name__ == "__main__":
    tor = TorManager()
    session = Session()
    tor.apply_tor_proxy(session) 
    response = session.get('http://ipecho.net/plain')
    print("My Original IP Address:", response.text)

    tor.reset_tor_IP()  # Reset Tor
    response = session.get('http://ipecho.net/plain')
    print("New Ip Address", response.text)
    session.close()