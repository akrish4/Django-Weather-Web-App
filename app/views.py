from django.core.mail.message import EmailMessage
from django.core import mail
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.models import Contact

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('num')
        description = request.POST.get('description')
        contact_query = Contact(
            name=fullname, email=email, number=phone, description=description)
        contact_query.save()
        from_email = settings.EMAIL_HOST_USER
        # email starts here
        # your mail starts here
        connection = mail.get_connection()
        connection.open()
        email_mesge = mail.EmailMessage(f'Website Email from {fullname}', f'Email from : {email}\nUser Query :{description}\nPhone No : {phone}', from_email, [
                                        'ananthakrishnannairrs@gmail.com'], connection=connection)
        email_user = mail.EmailMessage('ABC Company', f'Hello {fullname}\nThanks fo Contacting Us Will Resolve Your Query Asap\nThank You', from_email, [email], connection=connection)
        connection.send_messages([email_mesge, email_user])
        connection.close()
        messages.info(request, "Thanks for Contacting Us ")
        return redirect('/contact')
    return render(request, 'contact.html')




def get_html_content(request):
    import requests
    city = request.GET.get('city')
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content


def weather(request):
    result = None
    if 'city' in request.GET:
        # fetch the weather from Google.
        html_content = get_html_content(request)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        # extract region
        result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
        # extract temperature now
        result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
        # get the day and hour now
        result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
        # get the actual weather
        result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    return render(request, 'weather.html', {'result': result})

def handleBlog(request):
    if not request.user.is_authenticated:
        messages.error(request, "please login and try again")
        return redirect('/login')
    return render(request, 'handleBlog.html')


def about(request):
    return render(request, 'about.html')


def signUp(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse("password not matched")
        try:
            if user.objects.get(username=username):
                return HttpResponse("username is taken")
        except Exception as identifier:
            pass
        try:
            if user.objects.get(email=email):
                return HttpResponse("email is already taken")
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_nane = lastname
        myuser.save()
        messages.success(request, "signup successfully")
        return  redirect('/login')
    return render(request, 'auth/signUp.html')


def handlelogin(request):
    if request.method == "POST":
        handleusername = request.POST['username']
        handlepassword = request.POST['pass1']
        user = authenticate(username=handleusername, password=handlepassword)
        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome to my Website')
            return redirect('/')
        else:
            messages.warning(request, "Invalid credentials")
            return redirect('/login')
    return render(request, 'auth/login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, "logout success")
    return redirect('/login')

def search(request):
    query=request.GET['search']
    if len(query)>80:
        allPosts = handleBlog.objects.none()
    else:
        allPostsTitle=handleBlog.objects.filter(title__icontains=query)
        allPostsContent=handleBlog.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request,"No Search Results")
    params={'allPosts':allPosts,'query':query}        

    return render(request,'search.html',params)

