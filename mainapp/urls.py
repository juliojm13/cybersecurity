from django.urls import path
from .views import index_view, login, logout, diagnostic, results, dashboard, organisation, organisation_form

app_name = "mainapp"
urlpatterns = [
    path('', index_view, name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('diagnostic/<int:pk>', diagnostic, name="diagnostic"),
    path('organization/', organisation, name="organisation"),
    path('organizationform/', organisation_form, name="orgform"),
    path('results/<int:pk>', results, name="results"),
    path('dashboard/<int:pk>/', dashboard, name="dashboard"),
]
