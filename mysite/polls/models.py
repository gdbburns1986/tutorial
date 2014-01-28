from django.db import models
from django.utils import timezone

import datetime

#Poll contains a question and a publication date
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
    
    #custom method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Each choice is associated with a Poll
#Contains a tally and a choice
class Choice(models.Model):
    #ForiegnKey tells django that each choice
    #is related to a single Poll
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
