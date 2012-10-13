from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from Accounts.models import UserProfile
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.decorators import login_required
from Accounts.forms import RegistrationForm
from Accounts.forms import LoginForm
import datetime, random, sha

def register(request):
	if request.method=="POST":
	   registerform=RegistrationForm(request.POST)

	   if request.user.is_authenticated():
		# They already have an account; don't let them register again
			 return render_to_response('register.html', {'has_account': True})
	else:
		   registerform=RegistrationForm()
	return render_to_response('Accounts/register.html',{ 'form':registerform})

@csrf_exempt
def register(request):
	if request.POST:
		regForm = RegistrationForm(request.POST)
		
		if request.user.is_authenticated():
			return render_to_response('Accounts/register.html',{'has_account':True})
		
		new_data = request.POST.copy()
		errors = regForm.get_validation_errors(new_data)
		
		if not errors:
			# save the user
			regForm.do_html2python(new_data)
			new_user = regForm.save(new_data)
			# Build the activation key for their account  
			salt = sha.new(str(random.random())).hexdigest()[:5]
			activation_key = sha.new(salt+new_user.username).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)
			 
			# Create and save their profile
			new_profile = UserProfile(user = new_user, activation_key = activation_key,key_expires=key_expires)
			new_profile.save 
		
	
	else:
		   regForm=RegistrationForm()
	return render_to_response('Accounts/register.html',{ 'form':regForm})

#activating new account
@csrf_exempt
def confirm(request, activation_key):
	if request.user.is_authenticated():
		return render_to_response('confirm.html', {'has_account': True})
	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
	if user_profile.key_expires < datetime.datetime.today():
		return render_to_response('confirm.html', {'expired': True})
	user_account = user_profile.user
	user_account.is_active = True
	user_account.save()
	return render_to_response('confirm.html', {'success': True})
	pass
@csrf_exempt	
def login(request):
	if request.POST:
		form = LoginForm(request.POST)
		
		#capturing username and password
		username = request.POST['username']
		password = request.POST['password']
		
		#authenticate user
		
		user = authenticate(username= username, password = password)
		
		# checking if user exists
		
		if user is not None:
			if user.is_active:
			
				login(request, user)
				return HttpReponseRedirect(request.path)
			else: 
				return HttpResponse('Account can not be verified')
		else:
			form = LoginForm()
			return render_to_response('Accounts/login.html',{'form': form,'logged_in': request.user.is_authenticated()})
	else:
		form = LoginForm()
	return render_to_response('Accounts/login.html', {'form': form, 'logged_in': request.user.is_authenticated(),'users':request.user})
	
@csrf_exempt
def logout(request):
	logout(request)
	return render_to_response('Accounts/logout.html')	
		
		

