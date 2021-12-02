from django.contrib import admin
from .models import RPG, Stat, Classification, Entity, ClassOption, StatBuff

# Register your models here.

admin.site.register([RPG, Stat, Classification, Entity, ClassOption, StatBuff])