from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import IsAuthenticated
from api.v1.users.serializers import EmployeeSerializer

from api.v1.users.services import get_all_employees


class EmployeesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = get_all_employees()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
