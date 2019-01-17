from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .admin import FacebookPost
# Create your views here.
def test(request):
    return HttpResponse("hello world")


@csrf_exempt
class fbPOST(View):
    def get(self, request):
        form = FacebookPost()
        return HttpResponse("no POST request!!!")
    def post(self, request):
        form = FacebookPost(request.POST)
        if form.is_valid():
            des = request.POST['description']
            category = request.POST['category']
            media = request.FILES['media']
            print(des)
            print(category)
            print(media)
            form.save(des,category,media)
            return HttpResponse("Data saved")
        else:
            return HttpResponse("Some Error!!!")




@csrf_exempt
def twPOST(request):
    if request.POST:
        des = request.POST['description']
        category = request.POST['category']
        print(des)
        print(category)
        return HttpResponse("Data saved")
    return HttpResponse("no POST request!!!")

def tokenStatus(request):
    return HttpResponse("Token request!!!")