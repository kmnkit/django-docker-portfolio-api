import json
from django.core.exceptions import ImproperlyConfigured

secret_file = "secret.json"

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except Exception:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
