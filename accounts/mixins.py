from annoying.functions import get_object_or_None

from .models import Profile

class UserMixin(object):

    def get_profile(self):
        """ Method that will retrieve the profile object
            which contains the additional data of the
            authenticated user.
        """
        return get_object_or_None(Profile, user=self.request.user)
