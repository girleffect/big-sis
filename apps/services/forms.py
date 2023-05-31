from django import forms
from apps.services.models import ServiceLocation, ServiceType, ServicePage


class ServiceFinderForm(forms.ModelForm):
    service_type = forms.ModelMultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control'
        }
    ), queryset=ServiceType.objects.all())

    class Meta:
        model = ServicePage
        fields = ['service_type', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].empty_label = "Location"