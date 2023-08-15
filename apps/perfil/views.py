from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
from rolepermissions.decorators import has_role_decorator


def index_view(request):
    user = request.user
    return render(request, 'index.html', {'username':user.username, 'email':user.email})


def voluntary_view(request):
    user = request.user

    return render(request, 'voluntary.html', {'is_voluntary': user.is_voluntary})


def supporter_view(request):
    user = request.user

    return render(request, 'supporter.html', {'is_supporter': user.is_supporter})


@has_role_decorator('voluntary')
def project_registration(request):
    if request.method == 'GET':
        return render(request, 'voluntary.html')

