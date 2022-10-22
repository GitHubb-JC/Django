from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from reviews.models import Review
from django.db.models import Q
from urllib.parse import urlparse
from urllib.request import urlopen

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    context = {
        "review": review,
        "comment_form": comment_form,
    }

    return render(request, "reviews/detail.html", context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review.save()
                return redirect("reviews:detail", review.pk)
        else:
            review_form = ReviewForm(instance=review)
    else:
        return redirect("reviews:index")
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        if request.user == review.user:
            review.delete()
            return redirect("reviews:index")
    return redirect("reviews:detail", review.pk)


@login_required
def comment_create(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect("reviews:detail", review.pk)
    return redirect("reviews:detail", review.pk)


@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        if request.method == "POST":
            comment.delete()
            return redirect("reviews:detail", review_pk)
    return redirect("reviews:detail", review_pk)


def search(request):
    all_data = Review.objects.order_by("-pk")
    search = request.GET.get("search", "")
    if search:
        search_list = all_data.filter(
            Q(title__icontains=search) | Q(movie_name__icontains=search)
        )

        context = {
            "search_list": search_list,
        }
    else:
        context = {
            "search_list": all_data,
        }

    return render(request, "reviews/search.html", context)
