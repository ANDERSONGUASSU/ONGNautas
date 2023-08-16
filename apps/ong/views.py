from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm, RegisterNewsletterForm, CommentsForm
from rolepermissions.decorators import has_role_decorator
from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.contrib.messages import constants


def blog_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        three_posts = posts[:3]
        return render(request, 'blog.html', {'posts': three_posts})


def blog_show_view(request, post_id):
    posts = get_object_or_404(Post.objects.filter(id=post_id))
    return render(request, 'blog_show.html', {'posts': posts})


def home_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts})



@has_role_decorator('Admin')
def create_posts(request):
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('blog'))

            return render(request, 'blog.html')
        case 'POST':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_form.save() 
                messages.add_message(request, constants.SUCCESS, 'Post criado com sucesso!')



def show_posts_per_category(request):
    sel_posts = Post.objects.filter(category = request.POST.get('category'))
    return render(request, 'blog.html', {'sel_posts':sel_posts})


@has_role_decorator('Admin', 'Voluntary', 'Supporter')
def make_comment(request):
    if request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            try:
                comment_form.save()
                #nao sei oque retornar aqui
                return render(request, '.html')
            except:
                messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Houve algum erro. Tente novamente mais tarde.'
                    )


def newsletter_register(request):
    register_news_user = RegisterNewsletterForm()

    if register_news_user.is_valid():
        try:
            register_news_user.save()

            messages.add_message(request, constants.INFO, message)
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso!')

            return render(request, 'home.html')

        except:
            messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Erro interno do sistema. Tente novamente mais tarde.'
                    )

    return render(request, 'home.html')