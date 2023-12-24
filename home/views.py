from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    messages.success(request, "welcome to contact")
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact_form = Contact(name = name, email = email, message = message)
        Contact_form.save()
        return redirect("/")
    return render(request, "contact.html")
def blogs(request):
    return render(request, "blogs.html")
