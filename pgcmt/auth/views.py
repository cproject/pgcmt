from auth.models import LoginForm, ChangePasswordForm
from django.shortcuts import render_to_response, HttpResponseRedirect,render, get_object_or_404
from django.contrib.auth import *
from django.contrib.auth.models import User

def check_login(request):
    def errorHandle(error):
        form = LoginForm()
        context = { 
            'error' : error, 
            'form' : form, 
            'title': 'Login' 
            }
        return render(request,'auth/login.html', context )
    if request.user.is_authenticated():
        username = request.user.username
        return HttpResponseRedirect("/")
    else:
        if request.method == 'POST': # If the form has been submitted...
            form = LoginForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        # Redirect to a success page.
                        login(request, user)
                        return HttpResponseRedirect(request.POST["next"])
                    else:
                        # Return a 'disabled account' error message
                        error = u'account disabled'
                        return errorHandle(error)
                else:
                     # Return an 'invalid login' error message.
                    error = u'invalid login'
                    return errorHandle(error)
            else: 
                error = u'form is invalid'
                return errorHandle(error)       
        else:
            #form = LoginForm(initial={'next':request.GET["next"]}) # An unbound form
            if 'next' in request.GET:
                next = request.GET["next"]
            else:
                next = "/"
            form = LoginForm(initial={'next':next}) # An unbound form
            context = { 
                'form': form, 
                'title': 'Login'
                }
            return render(request,'auth/login.html', context )

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        form = LoginForm()
        return check_login(request)
    else: 
        check_login(request)
        return HttpResponseRedirect('/')

def changePassword(request):
    if request.method == 'GET':
        form = ChangePasswordForm()
        context = { 
                'form': form, 
                'title': 'Change Password'
                }
        return render(request,'auth/changePassword.html', context )
    else:
        print request
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if request.POST["password"] == request.POST["password_check"]:
                user = get_object_or_404(User,username=request.user)
                user.set_password(request.POST["password"])
                return HttpResponseRedirect('/')
            else:
                context = {
                    'form': form, 
                    'title': 'Change Password',
                    'error': 'Password does not match!'
                    }
                return render(request,'auth/changePassword.html', context )
        context = {
            'form': form, 
            'title': 'Change Password'
            }
    return render(request,'auth/changePassword.html', context )