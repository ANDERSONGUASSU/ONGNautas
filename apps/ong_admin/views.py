from django.shortcuts import render
from rolepermissions.decorators import has_role_decorator
from rolepermissions.roles import assign_role
from django.shortcuts import get_object_or_404

from ong.forms import ProjectForm
from authentication.forms import RegisterForm
from perfil.models import VoluntaryProjectJunction
from .forms import ExpensesForm
from ong.models import Project
# Create your views here.

def ong_admin_view(request):
    active_projects = Project.objects.filter(is_active=True)
    voluntary_projects_to_approve = VoluntaryProjectJunction.objects.filter(approved=False)
    return render(request, 'ong_admin.html', {'active_projects':active_projects, 
                                              'voluntary_projects_to_approve':voluntary_projects_to_approve}) 


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
def confirm_voluntary_participation(request, junction_id):
    project_to_approve = get_object_or_404(VoluntaryProjectJunction, id=junction_id)
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
    if request.method == 'POST':
        expenses_form = ExpensesForm(request.POST)
        if expenses_form.is_valid():
            try:
                expenses_form.save()
                messages.add_message(request, constants.SUCCESS, 'Despesa registrada com sucesso!')
                return render(request, 'ong_admin.html')
            except:
                messages.add_message(
                    request, 
                    constants.ERROR, 
                    'Houve algum erro. Tente novamente mais tarde.'
                )
    return render(request, 'ong_admin.html')


@has_role_decorator('admin')
def update_expenses_per_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    try:
        project.amount_spent = request.GET.get('total')
        project.save()
        messages.add_message(request, constants.SUCCESS, 'Despesa atualizada com sucesso!')
        return render(request, 'ong_admin.html')
    except:
        messages.add_message(
            request, 
            constants.ERROR, 
            'Houve algum erro. Tente novamente mais tarde.'
        )
    return render(request, 'ong_admin.html')