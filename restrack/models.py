from django.db import models
from datetime import datetime

# Create your models here.

FACILITY_TYPES = (
	('ADC', 'Adult Day Care'),
	('LTHHCP', 'Long Term Home Health Program'),
	('NH', 'Nursing Home')
)

# Facility Model
class Facility (models.Model):
	facility_name = models.CharField(max_length=400)
	facility_type = models.CharField(choices=FACILITY_TYPES, max_length=100)
	address = models.CharField(max_length=400, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zip = models.IntegerField(null=True)
	bed_capacity = models.IntegerField(null=True)
	respite_bed = models.IntegerField(default=0, null=True)
	administrator_name = models.CharField(max_length=200, null=True)
	administrator_license_number = models.CharField(max_length=100, null=True)
	doctor_name = models.CharField(max_length=200, null=True)
	doctor_npi = models.IntegerField(null=True)
	operating_cert = models.CharField(max_length=8, null=True)
	facility_npi = models.CharField(max_length=9, null=True)
	tax_id = models.IntegerField(null=True)
	bank_account_number = models.CharField(max_length=30, null=True)
	bank_routing_number = models.CharField(max_length=40, null=True)
	medicaid_number = models.IntegerField(null=True)
	medicare_ptan = models.IntegerField(null=True)
	upin = models.IntegerField(null=True)
	pps_start_date = models.DateTimeField(default=datetime.now, blank=True)
	medicare_m2_id = models.IntegerField(null=True)
	facility_state_assigned_unique_id = models.IntegerField(null=True)
	unique_state_id = models.IntegerField(null=True)
	state_id = models.IntegerField(null=True)
	state_number = models.IntegerField(null=True)
	federal_number = models.IntegerField(null=True)
	status = models.IntegerField(default=1, null=True)
	create_date = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__ (self):
		return self.facility_name

# Residents Model
class Residents (models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	facility_id = models.ForeignKey(Facility)
	admission_date = models.DateTimeField('date of admission')
	discharge_date = models.DateTimeField('date of discharge')
	payer_source = models.CharField(max_length=200)
	bed_number = models.IntegerField()
	
	def __str__(self):
		return self.first_name