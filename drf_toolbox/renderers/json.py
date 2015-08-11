from __future__ import absolute_import, unicode_literals
from calendar import timegm
from datetime import datetime
from functools import wraps
from rest_framework import renderers
from rest_framework.utils import encoders
import json


class JSONEncoder(encoders.JSONEncoder):
    """json.JSONEncoder subclass which understands how to serialize
    some non-standard objects.
    """
    def default(self, obj):
        """Serialize `obj` into a UNIX timestamp if it is a datetime
        object, and call the superclass method otherwise.
        """
        if isinstance(obj, datetime):
            return timegm(obj.utctimetuple())
        return super(JSONEncoder, self).default(obj)


class JSONRenderer(renderers.JSONRenderer):
    """Renderer which serializes to JSON."""
    encoder_class = JSONEncoder
