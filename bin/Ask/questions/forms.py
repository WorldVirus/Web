from django import forms
from django.contrib.auth.models import User
from questions.models import UserProfile,Question
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

class UserForm(forms.Form):
    username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    avatar = forms.ImageField(label='Upload avatar')

    def clean_username(self):
        userName = self.cleaned_data['username']
        if len(userName)<2 or len(userName)>10:
            raise ValidationError("too short")
        return userName

    def clean_password(self):
        paswd = self.cleaned_data['password']
        if len(paswd)<3:
            raise ValidationError("too short")
        return paswd

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        user.save()
        return user

    def save_image(self):
        profile = UserProfile( avatar=self.cleaned_data['avatar'])
        profile.save()
        return profile
'''
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            w, h = get_image_dimensions(avatar)
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                       u'Please use an image that is '
                        '%s x %s pixels or smaller.' % (max_width, max_height))
                main, sub = avatar.content_type.split('/')
                if not (main == 'avatar' and sub in ['jpeg', 'pjpeg', 'gif', 'png','jpg']):
                    return ('/')


            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(u'Avatar file size may not exceed 20k.')

        except AttributeError:
            pass
        return avatar
'''

class QuestionForm(forms.ModelForm):
    class Meta:

        model=Question
        fields=['header','question_text','author']
        widgets = {
            'header':forms.TextInput(attrs={'class':'form-control'}),
            'question_text':forms.Textarea(attrs={'class':'form-control'}),

        }

        def __init__(self,*args,**kwargs):
            super(QuestionForm,self).__init__(*args,**kwargs)

        def save(self,comit=True):
            obj = super (QuestionForm,self).save(commit=False)
            if commit:
                obj.save()
            return obj
