from django.urls import path
from .views import login, signup, user_logout

urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', user_logout, name="logout"),   
]
