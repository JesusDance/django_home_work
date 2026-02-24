from lesson_5.models import Client, Products
from django import forms


CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
GENDER_CHOICES = [("1", "Male"), ("2", "Female")]
GAME_GENRE = [("1", "rpg"), ("2", "arcade"), ("3", "shooter")]


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            #два варіанта. 1й більше використовують
            #"bitrhday": forms.DateInput(attrs={"type": "date"}),
            "birthday": forms.SelectDateWidget(
                years=range(1900, 2027)
            )
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class ClientResponseForm(forms.Form):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    grade = forms.ChoiceField(choices=CHOICES)
    response_type = forms.BooleanField(required=False,
                                       help_text="Please enter your negative or positive response")
    number_phone = forms.IntegerField(required=False)


class ClientRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=64)
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput,
                               max_length=64,
                               min_length=5)
    email = forms.EmailField(required=True,
                             error_messages={"required": "Please enter your real email address"})
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    photo = forms.ImageField(label="Passport photo",
                             required=False,
                             help_text="Please put your photo")


class GameForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=True)
    genre = forms.ChoiceField(choices=GAME_GENRE, required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    discount = forms.FloatField(required=False, initial=5.25)
