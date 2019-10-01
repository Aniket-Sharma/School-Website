from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Review
from .forms import ReviewForm
class Review_Page_View(TemplateView):
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