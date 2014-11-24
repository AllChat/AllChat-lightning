# -*- coding: utf-8 -*-
from webob.dec import wsgify


def Middleware(object):
    def __init__(self, app):
        self.app = app

    @wsgify
    def __call__(self, req):
        response = self.process_request(req)
        if response:
            return response
        response = req.get_response(self.app)
        return self.process_response(response)

    def process_request(self, req):
        return None

    def process_response(self, resp):
        return resp

    @classmethod
    def factory(cls, global_config, **local_config):
        def _factory(app):
            return cls(app, **local_config)
        return _factory