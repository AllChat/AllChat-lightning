# -*- coding: utf-8 -*-
from webob import Response
from lightning.middleware.base import Middleware
from lightning import HTTP_CODE
from lightning.db.sql import query_userauth_by_account

class auth(Middleware):
    def process_request(self, req):
        if "account" in req.headers and "token" in req.headers:
            token = query_userauth_by_account(req.headers["account"])
            if token == req.headers['token']:
                return None
        resp = Response(body = "Login First", status = HTTP_CODE['Unauthorized'])
        resp.headers['account'] = req.headers["account"]
        return resp

