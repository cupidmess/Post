from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class JobPost (models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(_("name"), max_length=50)
  job_title = models.CharField(_("job_title"), max_length=100)
  experience = models.IntegerField(_("experience"))
  desc = models.CharField(_("desc"), max_length=500)
  link = models.URLField(_("link"), max_length=200)
  skill_1 = models.CharField(_("skill_1"), max_length=50)
  skill_2 = models.CharField(_("skill_2"), max_length=50)
  skill_3 = models.CharField(_("skill_3"), max_length=50)
  payment = models.IntegerField(_("payment"))
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__ (self):
    return self.id