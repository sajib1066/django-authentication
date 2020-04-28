from django.urls import path
from .views import signin, signup, signout

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout')
]