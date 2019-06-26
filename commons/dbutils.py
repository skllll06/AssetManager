# -*- coding: utf-8 -*-
from django.db import connection


def exec_query(sqltext):
    with connection.cursor() as c:
        c.execute(sqltext)
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in c.description]
        return [
            dict(zip(columns, row))
            for row in c.fetchall()
        ]
