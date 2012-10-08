import socket

_log_enabled = False

def _module_log(msg):
    global _log_enabled
    if _log_enabled:
        print msg

def _set_module_log_enable(enable):
    global _log_enabled
    _log_enabled = enable


class PianodInterface:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port, username, password):
        self._sock.connect((host, port))
        msg = 'user %s %s'%(username,password)
        sent = 0
        while sent != len(msg):
            ct = self._sock.send(msg[sent:])
            sent += ct
            if ct == 0:
                raise RuntimeError("socket connection failed")

        _module_log('connected')

    def disconnect(self):
        self._sock.close()




    

