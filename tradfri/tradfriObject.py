import os, sys

from tradfri import tradfriConfig

class Tradfri:
    def __init__(self, configfile = "tradfri.cfg"):
        self.config = tradfriConfig.Config(configfile)
        self._tradfriHub = 'coaps://{}:{}'.format(str(self.config.hubip),
                                                  self.config.hubport)

    def cmd(self, path, method="get", payload=None):
        uri = 'coaps://{}:{}{}'.format(self.config.hubip,
                                       self.config.hubport,
                                       path)
        if payload is not None:
            e = '-e \'{}\''.format(payload)
        else:
            e = ''
        return '{} -m {} -u "{}" -k "{}" {} "{}"'.format(self.config.coap,
                                                         method,
                                                         self.config.identity,
                                                         self.config.securityid,
                                                         e,
                                                         uri)

    def get(self, path): 
        if os.path.exists(self.config.coap):
            result = os.popen(self.cmd(path))
        else:
            print("Command not found: " + self.config.coap, file=sys.stderr)
            sys.exit(1)

        return result.read().strip('\n')
        
    def put(self, path, payload=None):
        if os.path.exists(self.config.coap):
            result = os.popen(self.cmd(path, method="put", payload=payload))
        else:
            print("Command not found: " + self.config.coap, file=sys.stderr)
            sys.exit(1)

        return result.read().strip('\n')
