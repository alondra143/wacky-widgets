from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    
    return render(request, 'home.html', {'widgets': widgets,'widget_form': widget_form});

def add_widget(request):
    #make the ModelForm from the request.POST
    print (request.POST)
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')
    # #save to database
    # #redirect to home

def delete_widget(request, widget_id):
    #get the widget that is being deleted by its pk and delete
    Widget.objects.filter(id=widget_id).delete()
    #redirect to home
    return redirect('home')