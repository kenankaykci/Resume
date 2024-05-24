from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'parameter', 'updated_date', 'created_date')
    search_fields = ('name', 'description', 'parameter')
    list_editable = ('name', 'description', 'parameter')

    class Meta:
        model = GeneralSetting


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'percentage', 'updated_date', 'created_date')
    search_fields = ['name']
    list_editable = ('order', 'name', 'percentage')

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_title', 'job_location', 'job_information', 'start_date', 'end_date')
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ('company_name', 'job_title', 'job_location', 'job_information', 'start_date', 'end_date')

    class Meta:
        model = Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_description', 'project_date')
