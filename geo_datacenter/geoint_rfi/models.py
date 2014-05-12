from django.db import models

# Create your models here.
class Operation(models.Model):
	name = models.Charfield(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class RFI(models.Model):
	operation = models.ForeignKey(Operation)

	number = models.IntegerField() #not quite sure how to go about this. need to be in numerical order
	
	submission_date = #not sure about this one either. need to get a time stamp.

	suspense_date = #user would enter in a date here.

	LIOTV = # again user would enter a date 

	description = models.Charfield(max_length=500) #user enters what questions they want answered by the rfi

	POC = models.Charfield(max_length=128)

	POC_phone = models.Charfield(max_lenght=10)

	status = models.ForeignKey(Status)

	jpegs = models.IntegerField(default=0)
	
	assigned = models # this one need to whatever analyst is assigned to the task

	qa_qc = #same as above, except who qc'd it 
	
	classification = models.ForeignKey(classification)




"""

database objects


Operation
RFI
Country
finished jpegs
rfi status
classification

"""

