from django import forms

from base.models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'perception', 'satisfaction', 'comments']

    def save(self, version, mock_survey_data):
        instance = super(SurveyForm, self).save(commit=False)
        instance.set_mock_survey(mock_survey_data)
        instance.version = version
        instance.save()
        return instance
