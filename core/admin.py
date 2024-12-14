from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(GeneralSetting) #admin sayfasında görülür olması icin
class GeneralSettingdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameter','updated_date','created_date']
    search_fields = ['name','description','parameter']
    list_editable = ['description','parameter']

    class Meta: #default özellik veriliyor
        model = GeneralSetting


@admin.register(ImageSetting)  # admin sayfasında görülür olması icin
class ImageSettinAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:  # default özellik veriliyor
        model = ImageSetting

@admin.register(Skill)  # admin sayfasında görülür olması icin
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:  # default özellik veriliyor
        model = Skill
