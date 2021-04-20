import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from tendo_django.core.managers import UserManager

class TimestampModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False,
                                      db_index=True,
                                      verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, editable=False,
                                      db_index=True,
                                      verbose_name=_('Updated at'))

    class Meta:
        abstract = True

class Hospital(TimestampModel):
  name = models.CharField(_('Name'), max_length=500)

class Patient(TimestampModel, AbstractBaseUser):
  SUPER = 1
  ADMIN = 2
  PHYSICIAN = 3
  PATIENT = 4
  ROLES = (
      (SUPER, 'super'),
      (ADMIN, 'admin'),
      (PHYSICIAN, 'physician'),
      (PATIENT, 'patient')
  )
  MALE = 1
  FEMALE = 2
  OTHER = 3
  GENDERS = (
      (MALE, 'male'),
      (FEMALE, 'female'),
      (OTHER, 'other')
  )
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.EmailField(_('Email'), unique=True, max_length=500)
  first_name = models.CharField(_('First Name'), max_length=255)
  last_name = models.CharField(_('Last Name'), max_length=255)
  phone = models.CharField(_('Phone'), max_length=255, null=True)
  is_active = models.BooleanField(_('Is Active'), default=True)
  is_admin = models.BooleanField(_('Is Admin'), default=False)
  date_of_birth = models.DateField(_('Date of Birth'), null=True)
  role = models.PositiveSmallIntegerField(_('Role'), choices=ROLES, default=PATIENT)
  gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDERS, default=None, null=True)
  
  objects = UserManager()

  USERNAME_FIELD = 'email'

  class Meta:
        ordering = ['first_name', 'last_name', ]
  
  def __str__(self):
        return self.get_full_name()

  @property
  def is_staff(self):
      return self.is_admin

  def get_full_name(self):
      return '%s %s' % (self.first_name, self.last_name)

  def has_perm(self, perm, obj=None):
      return self.is_admin

  def has_module_perms(self, app_label):
      return self.is_admin

  @property
  def full_name(self):
      return self.get_full_name()
  
class Physician(TimestampModel):
  email = models.EmailField(_('Email'), unique=True, max_length=500)
  first_name = models.CharField(_('First Name'), max_length=255)
  last_name = models.CharField(_('Last Name'), max_length=255)
  phone = models.CharField(_('Phone'), max_length=255, null=True)
  title = models.CharField(_('Title'), max_length=255, null=True)
  prefix = models.CharField(_('Prefix'), max_length=255, null=True)
  hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)

  
class Appointment(TimestampModel):
  physician = models.ForeignKey(Physician, null=True, on_delete=models.SET_NULL)
  patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
  time_start = models.DateTimeField()
  time_end = models.DateTimeField()
  note = models.CharField(_('Note'), max_length=500, null=True)

class Diagnosis(TimestampModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
  appointment = models.ForeignKey(Appointment, null=True, on_delete=models.SET_NULL)

  name = models.CharField(_("Name"), max_length=500)

class FeedbackSurvey(TimestampModel):
  appointment = models.ForeignKey(Appointment, null=True, on_delete=models.SET_NULL)
  physician_rating = models.PositiveIntegerField()
  understanding = models.CharField(max_length=255)
  understanding_notes = models.TextField(null=True)
  patient_expression = models.TextField(null=True)

@receiver(post_save, sender=Patient)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)