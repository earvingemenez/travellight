from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from braces.views import LoginRequiredMixin

from .mixins import UserMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    """ Class based view for user dashboard
    """
    template_name = 'accounts/dashboard.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class UserProfileView(LoginRequiredMixin, UserMixin, TemplateView):
    """ Class based view for user profile
    """
    template_name = 'accounts/user_profile.html'
    context = {}

    def get(self, *args, **kwargs):
        # Get user profile data
        self.context['profile'] = self.get_profile()

        return render(self.request, self.template_name, self.context)