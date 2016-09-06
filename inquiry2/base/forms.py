from django import forms

from base.models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        excludes = ['mock_survey']

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)

        # programmatically create meme fields
