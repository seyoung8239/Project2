from django.urls import path
from .views import BoardList, BoardDetail, BoardDetailVoteUp

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/voteup/<int:pk_alt>', BoardDetailVoteUp.as_view()),
]
