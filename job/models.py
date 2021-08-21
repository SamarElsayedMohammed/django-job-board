from django.db import models
from datetime import datetime
import os
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    tx =timezone.localtime(timezone.now())
    # now = datetime.now()
    image_name , extention = filename.split(".")
    # sec = int(now.strftime("%S"))
    # m = int(now.strftime("%M"))
    # h = int(now.strftime("%H"))
    # t = (h*60*60)+(m*60)+sec 
    return "jobs/%s.%s"%(tx,extention)
    # ext = filename.split('.')[-1]
    # filename = "%s_%s.%s" % (instance.id, instance.title, ext)
    # return os.path.join('uploads', filename)

# Create your models here.
class Job(models.Model):

    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15 ,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)

    def save(self ,*args ,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs) 

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name 

class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name




