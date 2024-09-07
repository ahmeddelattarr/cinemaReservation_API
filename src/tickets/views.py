from rest_framework import status, viewsets,filters
from .models import Movie,Guest,Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer

# Create your views here.
@api_view(['GET','POST'])

def FBV_List(request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
#post-put-get
def FBV_PK(request,pk):
    try :
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=GuestSerializer(guest)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#better approach

class ViewsetsGuest(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class = GuestSerializer
class ViewsetsMovie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['movie']

class ViewsetsReservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer













