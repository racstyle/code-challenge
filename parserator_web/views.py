import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        print('Getting the input...')

        # get the input from the front-end
        input_string = request.GET.get('address')
        print('Got the user input')

        # initializing
        address_components = {}
        address_type = ''

        # parse the input
        address_components, address_type = self.parse(input_string)

        # if there was an error parsing the input
        if not address_components and not address_type:
            raise ParseError('An error has occurred')

        # otherwise, return parsed response
        return Response({
            'input_string': input_string,
            'address_components': address_components,
            'address_type': address_type
        })

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        print('Parsing the address input...')

        # init
        apiResponse = {}            # USAddress API response (dictionary)
        address_components = {}     # address broken down as address_part:tag (dictionary)
        address_type = ''           # address type (string)

        # try parsing the address input
        try:
            apiResponse = usaddress.tag(address)  # parse input

            # first item is address broken down,
            # need to switch key:val pair since API returned as tag:address_part
            for tag, address_part in dict(apiResponse[0]).items():
                address_components[str(address_part)] = str(tag)

            # second item is input type
            address_type = apiResponse[1]

            print('Successfully parsed the address input')

            return address_components, address_type
        except Exception:
            print('Error parsing the address input')
            return None, None
