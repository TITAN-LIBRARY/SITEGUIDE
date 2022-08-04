from datetime import datetime
from django.db import models

TYPE_CHOICES = (
    ("Website", "Website"),
    ("Application", "Application"))


class Technology(models.Model):
    logo = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Projects(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    case_study = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=500, blank=False, choices=TYPE_CHOICES)  # Website or application?
    website = models.URLField(blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='media/', help_text="Project Company logo", default="media/dummy.jpeg")
    image = models.ImageField(upload_to='media/', help_text="This image will shown on list and feed preview")
    mobile_image = models.ImageField(upload_to='media/', help_text="This image will shown on list and feed preview",
                                     blank=True, null=True)
    technology = models.ManyToManyField(Technology)
    created_at = models.DateTimeField(null=True, blank=True, default=datetime.now)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project_name}"


class Review(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, blank=False)
    review = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True, default=datetime.now)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    website = models.URLField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, default=datetime.now)
    
    def __str__(self):
        return f"{self.name}"