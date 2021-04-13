from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StarObject, NotStarObject
from .serializers import StarListSerializer, NotStarListSerializer


class AstroObjectListView(APIView):
    """
    Вывод списка всех астрономических объектов
    """

    @staticmethod
    def get(request):
        star_objects = StarObject.objects.all()
        non_star_objects = NotStarObject.objects.all()
        instances = StarListSerializer(star_objects, many=True).data
        instances += NotStarListSerializer(non_star_objects, many=True).data
        return Response(instances)
