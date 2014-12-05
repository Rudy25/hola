from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from usuarioperfil.models import Userprofile
from usuarioperfil.forms import UserprofileForm, SignUpForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def main(request):
    return render_to_response('main.html', {}, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            # Save new user attributes
            user.save()
            return HttpResponseRedirect(reverse('login'))  # Redirect after POST
    else:
        form = SignUpForm()
    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))

#@method_decorator(permission_required('usuarioperfil.list_zet'))
class UserprofileCreate(CreateView):
    model = Userprofile
    form_class = UserprofileForm

    def dispatch(self, *args, **kwargs):
        return super(UserprofileCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.useri = self.request.user
        self.object.save()
        return redirect("list_user")

@login_required()
def home(request):
    return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))


class UserprofileList(ListView):
    model =   Userprofile

def UserDetail(request, Userprofile_id):
    useri = get_object_or_404(Userprofile, id = Userprofile_id)
    return render(request, 'usuarioperfil/userprofile_detail.html', {'useri':useri})

class UserprofileUpdate(UpdateView):
    model = Userprofile
    form_class = UserprofileForm
    @method_decorator(permission_required('usuarioperfil.change_app'))
    def dispatch(self, *args, **kwargs):
        return super(UserprofileUpdate, self).dispatch(*args, **kwargs)


class UserUpdate(UpdateView):
    model = User
    form_class = SignUpForm
    def dispatch(self, *args, **kwargs):
        return super(UserUpdate, self).dispatch(*args, **kwargs)

class UserprofileDelete(DeleteView):
    model = Userprofile
    @method_decorator(permission_required('usuarioperfil.delete_app'))
    def dispatch(self, *args, **kwargs):
        return super(UserprofileDelete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        # To do this because the success_url class variable isn't reversed...
        return reverse('list_user')
