from django import forms
# from django.views.decorators.csrf import csrf_exempt
from django.core import validators

#additional validation can be parformed eg checcnking if input starts with z THEN PASS THE VALIDATOR IN CH

#def check_for_z(value):
    #if value[0].lower()!='z':
     #   raise forms.ValidationError("NAME NEEDS TO START WITH Z")





class FormName(forms.Form):
    name=forms.CharField()  #validators=[check_for_z] insert as an argument for manual validation
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter your email again')
    text=forms.CharField(widget=forms.Textarea)
   # manually... botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)
    botcatcher = forms.CharField(required=False,
                        widget=forms.HiddenInput,
                        validators=[validators.MaxLengthValidator(0)])
#manually usually not done
   # def clean_botcatcher(self):
       # botcatcher=self.cleaned_data['botcatcher']
      #  if len(botcatcher)>0:
      #      raise froms.validationError("GOTCHA BOT!")
       # return botcatcher 

# rather use built in django validation


    #to clean the entire form use method clean with super

    def clean(self):
        all_clean_data=super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email !=vmail:
            raise forms.ValidationError("Make sure emails match!")