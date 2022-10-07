from .models import VolunteerDay, Comment , gadeget ,advertisement, report
from django import forms

class VolunteerDayForm(forms.ModelForm):
    class Meta:
        model = VolunteerDay
        fields = ('Supervisor','street','start','finish','date')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user','content')

class gadegetForm(forms.ModelForm):
    class Meta:
        model = gadeget
        fields = ('user', 'name', 'amount')

class advertisementForm(forms.ModelForm):
    class Meta:
        model = advertisement
        fields = ('user','title','content')

class reportForm(forms.ModelForm):
    class Meta:
        model = report
        fields = ('user','volDate','moneySpent','moneyDonated')
