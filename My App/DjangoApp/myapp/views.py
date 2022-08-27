from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def IndexView(request):
    # return HttpResponse("Welcome to the home page")
    context = {
        'name' : "Abdelrahman",
    }
    return render(request,'myapp/index.html',context)

def ProfileView(request):
    context = {
        'my_age': '54',
    }
    return render(request,'myapp/profile.html',context)

# Not checked yet
class UserView(View):
    def get(self,request):
        data = {
            'first_name': 'Abdelrahman',
            'last_name': 'Salem',
            'age': '23',
            'email': 'Abdelrahmansalem16@gmail.com'
        }
        context = {'user_data': data}
        return render(request,'myapp/user.html',context)