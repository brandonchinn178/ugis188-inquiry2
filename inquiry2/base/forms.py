from django import forms

from base.models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'perception', 'professional', 'comments']

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)

        # programmatically create meme fields

    def save(self, version):
        instance = super(SurveyForm, self).save(commit=False)
        instance.version = version
        instance.save()
        return instance
