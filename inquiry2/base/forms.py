from django import forms

from base.models import Survey, MockSurvey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'perception', 'satisfaction', 'comments']

    def save(self, version, mock_survey_data):
        instance = super(SurveyForm, self).save(commit=False)
        instance.mock_survey = MockSurvey(mock_survey_data)
        instance.version = version
        instance.save()
        return instance
