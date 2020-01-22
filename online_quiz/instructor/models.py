from django.db import models

"""
Type 0 - True/False
Type 1 - Multiple Choice questions
Type 2 - Essay type
"""


class Questions(models.Model):
    quiz_id = models.CharField(max_length=40, null=True)
    question = models.TextField(null=True)
    question_type = models.IntegerField(null=True)
    op1 = models.CharField(max_length=40, null=True)
    op2 = models.CharField(max_length=40, null=True)
    op3 = models.CharField(max_length=40, null=True)
    op4 = models.CharField(max_length=40, null=True)
    ans = models.CharField(max_length=40, null=True)
    weightage = models.IntegerField(null=True)

    def __str__(self):
        return self.question

