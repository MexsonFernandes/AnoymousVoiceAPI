from django.contrib import admin

# Register your models here.
from .models import FacebookPost

class FacebookAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Facebook Posts'
        verbose_name_plural = verbose_name
        model = FacebookPost
        fields = "__all__"



admin.site.register(FacebookPost, FacebookAdmin)