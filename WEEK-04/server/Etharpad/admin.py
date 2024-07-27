from django.contrib import admin
from .models import EtharpadClass

class EtharpadClassAdmin(admin.ModelAdmin):
    pass

admin.site.register(EtharpadClass,EtharpadClassAdmin)


