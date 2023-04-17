from django.shortcuts import render, redirect
from questions.models import DBMS
from django.contrib import messages
# Create your views here.
def topic(request):
	return render(request, 'topic.html')

def dbms(request):
	if request.method == "POST":
		question = request.POST.get('question')
		answer = request.POST.get('answer')
		query = DBMS(question=question, answer=answer)
		query.save()
		messages.success(request, "Question added successfully!")
		return redirect('/questions/dbms')
	context = {'questions': DBMS.objects.all()}
	return render(request, 'dbms.html', context)