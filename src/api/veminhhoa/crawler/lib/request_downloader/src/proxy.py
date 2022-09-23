import random

PROXY_LIST = [
	'104.129.50.128:8800',
	'104.223.115.43:8800',
	'208.100.18.125:8800',
	'208.100.18.77:8800',
	'69.147.248.211:8800',
	'69.162.159.227:8800',
	'69.147.248.154:8800',
	'104.129.50.227:8800',
	'107.150.0.170:8800',
	'104.129.50.198:8800',
	'69.147.248.145:8800',
	'69.162.159.67:8800',
	'107.150.0.161:8800',
	'69.162.159.149:8800',
	'107.150.0.226:8800',
	'104.223.115.196:8800',
	'104.129.50.154:8800',
	'104.129.50.189:8800',
	'104.223.115.225:8800',
	'104.223.115.179:8800',
	'69.147.248.37:8800',
	'69.162.159.170:8800',
	'208.100.18.2:8800',
	'107.150.0.142:8800',
	'208.100.18.106:8800'
]

def apply_proxy(session):
        """Apply proxy for session"""
        global PROXY_LIST
        proxy = random.choice(PROXY_LIST)
        session.proxies = {'http':  f'socks5://{proxy}',
                        'https': f'socks5://{proxy}'}
        return session

def apply_proxy_for_firefox(firefox_profile):
    """Apply Proxy for Firefox driver"""
    global PROXY_LIST
    proxy = random.choice(PROXY_LIST)
    proxy_host = proxy.split(':')[0]
    proxy_port = proxy.split(':')[1]

    fp = firefox_profile
    PROXY_HOST = proxy_host
    PROXY_PORT = proxy_port
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
