from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    folder = models.ForeignKey('Folder', related_name= "notes", null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='notes', null=True, blank=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

class Folder(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
