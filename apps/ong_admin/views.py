from django.shortcuts import render
from rolepermissions.decorators import has_role_decorator
from ong.forms import ProjectForm
from authentication.forms import RegisterForm
from rolepermissions.roles import assign_role
from perfil.models import VoluntaryProjectJunction
# Create your views here.

def ong_admin_view(request):
    return render(request, 'ong_admin.html') 


@has_role_decorator('admin')
def register_projects(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            try:
                project_form.save()
                messages.add_message(request, constants.SUCCESS, 'Ação criada com sucesso!')
                return render(request, 'ong_admin.html')
            except:
                messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Houve algum erro. Tente novamente mais tarde.'
                    )
                return render(request, 'ong_admin.html', {'form':project_form})


@has_role_decorator('admin')
def register_admin(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            try:
                register_form.save()

                assign_role(user, 'admin')
                messages.add_message(request, constants.SUCCESS, 'Administrador criado com sucesso!')
                return render(request, 'ong_admin.html')
            except:
                messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Houve algum erro. Tente novamente mais tarde.'
                    )
                return render(request, 'ong_admin.html', {'form':register_form})


def show_projects_to_approve(request):
    projects_to_approve = VoluntaryProjectJunction.objects.filter(approved = False)
    #TODO: nao sei oq renderizar aqui
    return render(request, 'ong_admin.html', {'projects_to_approve':projects_to_approve})
    
        
@has_role_decorator('admin')
def confirm_voluntary_participation(request):
    project = request.GET.get('project')
    voluntary = request.GET.get('voluntary')
    project_to_approve = VoluntaryProjectJunction.objects.filter(project=project).filter(voluntary=voluntary)
    try:
        project_to_approve.approved = True
        project_to_approve.save()
        messages.add_message(request, constants.SUCCESS, 'Projeto aprovado com sucesso!')
    except:
        messages.add_message(
            request, 
            constants.ERROR, 
            'Houve algum erro. Tente novamente mais tarde.'
        )
        return render(request, 'ong_admin.html')


@has_role_decorator('admin')
def register_expenses(request):
    pass