from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context=context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect("reviews:detail", review.pk)

    else:
        review_form = ReviewForm(instance=review)

    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    if request.method == "POST":
        Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")
