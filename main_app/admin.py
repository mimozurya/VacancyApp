from django.contrib import admin
from .models import *

admin.site.register(Main) #регистрация моделей
admin.site.register(Info)
admin.site.register(Location)
admin.site.register(Ability)
