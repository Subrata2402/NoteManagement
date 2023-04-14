from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup(request):
	if request.method == "POST":
		get_email = request.POST.get('email')
		get_password = request.POST.get('password')
		get_confirm_password = request.POST.get('cnfpassword')
		print(get_email, get_password, get_confirm_password)
		if get_password != get_confirm_password:
			messages.info(request, "Password does not match")
			return redirect('/auth/signup')
		try:
			if User.objects.get(username=get_email):
				messages.warning(request, "User already exists")
				return redirect('/auth/signup')
		except Exception as identifier:
			pass
		myuser = User.objects.create_user(get_email, get_email, get_password)
		myuser.save()
		messages.success(request, "User created successfully! Please login to continue.")
		return redirect('/auth/login')
	return render(request, 'signup.html')

def handleLogin(request):
	if request.method == "POST":
		get_email = request.POST.get('email')
		get_password = request.POST.get('password')
		if not User.objects.filter(username=get_email).exists():
			messages.error(request, "User does not exist")
			return redirect('/auth/login')
		myuser = User.objects.get(username=get_email, password=get_password)
		if myuser:
			login(request, myuser)
			messages.success(request, "Logged in successfully!")
			return redirect('/')
		else:
			messages.error(request, "Invalid credentials! Please try again.")
			return redirect('/auth/login')
	return render(request, 'login.html')

def handleLogout(request):
	logout(request)
	messages.success(request, "Logged out successfully!")
	return render(request, 'login.html')