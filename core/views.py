from core.models import GeneralSetting, Skill, Experience, Project
from django.shortcuts import render


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    job_title = GeneralSetting.objects.get(name='job_title').parameter
    about_myself = GeneralSetting.objects.get(name='about_myself').parameter

    #Skills
    skills = Skill.objects.all().order_by('order')

    #Experience
    experiences = Experience.objects.all().order_by('start_date')

    projects = Project.objects.all().order_by('project_date')
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'about_myself': about_myself,
        'job_title': job_title,
        'skills': skills,
        'experience': experiences,
        'projects': projects,
    }

    return render(request, 'index.html', context=context)
