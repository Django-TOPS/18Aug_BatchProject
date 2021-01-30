from django.shortcuts import render, HttpResponse, redirect
from .models import signup,notes
from .forms import signupForm,notesForm
from django.core.mail import send_mail
from MyWebSite import settings
import random
from django.contrib.auth import logout
from twilio.rest import Client

# Create your views here.


def index(request):
    if request.method == 'POST':
        myfrm = signupForm(request.POST)
        if request.POST.get('signup')=='signup':
            if myfrm.is_valid():
                myfrm.save()

                """
                # Sending Confirmatoin Main
                subject = 'Signup Sucess! Welcome'
                msg = 'Hello User, Your account has been created successfully with us! Enjoy our service.'
                mail_from = settings.EMAIL_HOST_USER
                mail_to = ['jigneshpatel.ec.er@gmail.com',
                        'mehtamadhav007@gmail.com']

                send_mail(subject, msg, mail_from, mail_to)
                print("Mail Send Successfully!")
                
                """
                """
                # SMS Sending
                #account_sid = os.environ['ACd8e6df33dc5a3452449aca0d631e83d6']
                #auth_token = os.environ['67ab20a19e679ce8042c505fe664675b']
                #client = Client(account_sid, auth_token)
                otp = random.randint(1111, 9999)
                client = Client('ACd8e6df33dc5a3452449aca0d631e83d6',
                                '67ab20a19e679ce8042c505fe664675b')

                message = client.messages.create(
                    body=f"Hello User, Your account has been created successfully with us, and your one time password is {otp}",
                    from_='+18086701446',
                    to='+919898536464'
                )

                print(message.sid)
                """
                print("Signup Successfully!")
                return redirect('profile')
            
            else:
                print(myfrm.errors)
        
        elif request.POST.get('login')=='login':
            
            print("Login Calling.....")
            email=request.POST['email']
            password=request.POST['password']
            uid=signup.objects.get(email=email)
            user=signup.objects.filter(email=email,password=password)

            if user:
                
                request.session['userid']=email
                request.session['uid']=uid.id
                print('Login Successfully!')
                print("UserID:",uid.id)
                return redirect('profile')
            else:
                print('Login Faild! Try again')
    else:
        myfrm = signupForm()
    return render(request, 'index.html', {'myfrm': myfrm})


def profile(request):
    user=request.session.get('userid')
    if request.method=='POST':
        if request.POST.get('submitpost')=='submitpost':
            mynotes=notesForm(request.POST,request.FILES)
            if mynotes.is_valid():
                mynotes.save()
                print('Your Post has been uploaded successfully!')
            else:
                print(mynotes.errors)
        elif request.POST.get('login')=='login':
            print("Login Calling.....")
            email=request.POST['email']
            password=request.POST['password']
            uid=signup.objects.get(email=email)
            user=signup.objects.filter(email=email,password=password)

            if user:
                request.session['userid']=email
                request.session['uid']=uid.id
                print('Login Successfully!')
                print("UserID:",uid.id)
                return redirect('profile')
            else:
                print('Login Faild! Try again')
    else:
        mynotes=notesForm()
    return render(request,'profile.html',{'mynotes':mynotes,'user':user})

def user_logout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('userid')
    stid=request.session.get('uid')
    if request.method=='POST':
        myfrm=signupForm(request.POST)
        id=signup.objects.get(id=stid)
        if myfrm.is_valid():
            myfrm=signupForm(request.POST, instance=id)
            myfrm.save()
            print("Your profile has been updated!")
            return redirect('updateprofile')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupForm()
    return render(request,'updateprofile.html',{'myfrm':myfrm,'user':user,'stdata':signup.objects.get(id=stid)})