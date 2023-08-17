from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from authentication.validators import no_whitespaces
from authentication.models import User
from django.utils import timezone


class Project(models.Model):

    title = models.CharField(_('title'), max_length=24, blank=False)
    short_description = models.CharField(_('short description'), max_length=64, blank=False)
    description = models.TextField(_('description'))
    address = models.CharField(_('address'), max_length=50)
    image = models.ImageField(_('image'), upload_to='projects')
    is_active = models.BooleanField(_('is active'), default=True)
    amount_spent = models.DecimalField(_('amount spent'), max_digits=6, decimal_places=2, default=0.0)
    amount_expected = models.DecimalField(_('amount spent'), max_digits=6, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    CATEGORY_CHOICES = [('F', 'Forest'), ('W', 'Water'), ('A', 'Air'), ('L', 'Animals')]

    title = models.CharField(_('title'), max_length=100, blank=False)
    text = models.TextField(_('text'), blank=False)
    category = models.CharField(_('category'), max_length=1, choices=CATEGORY_CHOICES, blank=False)
    image = models.ImageField(_('image'), upload_to='blog_posts')
    date = models.DateField(_('date'), default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.autor) + ' | ' + str(self.date) + ' | ' + self.title



class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField(_('date'), default=timezone.now)

    def __str__(self) -> str:
        return self.autor + ' | ' + self.comment + ' | ' +  self.date


class NewsletterUser(models.Model):
    email = models.EmailField(
            _('email address'),
            unique=True,
            blank=False,
            validators=[no_whitespaces])

    date = models.DateField(_('date'), default=timezone.now)

    def __str__(self):
        return self.email + '  |  ' + str(self.date)
