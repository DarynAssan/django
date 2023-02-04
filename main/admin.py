from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
# from . import models
from .models import Tagam, Un, Negizgi, Susyn, Tatty, Salat, Commentary, Tapsyrys

# Register your models here.
admin.site.register(Tagam)
admin.site.register(Un)
admin.site.register(Negizgi)
admin.site.register(Susyn)
admin.site.register(Tatty)
admin.site.register(Salat)
admin.site.register(Commentary)
admin.site.register(Tapsyrys)
