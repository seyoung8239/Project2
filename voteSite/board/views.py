from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer
from rest_framework import generics, permissions, status
from .permission import IsOwnerOrReadOnly


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BoardDetailVoteUp(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, pk_alt, *args, **kwargs):
        instance = self.get_object()
        serializer = BoardSerializer(data=instance)
        vote = instance.vote
        # if self.request.user
        if vote['data'].length() < pk_alt:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        vote['data'][pk_alt][1] += 1
        instance.vote = vote
        serializer.is_valid()
        instance.save()

        return Response(serializer.data)
