from django.forms import ModelForm
from .models import Widget

class DeleteWidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']