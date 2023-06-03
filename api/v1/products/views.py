from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import IsAuthenticated

from api.v1.products.services import get_product_type_by_uuid


class ProductView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = get_product_type_by_uuid(product_type_uuid=request.data["product_type_uuid"])
        return Response(data={"data": "some"}, status=status.HTTP_200_OK)
