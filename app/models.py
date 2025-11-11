from django.core.validators import validate_email
from django.db import models 
from django.utils.translation import gettext_lazy as _
class React(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=75, unique=True, validators=[validate_email])

    def __str__(self):
        return self.username
    
def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)


class Posting(models.Model):
    name = models.CharField(max_length=30)
    problem = models.CharField(max_length=300)
    email = models.EmailField(max_length=75, unique=True, validators=[validate_email])
    age = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(_("Image"),upload_to=upload_to,default='posts/default.jpg')
    upi = models.CharField(max_length=50)
    


    # def image_url(self):
    #     if self.image:
    #         return self.image_url
    #     else:
    #         return ' '



    def __str__(self):
        return self.name
