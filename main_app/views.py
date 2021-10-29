from django.shortcuts import render, redirect
from .models import Widget
from .forms import DeleteWidgetForm

# Create your views here.
def home(request):
    return render(request, 'home.html');

def add_widget(request):
    #make the ModelForm from the request.POST
    pass
    #save to database
    #redirect to home

def delete_widget(request, widget_id):
    #get the widget that is being deleted by its pk and delete
    #redirect to home
    pass