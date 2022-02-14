from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def index(request):
    person ={'name': 'Jasmine Valdez','title':"Makeup Artist",'bio':"Hello, I am a freelance makeup artist with over 7 years experience. I have worked with individuals of every complexion and every skin type. I travel to you, giving you the time to make sure everything else is ready for whatever you have planned. I have done work for all sorts of events, ranging from weddings and birthdays, to photo shoots and new years parties." }
    services = {"Weddings":static('images/profolio-01.png'), "Engagement":static('images/profolio-04.png'), "Bride Tribe":static('images/profolio-03.png'), "Special Events":static('images/profolio-02.png')}
    contact ={'instagram':'https://www.instagram.com/makeup_by_jasminev/?hl=en'}
    return render(request, 'JasmineMakeup/index.html', {'person':person, "services":services, 'contact':contact})
