from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.template import RequestContext


def register(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST, prefix='user')
        if uf.is_valid():
            uf.save()

            return render(request, 'registration/login.html')
    else:
        uf = UserCreationForm(prefix='user')
    return render(request, 'registration/registration_form.html',
                  dict(userform=uf, context_instance=RequestContext(request)))
