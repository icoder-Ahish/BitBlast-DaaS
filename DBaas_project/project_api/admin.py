from django.contrib import admin
from .models import Project, Cluster,Db_credentials

from .models import DBcredentials
# Register your models here.
admin.site.register(DBcredentials)


admin.site.register(Db_credentials)

# Register your models here.
admin.site.register (Project)
admin.site.register (Cluster)