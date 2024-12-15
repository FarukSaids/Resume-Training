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

@admin.register(Experience)  # admin sayfasında görülür olması icin
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name' ,'job_title', 'job_location', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['company_name' ,'job_title', 'job_location']
    list_editable = ['company_name' ,'job_title', 'job_location', 'start_date', 'end_date']

    class Meta:  # default özellik veriliyor
        model = Experience

@admin.register(Education)  # admin sayfasında görülür olması icin
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name' ,'major', 'department', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['school_name' ,'major', 'department']
    list_editable = ['school_name' ,'major', 'department', 'start_date', 'end_date']

    class Meta:  # default özellik veriliyor
        model = Education

@admin.register(SocialMedia)  # admin sayfasında görülür olması icin
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order' ,'link', 'icon', 'updated_date', 'created_date']
    search_fields = ['order']
    list_editable = ['order' ,'link', 'icon']

    class Meta:  # default özellik veriliyor
        model = SocialMedia

@admin.register(Document)  # admin sayfasında görülür olması icin
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order' ,'slug', 'button_text','file', 'updated_date', 'created_date']
    search_fields = ['slug', 'button_text']
    list_editable = ['order' ,'slug', 'button_text','file']

    class Meta:  # default özellik veriliyor
        model = Document