from django.db import models
from django.contrib.auth.models import User

from django_prometheus.models import ExportModelOperationsMixin

class Provider(ExportModelOperationsMixin('provider'),models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    Key_name = models.CharField(max_length=100)

    provider_url = models.URLField(blank=True, null=True)
    secret_key =  models.CharField(max_length=100,  blank=True, null=True)
    access_token = models.CharField(max_length=100, blank=True, null=True )
    is_connected = models.BooleanField(default=False)  # New field
    kubeconfig_data = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.provider_name