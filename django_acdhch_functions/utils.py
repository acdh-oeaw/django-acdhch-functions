import functools
import requests
import os

from django.conf import settings


@functools.cache
def get_impressum() -> str:
    base_url = getattr(settings, "ACDH_IMPRINT_URL", "https://imprint.acdh.oeaw.ac.at/")
    redmine_id = getattr(settings, "REDMINE_ID", os.get("SERVICE_ID", ""))

    r = requests.get(f"{base_url}{redmine_id}")

    if r:
        return r.text
    else:
        return """
        One of our services is currently not available. Please try it later or write
        an email to acdh@oeaw.ac.at; if you are service provide, make sure that you
        provided ACDH_IMPRINT_URL and REDMINE_ID.
        """
