from django.urls import path
from .views import index_view, login, logout, diagnostic, results, dashboard, organisation

app_name = "mainapp"
urlpatterns = [
    path('', index_view, name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('diagnostic/', diagnostic, name="diagnostic"),
    path('organisation/', organisation, name="organisation"),
    path('results/', results, name="results"),
    path('dashboard/<int:pk>/', dashboard, name="dashboard"),
]
