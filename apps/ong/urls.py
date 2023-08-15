from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:post_id>/', views.blog_show_view, name='blog_show'),
]
