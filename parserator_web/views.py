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
        
        input_string = request.GET.get('address')    # get the input from the front-end
        address_components = {}
        address_type = ''
        
        print('request string:', input_string)
        
        print('running parse:')
        address_components, address_type = self.parse(input_string)
        print(address_components)
        print(address_type)
        print('end of parse')
            
        return Response({'input_string': input_string, 'address_components': address_components, 'address_type': address_type})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        
        print('address:', address)
        
        # init
        apiResponse = {}            # USAddress API response (dictionary)
        address_components = {}     # address parsed broken down into address_part:tag (switched fr init, see below) (dictionary)
        address_type = ''           # address type (string)
        
        # try parsing the address input
        try:
            apiResponse = usaddress.tag(address)  # parse input
            
            address_components = { str(address_part):str(tag) for tag,address_part in dict(apiResponse[0]).items() }     # first item is address broken down, need to switch key:val pair since API returned as tag:address_part
            address_type = apiResponse[1]         # second item is input type
            
            print('components:', address_components)
            print('type:', address_type)
            
            return address_components, address_type
        except:
            print('Error parsing the address input')
            return None, None
        
        