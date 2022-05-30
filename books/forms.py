from django import forms
from .models import Recommendation


class RecommendationForm(forms.ModelForm):
    # book = forms.CharField(max_length=64)
    # rate = forms.FloatField()
    # description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Recommendation
        fields = '__all__'