from django import forms

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Max Length is 100"
#     })
#     review_text = forms.CharField(label="Your FeedBack", widget=forms.Textarea, max_length=255)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'review': 'Your Review',
            'rating': 'Rating'
        }
        error_messages = {
            'user_name': {
                "required": "Your name must not be empty",
                "max_length": "Max Length is 100"
            }
        }
