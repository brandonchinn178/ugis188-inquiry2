from django.db import models

import random, json

from base.fields import MockSurveyFormField

MEMES = {
    'Bad Luck Brian': 'http://s2.quickmeme.com/img/1e/1e797a2ea3c4001c7c5d6d08736a0c8ca4c68b497a3f4c93cdf0594130bff486.jpg',
}

class MockSurvey(object):
    """
    The class wrapping a dictionary mapping the name of a meme to the user's
    responses to the meme.
    """
    def __init__(self, data):
        if data is None:
            self.data = {
                meme: {
                    'funny': None,
                    'relevance': None,
                }
                for meme in MEMES.keys()
            }
        else:
            self.data = data

    def random_memes(self):
        """
        Return a list of Memes in a random order
        """
        memes = self.data.keys()
        random.shuffle(memes)
        return memes

class MockSurveyField(models.TextField):
    """
    A field to convert a MockSurvey to save into a database
    """
    def __init__(self, *args, **kwargs):
        # initializes an empty MockSurvey for a default
        kwargs['default'] = MockSurvey()

        super(MockSurveyField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, MockSurvey) or value is None:
            return value

        data = json.loads(value)
        return MockSurvey(data)

    def get_prep_value(self, value):
        if isinstance(value, MockSurvey):
            return json.dumps(value.data)
        else:
            return value

class Survey(models.Model):
    mock_survey = MockSurveyField()

    # survey questions
    name = models.CharField(max_length=255)
    perception = models.PositiveSmallIntegerField()
    satisfaction = models.PositiveSmallIntegerField()
    comments = models.TextField()

    # logistics
    version = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
