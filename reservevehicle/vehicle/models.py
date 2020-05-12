from django.contrib.auth.models import User
from django.db import models



# Create your models here.
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe

from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):

    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True,max_length=100)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '>>' .join(full_path[:: -1])

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Vehicle(models.Model):

        STATUS = (
            ('True', 'Evet'),
            ('FALSE', 'HAYIR'),
        )

        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        keywords = models.CharField(blank=True, max_length=100)
        description = models.CharField(blank=True, max_length=100)
        image = models.ImageField(blank=True, upload_to='images/')
        price = models.FloatField()
        amount = models.IntegerField()
        detail = RichTextUploadingField()
        slug = models.CharField(blank=True, max_length=150)
        status = models.CharField(max_length=10, choices=STATUS)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

        def image_tag(self):
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        image_tag.short_description = 'Image'

        def cating_tag(self):
            return mark_safe(((Category.status)))

class Images(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank= True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))

    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS ={
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
        class Meta:
            model = Comment
            fields = ['subject', 'comment', 'rate']