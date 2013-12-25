from django.db import models
import datetime
from django.utils import timezone

class SqlTable(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

class TableRow(models.Model):
    poll = models.ForeignKey(SqlTable)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
