from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from braces.views import LoginRequiredMixin

from accounts.mixins import UserMixin, AuthenticateMixin
from accounts.forms import LoginForm, UserForm, UserProfileForm


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


class SignupView(UserMixin, AuthenticateMixin, TemplateView):
    """ Class based view that handles the user creation.
    """
    template_name = 'accounts/signup.html'
    context = {}

    def get(self, *args, **kwargs):
        # render signup form
        self.context['form'] = UserForm()
        self.context['profileform'] = UserProfileForm()

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        data = self.request.POST
        # Load User and Profile forms
        form = UserForm(data)
        profileform = UserProfileForm(data)

        # Calls the validation method of the two model forms
        if form.is_valid() and profileform.is_valid():
            # create and save user object
            user = form.save()
            # create and save profile object
            # assign `user` as a fk of the user field in the profile object
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            # authenticate user
            self.login_user_no_password(user)

            # Redirect to dashboard
            return HttpResponseRedirect(reverse('dashboard'))

        else:
            self.context['form'] = form
            self.context['profileform'] = profileform
            return render(self.request, self.template_name, self.context)