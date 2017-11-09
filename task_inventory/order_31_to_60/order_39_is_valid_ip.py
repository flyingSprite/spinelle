import socket
import re


def is_valid_ip(ip):
    """Returns true if the given string is a well-formed IP address.

    Supports IPv4 and IPv6.
    """
    if not ip or '\x00' in ip:
        # getaddrinfo resolves empty strings to localhost, and truncates
        # on zero bytes.
        return False
    try:
        res = socket.getaddrinfo(ip, 0, socket.AF_UNSPEC,
                                 socket.SOCK_STREAM,
                                 0, socket.AI_NUMERICHOST)
        return bool(res)
    except socket.gaierror as e:
        if e.args[0] == socket.EAI_NONAME:
            return False
        raise
    return True


def vv(ip_str):
    return socket.inet_pton(socket.AF_INET6, ip_str)

def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False


print(is_valid_ip('2.2'))
print(is_valid_ip('2.2.'))
print(is_valid_ip('2.2.2.2'))
print(is_valid_ip('2::2'))
print(is_valid_ip('2:2:2'))
print(is_valid_ip('2:2:2:2:2:2:2:2'))
print('=====')
socket.inet_pton(socket.AF_INET6, '2:2:2:2:2:2:2:2')
print(checkip('2.2.033.6'))