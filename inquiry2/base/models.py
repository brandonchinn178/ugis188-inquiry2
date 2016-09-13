from django.db import models
from django.utils import timezone

import json
from collections import OrderedDict

# list of slugs, needs an image at static/img/<slug>.jpg
MEMES = [
    'bad-luck-brian',
    # 'drunk-baby',
    # 'bsian',
]

class Survey(models.Model):
    # store all meme questions in one big json text field
    mock_survey = models.TextField()

    # survey questions
    name = models.CharField(max_length=255)
    perception = models.PositiveSmallIntegerField()
    satisfaction = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True)

    # logistics
    version = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def set_mock_survey(self, data):
        self.mock_survey = json.dumps(data)

    def get_mock_survey(self):
        return json.loads(self.mock_survey)

    def serialize(self):
        """
        Convert this object into a dictionary that will be converted into
        a JSON string
        """
        # convert to local timezone
        timestamp = timezone.localtime(self.timestamp)

        return OrderedDict([
            ('name', self.name),
            ('version', self.version),
            ('perception', self.perception),
            ('satisfaction', self.satisfaction),
            ('mock_survey', self.get_mock_survey()),
            ('comments', self.comments),
            ('timestamp', timestamp.strftime('%-m/%d [%H:%M:%S]')),
        ])
