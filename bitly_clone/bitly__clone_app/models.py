from __future__ import unicode_literals

import random
import string

from django.db import models

# Create your models here.

def generate(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

    code = ''.join(aleatoire)
    return code

class UrlShort(models.Model):
    user_url=models.URLField(unique=True, verbose_name='the user url')
    url_code=models.CharField(max_length=6,unique=True)
    date_creation=models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='creation date')
    update_time=models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='creation date')
    nike_name=models.CharField(max_length=20,null=True,blank=True,verbose_name='user nike name')
    nb_access=models.IntegerField(default=0)



    def __str__(self):
        return self.user_url


    def __unicode__(self):
        return unicode(self.user_url)



    """this methode is used to override the save methode"""
    def save(self,*args,**kwargs):
        self.url_code=generate(6)
        super(UrlShort, self).save(*args,**kwargs)




