from django.contrib import admin
from .models import stuffs, category
from import_export.admin import ImportExportModelAdmin
from .resource import stuffsResource, categoryResource
from django import forms

# Register your models here.
"""class StuffsAdminForm(forms.ModelForm):
    class Meta:
        model = stuffs
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(
        queryset=category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class StuffsAdmin(admin.ModelAdmin):
    form = StuffsAdminForm"""

class stuffsAdmin(ImportExportModelAdmin):
     stuffs_class = stuffsResource

class categoryAdmin(ImportExportModelAdmin):
     category_class = categoryResource

admin.site.register(stuffs,stuffsAdmin)
#admin.site.register(category)

#admin.site.unregister(stuffs)
#admin.site.unregister(category)
admin.site.register(category,categoryAdmin)
#admin.site.register(stuffs,StuffsAdmin)
