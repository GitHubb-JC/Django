from tkinter import Widget
from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "movie_name",
            "title",
            "content",
            "grade",
        ]
        labels = {"title": "제목", "content": "내용", "movie_name": "영화 제목", "grade": "평점"}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(attrs={"class": "from-control", "rows": 1}),
        }
        labels = {
            "content": "댓글",
        }
