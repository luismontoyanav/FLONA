from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    id = serializers.IntegerField()
    birth_date = serializers.DateField()
    photo = serializers.CharField(allow_null=True)
    date_joined = serializers.DateField()
    last_modified = serializers.DateField()
    phone = serializers.CharField()
    street = serializers.CharField()
    state = serializers.CharField()
    city = serializers.CharField()
    neighborhood = serializers.CharField()
    zip_code = serializers.CharField()
    salary = serializers.DecimalField(max_digits=5, decimal_places=2)
