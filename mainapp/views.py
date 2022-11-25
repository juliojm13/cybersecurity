from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import RedirectView, TemplateView
from django.contrib import auth


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


index_view = IndexView.as_view()


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password,
                                 backend='django.contrib.auth.backends.ModelBackend')
        print('user', user)
        if user and user.is_active:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:

                return HttpResponseRedirect(reverse('mainapp:index'))

    content = {'title': 'login', 'next': next}
    return render(request, 'mainapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
