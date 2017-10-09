import logging
import requests
import os

try:
    from alerta.plugins import app  # alerta >= 5.0
except ImportError:
    from alerta.app import app  # alerta < 5.0
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.rest')

POSTBACK_URL = app.config.get('POSTBACK_URL') or os.environ.get('POSTBACK_URL')
POSTBACK_AUTH_CODE = app.config.get('POSTBACK_AUTH_CODE') or os.environ.get('POSTBACK_AUTH_CODE')


class RestPublisher(PluginBase):
    def __init__(self, name=None):
        super(RestPublisher, self).__init__(name)

    def pre_receive(self, alert):
        return alert

    def post_receive(self, alert):
        return alert

    def status_change(self, alert, status, text):
        data = {
            "resource": alert.resource,
            "id": alert.id,
            "status": status,
            "customer": alert.customer
        }

        headers = {"X-ApiKey-Auth": POSTBACK_AUTH_CODE}

        r = requests.post(POSTBACK_URL, json=data, headers=headers)

        LOG.info('Processed postback with status code %s', r.status_code)

        return
