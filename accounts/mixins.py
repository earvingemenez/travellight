from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from annoying.functions import get_object_or_None

from .models import Profile


class UserMixin(object):

    def get_profile(self):
        """ Method that will retrieve the profile object
            which contains the additional data of the
            authenticated user.
        """
        return get_object_or_None(Profile, user=self.request.user)


class AuthenticateMixin(object):
    """ Mixin class that contains methods related to User authentications
    """
    def login_user(self, username, password):
        """ Method that can be used to login user. this function requires the
            username and password.
        """
        # verify user credentials
        user = authenticate(username=username, password=password)
        # login user
        login(self.request, user)

    def login_user_no_password(self, auth_user=None):
        """ Method that can be used to login user. this function doesn't need user's
            password but it requires the user object.
        """
        auth_user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, auth_user)