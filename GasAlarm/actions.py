from django.shortcuts import render
import logging

LOGGER = logging.getLogger(__name__)

def setPhoneNumber(request):
	context = {}
	if request.method == 'GET':
		# display the form with current phone number
		LOGGER.info("requested to show set phone number page")
		try :
			f = open("currentPhoneNumber","r")
			context['currentPhoneNumber'] = f.readline()
			f.close()
		except :
			LOGGER.debug("cannot get currentPhoneNumber")
	elif request.method == 'POST':
		# change phone number
		LOGGER.info("requested to change phone number")
		try :
			LOGGER.info("requested to change phone number")
			phoneNumber = request.POST.get('phoneNumber', "")
			f = open("currentPhoneNumber","w")
			f.write(phoneNumber)
			f.close()
			context['currentPhoneNumber'] = phoneNumber
		except :
			LOGGER.debug("cannot set phoneNumber")

	return render(request, 'setPhoneNumber.html', context)
