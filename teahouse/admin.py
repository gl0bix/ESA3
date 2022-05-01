from django.contrib import admin

# Register your models here.
from teahouse.models import Tea, Origin, Preperation

admin.site.register(Tea)
admin.site.register(Origin)
admin.site.register(Preperation)
