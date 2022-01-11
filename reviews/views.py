from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from reviews.forms import ReviewForm


class ReviewView(View):
    @staticmethod
    def get(request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form,
        })

    @staticmethod
    def post(request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form,
        })


# def reviews(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = Review(user_name=form.cleaned_data['user_name'], review=form.cleaned_data['review_text'],
#                             rating=form.cleaned_data['rating'])
#             review.save()
# form.save()
# return HttpResponseRedirect("/thank-you")
# else:
#     form = ReviewForm()
# return render(request, "reviews/review.html", {
#     "form": form,
# })


def thank_you(request):
    return render(request, "reviews/thank-you.html")
