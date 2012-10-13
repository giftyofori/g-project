from django import forms

COURSES = (('Sci', 'SCIENCE'),
             ('Bus', 'BUSINESS'))
class RegistrationForm(forms.Form):
	#username = forms.RegexField(label = ' Choose a username',regex = r'^\w+$', max_length = 30 )
	username = forms.RegexField(regex=r'^\w+$', max_length=30,widget=forms.TextInput())
	email = forms.EmailField(label = 'Your current email address')
	password1 = forms.CharField(label = 'Create a Password',widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Comfirm your created password',help_text = 'Re-type password',widget = forms.PasswordInput)
	course = forms.MultipleChoiceField(label= 'Course(s)',required = False, widget=forms.CheckboxSelectMultiple, choices = COURSES)
	phone_number = forms.IntegerField(label = 'Phone Number', required = False)
	
	
	def inValidUsername(self,field_data , all_data):
		try:
			User.objects.get(username = field_data)
		except User.DoesNotExist:
			return 
		raise validators.ValidationError('The username ',field_data ,'is not available')
		
	def save(self, new_data):
		user = User.objects.create_user(new_data['username'], new_data['email'], new_data['password1'])
		user.is_active = False
		user.save()
		return user
		
		
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
		
		