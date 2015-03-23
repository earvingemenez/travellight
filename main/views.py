from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from braces.views import LoginRequiredMixin

from accounts.forms import LoginForm


class IndexView(TemplateView):
    """ Class based view for the index page.
    """
    template_name = 'main/index.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class LoginView(TemplateView):
    """ Class based view that handles the user authentication. this evaluates the user's
        inputted username and password and authenticate it using `LoginForm` which is an
        extension of django's AuthenticationForm.
    """
    template_name = 'accounts/login.html'
    context = {}

    def get(self, *args, **kwargs):
        # Render LoginForm to the template
        self.context['form'] = LoginForm()
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        data = self.request.POST
        form = LoginForm(data=data)

        # Calls the validation method of
        # `django.contrib.auth.forms.AuthenticationForm`
        if form.is_valid():
            # `form.get_user` is a method from
            # `django.contrib.auth.forms.AuthenticationForm`
            login(self.request, form.get_user())

            # Redirect to dashboard
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            # form is not valid meaning that username/password is invalid
            # or user doesn't not exists in the database.
            self.context['form'] = form
            return render(self.request, self.template_name, self.context)


class LogoutView(LoginRequiredMixin, View):
    """ Class based view that remove the session of the authenticated user.
    """
    def get(self, *args, **kwargs):
        # Calls django's `logout` function
        logout(self.request)
        return HttpResponseRedirect(reverse('user_login'))