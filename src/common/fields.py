from datetime import datetime

from flask import abort

from core import ma


class DateTime(ma.DateTime):
    def _serialize(self, value, *args, **kwargs):
        if isinstance(value, str):
            try:
                date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
                return date
            except:
                abort(422, "Invalid date format. Should be YYYY-MM-DD HH:MM:SS.MS")
        return str(value)
