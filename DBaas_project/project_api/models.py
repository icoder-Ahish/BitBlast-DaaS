from django.db import models
from django.contrib.auth.models import User
# For django-prometheus

from django_prometheus.models import ExportModelOperationsMixin

class Project(ExportModelOperationsMixin('project'), models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, db_index = True)
    updated_date = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.project_name

class Cluster(ExportModelOperationsMixin('cluster'), models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cluster_name = models.CharField(max_length=255)
    cluster_type = models.CharField(max_length=100)
    database_version = models.CharField(max_length=50)
    provider = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cluster_name




class DBcredentials(ExportModelOperationsMixin('dbcredentials'), models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    clusterName = models.CharField(max_length=225)
    pipeline_id = models.IntegerField()
    filename = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.clusterName} and {self.filename} and {self.pipeline_id}"        

class Db_credentials(ExportModelOperationsMixin('Dbcredentials'), models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cluster_name = models.CharField(max_length=225)
    cluster_type = models.CharField(max_length=225)
    database_version = models.CharField(max_length=225)
    provider_name = models.CharField(max_length=225)
    pipeline_id = models.IntegerField()
    filename = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
