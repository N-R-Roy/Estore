from django.urls import path
from .views.index import index
from .views.login import login
from .views.signup import signup


app_name = "mstore"

urlpatterns = [
    path('', login, name="login"),
    path('signup/', signup, name="signup"),
    path('index/', index, name="index"),
]

