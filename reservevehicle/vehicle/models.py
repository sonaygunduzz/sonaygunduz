from django.db import models



# Create your models here.
class Category(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)

    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Vehicle(models.Model):

        STATUS = (
            ('True', 'Evet'),
            ('FALSE', 'HAYIR'),
        )

        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        title = models.CharField(max_length=50)
        keywords = models.CharField(max_length=100)
        description = models.CharField(max_length=100)
        image = models.ImageField(blank=True, upload_to='images/')

        price = models.FloatField()
        amount = models.IntegerField()
        detail = models.TextField()
        status = models.CharField(max_length=10, choices=STATUS)

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title
