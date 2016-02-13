
from oauthlib import oauth
import base64

class AuthHelper(object):

    def __init__(self, consumer_id, consumer_secret):
        self.consumer_id = consumer_id
        self.consumer_secret = consumer_secret

        self.consumer = oauth.OAuthConsumer('', self.consumer_secret) # consumer id do not needed
        self.sha = oauth.OAuthSignatureMethod_HMAC_SHA1()

    def signature(self, http_method, http_url, parameters, full=True):
        request = oauth.OAuthRequest(http_method=http_method, http_url=http_url, parameters=parameters)
        '''key, raw = self.sha.build_signature_base_string(request, self.consumer, None)
        print key
        print raw
        '''
        _sig = self.sha.build_signature(request, self.consumer, None)
        if full:
            return 'Ticketman %s:%s' % (self.consumer_id, _sig)
        else:
            return _sig

    ''' HTTPHeader format: 'Ticketman-Authenticate': 'Ticketman consumer:JsRfhb9gb9qP1SzOiqM3MBNpHJA=' '''
    def makeSignatureHeader(self, http_method, http_url, parameters):
        return ('Ticketman-Authenticate', self.signature(http_method, http_url, parameters))

    def makeBasicAuthHeader(self, user='dev', pwd='123'):
        base64string = base64.encodestring('%s:%s' % (user, pwd)).replace('\n', '')
        return ("Authorization", "Basic %s" % base64string) 


