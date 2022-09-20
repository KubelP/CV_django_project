from django import forms
from jpportfolio.models import Comments, Contact

class CommentsForm(forms.ModelForm):
    comment_body = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder': 'Leave a comment!'}))
    class Meta:
        model = Comments
        fields = ('author', 'comment_body')
        labels = {
            'author': False
        }

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your name'})
        }

class ContactForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    e_mail = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Your e-mail'}))
    contact_body = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder': 'Leave a message!'}))
    class Meta:
        model = Contact
        fields = ('name', 'e_mail', 'contact_body')



