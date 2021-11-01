from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from django.http import HttpRequest
# Create your views here.


def more_todo(request):
    return HttpResponse('Ok')


def home(request):
    filter_products = Prabhu.objects.filter(is_there_in_popular=True)
    live = Live.objects.all()
    vani = UpcomingEvent.objects.all()
    ts = TempleKirtan.objects.all()
    ft = FestivalTrack.objects.all()
    return render(request, 'index.html', {'filter_ps': filter_products, 'lives': live, 'ue': vani, 'ts': ts, 'ft': ft})


def register(request):
    form = RegisterationForm(request.POST)
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()
            email_subject = 'Thanks for registering'
            message = render_to_string('authentication/thanks_for_registering.html', {
                'user': user,
            })
            to_email = email
            send_email = EmailMessage(email_subject, message, to=[to_email])
            send_email.send()
            return redirect('login')

        return render(request, 'authentication/signup.html', {'form': form})


def login(request, error=None):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            auth.login(request, user)
            return redirect('home')
        except AttributeError:
            messages.error(request, 'Invalid email or password')

    return render(request, 'authentication/login.html', {'errors': error})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def artists(request):
    prabhu = Prabhu.objects.all()
    return render(request, 'artists.html', {'prabhu': prabhu})


def artists_single(request, product_slug):
    single_prabhu = Prabhu.objects.get(slug=product_slug)

    context = {
        'single_prabhu': single_prabhu,
    }
    return render(request, 'artist.html', context)


def podcasts(request):
    single = Prabhu.objects.all()
    return render(request, 'podcasts.html', {'singles': single})


def release(request, prabhu):
    content = Content.objects.filter(prabhu=prabhu)
    p = Prabhu.objects.values_list('id')
    i = p[0]
    j = i[0]
    return render(request, 'releases.html', {'content': content, 'p': j})


def track(request, prabhu, name):
    content = Content.objects.get(id=name)
    p = Prabhu.objects.values_list('id')
    i = p[0]
    j = list(i)
    m = j
    audio = Audio.objects.filter(prabhu=name)
    count = audio.count()
    return render(request, 'release.html', {'content': content, 'audios': audio, 'count': count, 'p': m})


@login_required(login_url='login')
def playlist_a(request, id):
    audio = Audio.objects.get(id=id)
    play_list_model = Playlist()
    play_list_model.user = request.user
    play_list_model.song_1 = audio
    play_list_model.save()
    return redirect('profile')


@login_required(login_url='login')
def playlist_remove(request, id):
    audio = Playlist.objects.get(id=id, user=request.user)
    audio.delete()
    return redirect('profile')


@login_required(login_url='login')
def profile(request):
    audio1 = Playlist.objects.filter(user=request.user)
    notifications = Notification.objects.all()
    return render(request, 'profile.html', {'audios': audio1, 'notifications': notifications})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']
        email_subject = subject
        message = render_to_string('contact_email.html', {
            'user': request.user,
            'content': text,
            'name': name,
            'email': email,
        })
        to_email = 'ram.harekrishna108@gmail.com'
        send_email = EmailMessage(email_subject, message, to=[to_email])
        send_email.send()
        return redirect('c_thanks')
    return render(request, 'contacts.html', {})


def c_thanks(request):
    return render(request, 'contact_thanks.html', {})
