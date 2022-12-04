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
def diagnostic(request, pk):
    context = {
        'pk': pk
    }
    if request.method == 'POST':
        organization = Organisation.objects.get(pk=pk)

        gr = int(request.POST['gr_1']) + int(request.POST['gr_2']) + int(request.POST['gr_3']) + int(
            request.POST['gr_4']) + int(request.POST['gr_5']) + int(request.POST['gr_6']) + int(
            request.POST['gr_7']) + int(request.POST['gr_8']) + int(request.POST['gr_9']) + int(
            request.POST['gr_10']) + int(request.POST['gr_11']) + int(request.POST['gr_12']) + int(
            request.POST['gr_13']) + int(request.POST['gr_14'])

        ga = int(request.POST['ga_1']) + int(request.POST['ga_2']) + int(request.POST['ga_3']) + int(
            request.POST['ga_4']) + int(request.POST['ga_5']) + int(request.POST['ga_6']) + int(
            request.POST['ga_7']) + int(request.POST['ga_8']) + int(request.POST['ga_9']) + int(
            request.POST['ga_10']) + int(request.POST['ga_11']) + int(request.POST['ga_12']) + int(
            request.POST['ga_13']) + int(request.POST['ga_14']) + int(request.POST['ga_15'])

        gia = int(request.POST['gia_1']) + int(request.POST['gia_2']) + int(request.POST['gia_3']) + int(
            request.POST['gia_4']) + int(request.POST['gia_5']) + int(request.POST['gia_6']) + int(
            request.POST['gia_7']) + int(request.POST['gia_8']) + int(request.POST['gia_9']) + int(
            request.POST['gia_10']) + int(request.POST['gia_11']) + int(request.POST['gia_12']) + int(
            request.POST['gia_13']) + int(request.POST['gia_14']) + int(request.POST['gia_15']) + int(
            request.POST['gia_16']) + int(request.POST['gia_17'])

        gav = int(request.POST['gav_1']) + int(request.POST['gav_2']) + int(request.POST['gav_3']) + int(
            request.POST['gav_4']) + int(request.POST['gav_5']) + int(request.POST['gav_6']) + int(
            request.POST['gav_7']) + int(request.POST['gav_8']) + int(request.POST['gav_9']) + int(
            request.POST['gav_10']) + int(request.POST['gav_11']) + int(request.POST['gav_12']) + int(
            request.POST['gav_13']) + int(request.POST['gav_14']) + int(request.POST['gav_15']) + int(
            request.POST['gav_16'])

        cea = int(request.POST['cea_1']) + int(request.POST['cea_2']) + int(request.POST['cea_3']) + int(
            request.POST['cea_4']) + int(request.POST['cea_5']) + int(request.POST['cea_6']) + int(
            request.POST['cea_7']) + int(request.POST['cea_8']) + int(request.POST['cea_9']) + int(
            request.POST['cea_10']) + int(request.POST['cea_11']) + int(request.POST['cea_12'])

        iic = int(request.POST['iic_1']) + int(request.POST['iic_2']) + int(request.POST['iic_3']) + int(
            request.POST['iic_4']) + int(request.POST['iic_5']) + int(request.POST['iic_6']) + int(
            request.POST['iic_7']) + int(request.POST['iic_8']) + int(request.POST['iic_9']) + int(
            request.POST['iic_10']) + int(request.POST['iic_11']) + int(request.POST['iic_12']) + int(
            request.POST['iic_13'])

        ri = int(request.POST['gde_1']) + int(request.POST['gde_2']) + int(request.POST['gde_3']) + int(
            request.POST['gde_4']) + int(request.POST['gde_5']) + int(request.POST['gde_6']) + int(
            request.POST['gde_7']) + int(request.POST['gde_8']) + int(request.POST['gde_9']) + int(
            request.POST['gde_10']) + int(request.POST['gde_11']) + int(request.POST['gde_12']) + int(
            request.POST['gde_13']) + int(request.POST['gde_14']) + int(request.POST['gde_15']) + int(
            request.POST['gde_16'])

        gde = int(request.POST['gde_1']) + int(request.POST['gde_2']) + int(request.POST['gde_3']) + int(
            request.POST['gde_4']) + int(request.POST['gde_5']) + int(request.POST['gde_6']) + int(
            request.POST['gde_7']) + int(request.POST['gde_8']) + int(request.POST['gde_9']) + int(
            request.POST['gde_10']) + int(request.POST['gde_11']) + int(request.POST['gde_12']) + int(
            request.POST['gde_13']) + int(request.POST['gde_14']) + int(request.POST['gde_15']) + int(
            request.POST['gde_16']) + int(request.POST['gde_17'])

        cp = int(request.POST['cp_1']) + int(request.POST['cp_2']) + int(request.POST['cp_3']) + int(
            request.POST['cp_4']) + int(request.POST['cp_5']) + int(request.POST['cp_6']) + int(
            request.POST['cp_7']) + int(request.POST['cp_8']) + int(request.POST['cp_9']) + int(
            request.POST['cp_10']) + int(request.POST['cp_11']) + int(request.POST['cp_12']) + int(
            request.POST['cp_13']) + int(request.POST['cp_14']) + int(request.POST['cp_15']) + int(
            request.POST['cp_16']) + int(request.POST['cp_17']) + int(request.POST['cp_18']) + int(
            request.POST['cp_19'])

        gpc = int(request.POST['gpc_1']) + int(request.POST['gpc_2']) + int(request.POST['gpc_3']) + int(
            request.POST['gpc_4']) + int(request.POST['gpc_5']) + int(request.POST['gpc_6']) + int(
            request.POST['gpc_7']) + int(request.POST['gpc_8']) + int(request.POST['gpc_9']) + int(
            request.POST['gpc_10']) + int(request.POST['gpc_11']) + int(request.POST['gpc_12']) + int(
            request.POST['gpc_13']) + int(request.POST['gpc_14']) + int(request.POST['gpc_15']) + int(
            request.POST['gpc_16'])

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
            id_organization=organization,
        )
        return HttpResponseRedirect(reverse('mainapp:results', kwargs={'pk': pk}))
    return render(request, 'mainapp/diagnostic.html', context)


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
            same_org = Organisation.objects.filter(org_name=request.POST['org_name'])
            context = {
                'same_obj': same_org,
                'new_obj': request.POST['org_name']
            }
            if not same_org:
                organization_form.save()
            else:
                return render(request, 'mainapp/checking_org.html', context)
            return render(request, 'mainapp/checking_org.html', context)
        #     # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            # return super().get(request, *args, **kwargs)
            return HttpResponse('Неверно заполненная форма. Попробуйте еще раз.')

    return render(request, 'mainapp/organizationform.html', context)


@login_required
def results(request, pk):
    data = Diagnostic.objects.filter(id_organization=pk)
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
