from allauth.account.forms import SignupForm,LoginForm,ChangePasswordForm
from colorfield.widgets import ColorWidget
from colorfield.fields import ColorField
from django import forms
from .models import Profile,Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from colorfield.widgets import ColorWidget
from allauth.account.forms import ResetPasswordKeyForm

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['remember'].widget.attrs['checked'] = 'checked'

class AccountDetails(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["GithubURL","tiktokURL",'instagramURL','youtubeURL','linkedinURL','twitterURL','FacebookURL','FirstName','LastName','Email','PhoneNumber','Address','Country']
    def __init__(self, *args, **kwargs):
        super(AccountDetails, self).__init__(*args, **kwargs)
        self.fields['GithubURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Username Github',

        })
        self.fields['tiktokURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Username Tiktok',

        })
        self.fields['instagramURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Username instagram',

        })
        self.fields['youtubeURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Link Youtube',

        })
        self.fields['linkedinURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Link linkedin',

        })
        self.fields['twitterURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Username Twitter',

        })
        self.fields['FacebookURL'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Link Facebook',

        })
        self.fields['FirstName'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'First Name',

        })
        self.fields['LastName'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Last Name',

        })
        self.fields['Email'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Email',

        })
        self.fields['PhoneNumber'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Phone Number',

        })
        self.fields['Address'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Address',

        })
        self.fields['Country'].widget.attrs.update({
            'class': 'input-data',
            'placeholder': 'Country',

        })
        

class UsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']
    def __init__(self, *args, **kwargs):
            super(UsernameForm, self).__init__(*args, **kwargs)
        
            self.fields['username'].widget.attrs.update({
                'id': 'input-username',
                'class':'input-data'
            })



class PhotoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photoProfile']
        widgets = {
            'photoProfile': forms.widgets.FileInput(attrs={'id': 'file-input'})
        }
    # def __init__(self, *args, **kwargs):
    #     super(PhotoProfileForm, self).__init__(*args, **kwargs)
    
    #     self.fields['photoProfile'].widget.attrs.update({
    #         'id': 'file-input',
    #     })

class ChangePasswordMyForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
                'class':'input-data',
                'placeholder':'Current Password'
            })
        self.fields['password1'].widget.attrs.update({
                'class':'input-data',
                'placeholder':'New Password'
            })
        self.fields['password2'].widget.attrs.update({
                'class':'input-data',
                'placeholder':'Confirm New Password'
            })
        # self.fields['oldpassword'].widget.attrs['class'] = 'my-custom-class'
        # self.fields['password1'].widget.attrs['class'] = 'my-custom-class'
        # self.fields['password2'].widget.attrs['class'] = 'my-custom-class'


class UpdataItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["text",'image','url','showPhoto']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
                'class':'input-Item',
                'placeholder':'add anything'
            })    
        self.fields['url'].widget.attrs.update({
                'class':'input-Item',
                'placeholder':'add Url'
            })  
        self.fields['showPhoto'].widget.attrs.update({
                'class':'cyberpunk-checkbox',
                'placeholder':'add Url'
            })  
class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["text",'image','url','showPhoto']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
                'class':'input-Item',
                'placeholder':'add anything'
            })    
        self.fields['image'].widget.attrs.update({
                'id':'additem',
            })    
        self.fields['url'].widget.attrs.update({
                'class':'input-Item',
                'placeholder':'add Url'
            })  
        self.fields['showPhoto'].widget.attrs.update({
                'class':'cyberpunk-checkbox',
                'placeholder':'add Url'
            })  

class StyleItem(forms.ModelForm):
    # gradientOne = ColorField()
    class Meta:
        model= Item
        fields = ['gradientoption',"gradientOne",'gradientTwo', 'backgroundbox','BackgroundBlur','BackgroundBlurActive','backgoundActive']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['BackgroundBlur'].widget.attrs.update({
                'class':'input-Item',
                'placeholder':'Enter Value Blur'
            })


class ProfileCustomizer(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["BackgroundProfile",'gradientActive','BackgroundBlur','gradientOne','gradientTwo','gradientoption','Description','colorDescription']
        widgets = {
            'BackgroundProfile': forms.widgets.FileInput(attrs={'class': 'input-backgroundProfile'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['BackgroundProfile'].widget.attrs.update({
        #         'class':'input-backgroundProfile',
        #     })
        self.fields['BackgroundBlur'].widget.attrs.update({
                'class':'input-Item input',
                'placeholder':"Enter Value Blur"
            })
        self.fields['gradientActive'].widget.attrs.update({
                'class':'inp-cbx',
                'id':"morning"
            })
        self.fields['Description'].widget.attrs.update({
                'class':'textarea-des',
                'placeholder':"Description"
            })
        # self.fields['colorDescription'].widget.attrs.update({
        #         'id':'likeone'
        #     })
        
    
# forms.py


class CustomPasswordResetForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add class names to form fields
        self.fields['password1'].widget.attrs['class'] = 'input-password'
        self.fields['password2'].widget.attrs['class'] = 'input-password'
        self.fields['password1'].widget.attrs['placeholder'] = 'New Password Min 8'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['password2'].widget.attrs['disabled'] = True
