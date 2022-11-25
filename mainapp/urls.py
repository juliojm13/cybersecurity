from django.urls import path
from .views import index_view, login, logout

app_name = "mainapp"
urlpatterns = [
    path('', index_view, name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]
