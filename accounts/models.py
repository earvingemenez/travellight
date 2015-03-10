from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ Extension of `User` model which contains additional
        fields for the User object.
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
        return "%s" % self.user.get_full_name()