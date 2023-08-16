from django.urls import path
from . import views

urlpatterns = [
    path('', views.ong_admin_view, name='ong_admin'),
    path('/approve/<int:junction_id>', views.confirm_voluntary_participation, name='approve_participation'),
    path('/update_expense/<int:id>', views.update_expenses_per_project, name='update_project_expense'),
]