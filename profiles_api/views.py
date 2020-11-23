from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIEW"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            '1111111111111111111111',
            '2222222222222222222222',
            '3333333333333333333333',
            'sosi huy pidrila',
        ]

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})
