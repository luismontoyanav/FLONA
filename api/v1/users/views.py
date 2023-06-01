from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from users.models import Employee


class EmployeesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Employee.objects.all()
        return Response({"employees list": "some"})
