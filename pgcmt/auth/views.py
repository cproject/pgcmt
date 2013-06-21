from auth.models import LoginForm
from django.shortcuts import render_to_response, HttpResponseRedirect,render
from django.contrib.auth import *

def check_login(request):
    def errorHandle(error):
        form = LoginForm()
        return render(request,'auth/login.html', {
                'error' : error,
                'form' : form,
        })
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
            return render(request,'auth/login.html', { 'form': form, 'title':'Login' })

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        form = LoginForm()
        return check_login(request)
    else: 
        check_login(request)
        return HttpResponseRedirect('/')
