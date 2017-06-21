import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()

        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now
        # todo why does this work?

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.Boolean = True
    was_published_recently.short_description = 'Published recently1234?'

    # def image_tag(self):
    #     return u'<img src="%s" />' % self.hint_image
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

class HintImage(models.Model):
    hint = models.ForeignKey(Question, related_name='images')
    hint_image = models.FileField(max_length=255, upload_to='images', default='missing')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
