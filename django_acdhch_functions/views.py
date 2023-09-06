from django.conf import settings
from django.views.generic import TemplateView

from . import utils


class Imprint(TemplateView):
    template_name = "acdhch_functions/imprint.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['imprint'] = utils.get_impressum()
        ctx["basetemplate"] = getattr(settings, "BASE_TEMPLATE", "base.html")
        return ctx
