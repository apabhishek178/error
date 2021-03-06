from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from tweet.models import Tweet
from .serializers import TweetModelSerializer

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):

    serializer_class = TweetModelSerializer

    def get_queryset(self):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            #searching for the searched content in the tweet and return the tweet if found
            #checkout making queries in database from django documentation
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
            )
        return  qs
