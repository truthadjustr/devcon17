from django.db import models

#from django.contrib.auth.models

###########
# new app applications
# new model Application
#  - fk: applicant: django.contrib.auth.models.User or 'auth.User'
#     example:
#       applicant = models.Foreignkey('auth.User')
#  - fk: job
#
# API:
# /v1/jobs/<pk>/apply/
# payload example: {'application_id':1}
#
#

# Create your models here.
'''
class Application(models.Model):
    #name = models.CharField(max_length=30)
    job = models.ForeignKey('jobs.Job',blank=True,null=True)
    #company = models.ForeignKey('companies.Company',blank=True,null=True)
    applicant = models.ForeignKey('auth.User')
    
    def __str__(self):
        return self.name
'''
