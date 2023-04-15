from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blog
# below imports are for sending email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
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
		# sending email
		from_email = settings.EMAIL_HOST_USER
		connection = mail.get_connection()
		connection.open()
		email_message = mail.EmailMessage(f"Email from {name}", f"User's email: {email}\nUser's phone number: {phone_number}\n\n\nUser's query: {description}", from_email, ["sakhman3250@gmail.com", "sakhman2001@gmail.com"], connection=connection)
		connection.send_messages([email_message])
		connection.close()
		messages.success(request, "Your message has been sent successfully! We will get back to you soon. Thank you!")
		return redirect('/contact')
	return render(request, 'contact.html')