from django.db import models

# Create your models here.

class FacebookPost(models.Model):
        des = models.CharField(max_length=10000,verbose_name='Post Description')
        category = models.CharField(max_length=50, verbose_name='Post Category')
        media = models.FileField(upload_to=''+str(id) +'/', verbose_name='Post Media file')
        timestamp = models.DateField(auto_now_add=True)
        status = models.CharField(max_length=10, verbose_name='Post Status')
        def save(self, *args, **kwargs):
            return super(FacebookPost, self).save(*args, **kwargs)

        class Meta:
            verbose_name = 'Facebook Posts'
            verbose_name_plural = verbose_name