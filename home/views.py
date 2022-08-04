from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Projects, Review, Contact, Technology
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView


class Home(View):
    def get(self, *args, **kwargs):
        project = Projects.objects.filter(is_featured=True)
        review = Review.objects.all()
        technology = Technology.objects.all()
        brands = Projects.objects.filter()

        return render(self.request, 'home.html', {"project": project, "review": review, "technology": technology,
                                                  "brands": brands})


class Works(View):
    def get(self, *args, **kwargs):
        project = Projects.objects.all()
        return render(self.request, 'works.html', {"project": project})


class WebsiteServicesView(View):
    def get(self, *args, **kwargs):
        project = Projects.objects.filter(is_featured=True)
        brands = Projects.objects.filter()
        return render(self.request, 'services.html', {"project": project, "brands": brands})


class Testimonials(View):
    def get(self, *args, **kwargs):
        review = Review.objects.all()
        brands = Projects.objects.filter()
        return render(self.request, 'testimonials.html', {"review": review, "brands": brands})


# TODO show success message
# TODO add a captcha
class ContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'description', 'website']
    template_name = "contact.html"
    success_url = '/contact'

    def form_valid(self, form):
        messages.success(self.request, "We will get back to you soon!")
        return super().form_valid(form)
