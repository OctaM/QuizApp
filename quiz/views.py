from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import User
from django.views.decorators.csrf import csrf_exempt,csrf_protect, requires_csrf_token
from django.core.files.uploadedfile import SimpleUploadedFile
import sys
from django.shortcuts import redirect


globalData = []
globalData.append("General Info")


@csrf_exempt
# def IndexTemp(request):
#     sys.stderr.write(">> TEMP INDEX ACCESSED \n")
#     if request.method == 'GET':
#         return render(request, 'quiz/index.html')
#     elif request.method == 'POST':
#         try:
#             data = request.POST.get('data')
#             # FUNCTIONALITY
#             # print(">> INFO IMG DATA : " + str(data[:200]))
#             # with open('dev/tempFiles/fis.txt', 'w') as f:
#             #     f.write(data)
#             #     f.close()
#         except:
#             print(">>> Troubles in request")
#         return HttpResponseRedirect('/')

@csrf_exempt
def IndexView(request):
    if request.method == 'GET':
       return render(request, 'quiz/index.html')
    elif request.method == 'POST':
        button_pressed = request.POST.get('but_pressed')
        print(">> " + str(button_pressed) + "pressed")
        if button_pressed == 'profile':
            print("Profile pressed ")
            # return HttpResponseRedirect('/quiz/profile/')
            redirect('/quiz/profile')

def ProfileView(request):
    if request.method == 'GET':
        return render(request, 'quiz/profile.html')

@csrf_exempt
def LogInView(request):
    if request.method == 'GET':
        temp = len(globalData)
        context = {'info': globalData, 'len': temp}
        return render(request, 'quiz/login.html', context)
    elif request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(">> Client msg : " + str(username) + "  " + str(password))
        # globalData.append()

        # retrieving user from database
        user = User.objects.filter(username=username, password=password)

        #validation
        if user is not None:
            print('userul a fost gasit')
            context = {'info' : 'popup'}
            return render(request, 'quiz/index.html', context)
            # return HttpResponseRedirect('/quiz/index/')


def TestView(request):
    if request.method == 'GET':
        temp = len(globalData)
        context = {'info': globalData, 'len': temp}
        return render(request, 'quiz/test.html', context)
    elif request.method == 'POST':

        data = request.POST.get('data')
        print(">> Client msg : " + str(data))
        globalData.append(data)
        return HttpResponseRedirect('/quiz/login/')


def GameView(request):
    pass
