import sys
import configparser
import ipaddress

class Config:
    def __init__(self, filename = 'tradfri.cfg'):
        self._conf = configparser.ConfigParser()
        self._conf.read(filename)

        self.coap = None
        try:
            coap = self._conf['libcoap']
            self.coap = coap.get('coap_client')
        except KeyError:
            pass
        except config.NoOptionError:
            pass
        finally:
            if self.coap is None:
                self.coap = 'coap-client'

        try:
            tf = self._conf['tradfri']
            self.identity = tf.get('identity', 'Client_identity')
            self.hubport = tf.get('hubport', '5684')
        except KeyError:
            print('Cannot find section tradfri in {}'.format(filename),
                  file=sys.stderr)
        else:
            self.hubip = ipaddress.ip_address(tf.get('hubip'))
            self.securityid = tf.get('securityid')
