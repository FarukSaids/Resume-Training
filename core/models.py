from wsgiref.validate import validator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text='',
    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,  # bir kere kayıt alıyor
        verbose_name='Created Date',
        help_text='',
    )

    class Meta:
        abstract = True  # django icin buranın abstract modunu acıyoruz yoksa bir tablo daha olusturacak


# Create your models here.
class GeneralSetting(AbstractModel):  # database de bir tablo old belirtiliyor.
    name = (models.CharField
        (
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name test',
        help_text='This is variable of the setting.',
    ))
    description = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name='description',
        help_text='',
    )
    parameter = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']


class ImageSetting(AbstractModel):
    name = (models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name test',
        help_text='This is variable of the setting.',
    ))
    description = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name='description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        blank=True,
        help_text='',
        upload_to='images/',
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = (models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name test',
        help_text='This is variable of the setting.',
    ))
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
    )


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date',

    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Skill: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['company_name']


class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )
    major = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date',

    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Skill: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['school_name']


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        default='',
        max_length=254,                     #cntrl alt L ile duzenleme
        blank=True,
        verbose_name='Icon',

    )

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'
        ordering = ('order',)



class Document(AbstractModel):
    order=models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button text',
        help_text='',
    )
    file=models.FileField(
        default='',
        verbose_name='File',
        blank=True,
        upload_to='documents/',
    )
    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
