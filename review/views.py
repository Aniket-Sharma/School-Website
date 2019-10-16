from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Review, Contact, Teacher
from .forms import ReviewForm


class ReviewPageView(TemplateView):
	template_name = 'review/home.html'

	def get(self, request):
		
		reviews = Review.objects.all()
		form = ReviewForm()

		args = {'reviews' : reviews, 'form': form}

		return render(request, self.template_name, args)

	def post(self, request):
		form = ReviewForm(request.POST)
		form.save()
		return redirect('review')


class HomePageView(TemplateView):
	template_name = 'main/school_home.html'

	def get(self, request):

		args = {}

		return render(request, self.template_name, args)


class AboutPageView(TemplateView):
	template_name = 'main/about.html'

	def get(self, request):

		teachers = Teacher.objects.all()

		args = {'teachers': teachers}

		return render(request, self.template_name, args)


class AdmissionPageView(TemplateView):
	template_name = 'main/admissions.html'

	def get(self, request):

		args = {}

		return render(request, self.template_name, args)


class GalleryPageView(TemplateView):
	template_name = 'main/gallery.html'

	def get(self, request):

		args = {}

		return render(request, self.template_name, args)


class ContactPageView(TemplateView):
	template_name = 'main/contact.html'

	def get(self, request):

		args = {}

		return render(request, self.template_name, args)


