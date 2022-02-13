from urllib import request
from django.shortcuts import render

# Create your views here.

def index(request):
    person = {'name':'Isabel Valdez', 'title':'Computer Science'}

    tabs = {"Resume":"https://github.com/liz0123", "LinkedIn":"https://www.linkedin.com/in/isabel-valdez-000045b5","GitHub":"https://github.com/liz0123"}
   
    competdium ={"name": "Competdium", "subtitle":'Website',"summary":"This website is geared toward helping indiviuals find their perfect pet. ", 'link':"https://github.com/liz0123/Competdium"}
    makeup ={"name": "Makeup With Jasmine", "subtitle":'Website',"summary":"Created a proflio website for a makeup artist. ", 'link':"https://github.com/liz0123/Competdium"}
    
    projects = [competdium, makeup]
    return render(request,'profolio/index.html', {'tabs':tabs, 'projects':projects, 'person':person})
