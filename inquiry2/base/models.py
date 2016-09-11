from django.db import models

import random, json

# map slug to URL of meme
MEMES = {
    'bad-luck-brian': 'http://s2.quickmeme.com/img/1e/1e797a2ea3c4001c7c5d6d08736a0c8ca4c68b497a3f4c93cdf0594130bff486.jpg',
}

def random_memes():
    """
    Returns a list of memes in a random order
    """
    memes = MEMES.items()
    random.shuffle(memes)
    return memes

class MockSurvey(object):
    """
    The class wrapping a dictionary mapping the slug of a meme to the user's
    responses to the meme.
    """
    def __init__(self, data):
        self.data = data

class MockSurveyField(models.TextField):
    """
    A field to convert a MockSurvey to save into a database
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            'null': True,
        }
        defaults.update(kwargs)
        super(MockSurveyField, self).__init__(*args, **defaults)

    def to_python(self, value):
        if isinstance(value, MockSurvey) or value is None:
            return value

        data = json.loads(value)
        return MockSurvey(data)

    def get_prep_value(self, value):
        if isinstance(value, MockSurvey):
            return json.dumps(value.data)
        elif value is None:
            return None # save None instead of ''
        else:
            raise ValueError('MockSurveyField requires an instance of MockSurvey')

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
