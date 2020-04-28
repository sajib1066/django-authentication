from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='signin')
def home(request):
    usr = request.user
    user = User.objects.get(username=usr)
    print('Name:', user.first_name)
    return render(request, 'home.html')