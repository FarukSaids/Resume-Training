from lib2to3.fixes.fix_input import context
from xml.dom.minidom import Document

from django.shortcuts import render,redirect,get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia,Document


def layout(request):
    documents = Document.objects.all()
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter

    # Image
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_imge = ImageSetting.objects.get(name='home_banner_imge').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    socialmedia = SocialMedia.objects.all()
    context ={
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'home_banner_name': home_banner_name,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_description ': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,
        'header_logo': header_logo,
        'home_banner_image': home_banner_imge,
        'site_favicon': site_favicon,
        'socialmedia': socialmedia,
    }
    return context

# Create your views here.
def index(request):


#skills
    skills= Skill.objects.all().order_by('name')

#experiences
    experiences = Experience.objects.all().order_by('start_date')

#educations
    educations = Education.objects.all().order_by('start_date')
#socialmedi


    context = \
        {

        'skills': skills,
        'experiences': experiences,
        'educations':educations,



         }
    return render(request,'index.html', context=context)

def redirect_urls(request,slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)

