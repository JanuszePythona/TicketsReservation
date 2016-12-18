from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.template import RequestContext


def register(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST, prefix='user')
        # upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid():  # * upf.is_valid():
            # uf.cleaned_data['password']= make_password(uf.cleaned_data['password'])
            user = uf.save()
            # userprofile = upf.save(commit=False)
            # userprofile.user = user
            # userprofile.save()
            return render(request, 'registration/login.html')
    else:
        uf = UserCreationForm(prefix='user')
        # upf = UserProfileForm(prefix='userprofile')
    return render(request, 'registration/registration_form.html',
                              dict(userform=uf, context_instance=RequestContext(request)))
    # return render_to_response('register.html',
    # dict(userform=uf, userprofileform=upf), context_instance=RequestContext(request))


@login_required
def user_home(request):
    return render(request, 'user_home.html')
