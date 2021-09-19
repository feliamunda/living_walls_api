from django.utils.translation import gettext as _
from django.db import models

class Asset(models.Model):
    name = models.CharField(_("name"), max_length=70)
    bundle = models.FileField(_("bundle"), upload_to="bundles")