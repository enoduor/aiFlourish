from import_export import resources
from .models import stuffs,category

class stuffsResource(resources.ModelResource):
     class Meta:
         model = stuffs

class categoryResource(resources.ModelResource):
     class Meta:
         model = category

        