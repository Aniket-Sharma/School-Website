from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Review, Contact, Teacher, Subscriber
from .forms import ReviewForm, ContactForm, SubscriberForm


class ReviewPageView(TemplateView):
    template_name = 'review/home.html'

    def get(self, request):
        reviews = Review.objects.all()
        form = ReviewForm()

        args = {'reviews': reviews, 'form': form}

        return render(request, self.template_name, args)

    def post(self, request):
        form = ReviewForm(request.POST)
        form.save()
        return redirect('review')


class HomePageView(TemplateView):
    template_name = 'main/school_home.html'

    def get(self, request):

        form = SubscriberForm()

        args = {'form': form}

        return render(request, self.template_name, args)

    def post(self,request):
        sub = SubscriberForm(request.POST)
        if sub.is_valid():
            sub.save()
            messages.success(request, "You are successfully subscribed for future updates !")
        return redirect('home')


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
        form = ContactForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Your message was sent successfully !")
        return redirect('home')

# @csrf_exempt
# def send_message(self, request):
#     template_name = 'main/contact.html'
#     if request.method == 'POST':
#         form = Contact()
#         form.f_name = request.POST.get('fname')
#         form.l_name = request.POST.get('lname')
#         form.email = request.POST.get('eadress')
#         form.tel_no = request.POST.get('tel')
#         form.message = request.POST.get('message')
#         form.save()
#         messages.success(request, "Your message was sent successfully !")
#         return redirect('home')
#     else :
#         args = {}
#         return render(request, self.template_name, args)


