from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.urls import reverse
from .choices import Categories, Regions

class NewsBaseModel(models.Model):
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Last Updated'), auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField()
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        unique_together = (('created_at', 'slug'), )
        abstract = True

    def __str__(self):
        return self.title

class TextNewsModel(NewsBaseModel):
    category = models.CharField(
        _("Category"), 
        max_length=14, 
        choices=Categories.choices,
        db_index=True
    )
    region = models.CharField(
        _("Region"), 
        max_length=14, 
        choices=Regions.choices,
        db_index=True
    )
    cover_img  = models.ImageField(_("Cover photo"), upload_to='cover_imgs/')
    body = models.TextField(_("Body"))
    tags = TaggableManager()

    # def get_absolute_url(self):
    #     return reverse('news:text-detail', args=[
    #         self.created_at.year,
    #         self.created_at.month,
    #         self.created_at.day,
    #         self.slug
    #     ])
    

class AudioNewsModel(NewsBaseModel):
    audio = models.FileField(upload_to='audio/')