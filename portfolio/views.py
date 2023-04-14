from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blog
# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def handleBlog(request):
	posts = Blog.objects.all()
	context = {'posts': posts}
	return render(request, 'blog.html', context)

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone_number = request.POST.get('number')
		description = request.POST.get('description')
		# print(name, email, phone_number, description)
		query = Contact(name=name, email=email, phone_number=phone_number, description=description)
		query.save()
		messages.success(request, "Your message has been sent successfully! We will get back to you soon. Thank you!")
		return redirect('/contact')
	return render(request, 'contact.html')