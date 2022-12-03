from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import RedirectView, TemplateView
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import AddOrganizationForm
from .models import Diagnostic, Organisation


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


@login_required
def diagnostic(request):
    if request.method == 'POST':
        print(request.POST)
        gr = int(request.POST['gr_1']) + int(request.POST['gr_2']) + int(request.POST['gr_3']) + int(
            request.POST['gr_4'])
        ga = 30
        gia = 0
        gav = 0
        cea = 40
        iic = 0
        ri = 0
        gde = 50
        cp = 10
        gpc = 0
        total = gr + ga + gia + gav + cea + iic + ri + gde + cp + gpc
        Diagnostic.objects.create(
            gr=gr,
            ga=ga,
            gia=gia,
            gav=gav,
            cea=cea,
            iic=iic,
            ri=ri,
            gde=gde,
            cp=cp,
            gpc=gpc,
            total=total,
        )
        return HttpResponseRedirect(reverse('mainapp:results'))
    return render(request, 'mainapp/diagnostic.html')


@login_required
def organisation(request):
    data = Organisation.objects.order_by('org_name')
    context = {
        'object_list': data
    }
    return render(request, 'mainapp/organisation.html', context)


@login_required
def organisation_form(request):
    organization_form = AddOrganizationForm()

    context = {
        'organization_form': organization_form
    }
    if request.method == 'POST':
        organization_form = AddOrganizationForm(request.POST)
        if organization_form.is_valid():
            # print(request.POST['org_name'])
            # print(Organisation.objects.filter(org_name=request.POST['org_name']))
            organization_form.save()

            return HttpResponseRedirect(reverse('mainapp:organisation'))
        #     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            # return super().get(request, *args, **kwargs)
            return HttpResponse('Неверно заполненная форма. Попробуйте еще раз.')

    return render(request, 'mainapp/organizationform.html', context)


@login_required
def results(request):
    data = Diagnostic.objects.all()
    context = {
        'data': data
    }
    return render(request, 'mainapp/results.html', context)


@login_required
def dashboard(request, pk):
    data = Diagnostic.objects.get(pk=pk)
    context = {
        'object': data
    }
    return render(request, 'mainapp/dashboard.html', context)
