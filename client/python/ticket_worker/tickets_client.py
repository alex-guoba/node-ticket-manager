import urllib
import urllib2
import json

import auth_helper

def tm_api():
    def wrap(function):
        def _apicall(*args, **kw):
            rsp = function(*args, **kw)
            if rsp:
                try:
                    return json.loads(rsp)
                except:
                    return rsp
        return _apicall
    return wrap

class TicketsClient(object):

    def __init__(self, host, consumer_id, consumer_secret, basicauth_user, basicauth_pwd,
            timeout=2):
        self.host = host
        self.ah = auth_helper.AuthHelper(consumer_id, consumer_secret)
        self.basicauth_user = basicauth_user
        self.basicauth_pwd = basicauth_pwd
        self.timeout = timeout

    def _make_request(self, http_method, url, parameters):
        #req = urllib2.Request(url, data=urllib.urlencode(parameters))

        # send a json-formated content to server
        req = urllib2.Request(url, json.dumps(parameters), {'Content-Type': 'application/json'})

        hk, hv = self.ah.makeSignatureHeader(http_method, url, parameters)
        req.add_header(hk, hv)
        req.get_method = lambda: http_method 

        hk, hv = self.ah.makeBasicAuthHeader(self.basicauth_user, self.basicauth_pwd)
        req.add_header(hk, hv)
        return req
    
    @tm_api()
    def assign(self, category, tid=None):
        url = self.host + '/api/tickets/assign'
        parameters = {}
        if tid:
            parameters['id'] = tid
        else:
            parameters['category'] = category
        req = self._make_request('PUT', url, parameters)
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()

    @tm_api()
    def comment(self, tid, content, kind='info'):
        url = self.host + '/api/tickets/%s/comment' % tid
        parameters = { 
                'content': content,
                'kind': kind }

        req = self._make_request('PUT', url, parameters)
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()

    @tm_api()
    def complete(self, tid):
        url = self.host + '/api/tickets/%s/complete' % tid
        req = self._make_request('PUT', url, {})
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()

    @tm_api()
    def find(self, parameters):
        url = self.host + '/api/tickets/find'
        req = self._make_request('POST', url, parameters)
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()

    @tm_api()
    def giveup(self, tid):
        url = self.host + '/api/tickets/%s/giveup' % tid
        req = self._make_request('PUT', url, {})
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()

    @tm_api()
    def new(self, title, category, content, description, owner_id='nobody', status='pending'):
        url = self.host + '/api/tickets/new'
        parameters = {
                'title': title,
                'category': category,
                'content': content,
                'description': description,
                'owner_id': owner_id,
                'status': status
                }

        req = self._make_request('POST', url, parameters)
        f = urllib2.urlopen(req, timeout=self.timeout)
        return f.read()



