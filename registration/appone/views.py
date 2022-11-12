from django.shortcuts import render , redirect

from appone.forms import UserRegistrationForm , AddressRegistrationForm

from django.contrib.auth import authenticate , login as lg , logout as loggout

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    return render(request,'appone/index.html',{})


def register(request):

    form = UserRegistrationForm()

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')


    else:
        return render(request,'appone/register.html',{'form':form})


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username = username,password = password)

            if user is not None:

                lg(request,user)

                return render(request,'appone/home.html',{})

            else:

                return redirect('login')
        else:

            return redirect('login')

    else:
        return render(request,'appone/login.html',{})

@login_required(login_url='/login')
def home(request):

    return render(request,'appone/home.html',{})



def lgout(request):

    loggout(request)

    return redirect('login')


@login_required(login_url='/login')
def Address(request):

    form = AddressRegistrationForm()
    if request.method == 'POST':

        form = AddressRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

        else:
            return render(request,'appone/address.html',{'form':form})


    else:

        return render(request,'appone/address.html',{'form':form})



