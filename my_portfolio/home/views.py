from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.

def index(request):
    # return HttpResponse('This is my Home Page ')
    context = {'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my About Page (about/)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my contact Page (projects/)")
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']

        # print(name,phone,email,desc)

        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print('the data was saved in the database')
    # return HttpResponse("This is my contact Page (contact/)")
    return render(request, 'contact.html')
