from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name="Updated Date"
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name"
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description"
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Parameter"
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        max_length=254,
        default='',
        blank=True,
        verbose_name="Name",
        help_text="This variable is used for giving info about your skill"
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        verbose_name="Company Name",
        blank='',
    )
    job_title = models.CharField(
        max_length=254,
        default='',
        verbose_name="Job Title",
        blank='',
    )
    job_location = models.CharField(
        max_length=254,
        default='',
        verbose_name="Job Location",
        blank='',
    )
    job_information = models.CharField(
        max_length=254,
        default='',
        verbose_name="Job Information",
        blank='',
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('start_date',)


class Project(AbstractModel):
    project_name = models.CharField(
        default='',
        max_length=254,
        verbose_name="Project Name",
        blank='',
    )
    project_description = models.CharField(
        default='',
        max_length=254,
        verbose_name="Description",
        blank='',
    )
    project_date = models.DateField(
        verbose_name="Project Date",
    )

    def __str__(self):
        return f'Project: {self.project_name}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('project_date',)
