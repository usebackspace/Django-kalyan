from  django import forms

class MarvelForm(forms.Form):
    name= forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password Again'}))
    
    # def clean_name(self):

    #     validate_name = self.cleaned_data['name']

    #     if len(validate_name)>5:
    #         raise forms.ValidationError('Enter name less than 5 character')

    def clean(self):

        cleaned_data = super().clean()

        val_name = cleaned_data['name']
        val_email = cleaned_data['email']
        
        val_pass = cleaned_data['password']
        con_pass = cleaned_data['confirm_password']


        # if len(val_name)>5:
        #     raise forms.ValidationError('Enter name less than 5 character')
        
        # if len(val_email)>10:
        #     raise forms.ValidationError('Enter email less than 10 character')

        if val_pass!=con_pass:
            raise forms.ValidationError('Password Doesn"t match')