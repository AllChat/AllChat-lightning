# -*- coding: utf-8 -*-
from lightning.db import session
from lightning.db.model import UserAuth


def query_userauth_by_account(account):
    if account is None:
        return None
    try:
        token = session.query(UserAuth).filter(UserAuth.account == account).one()
    except Exception as e:
        return None
    else:
        return token