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
        print('request string:', input_string)
        
        print('running parse:', self.parse(input_string))
        
            
        return Response({'input_string': input_string})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        
        print('address:', address)
        
        # init
        address_components = []     # address broken down into components (list)
        address_type = []           # address component type (list)
        parsedAddr = {}             # address parsed (dictionary)
        
        # try parsing the address input
        try:
            parsedAddr = usaddress.tag(address)[0]
            
            print(parsedAddr)
            
            address_components = list(parsedAddr.values())
            address_type = list(parsedAddr.keys())
            
            print('components:', address_components)
            print('type:', address_type)
        except:
            print('Error parsing the address input')
        
        return address_components, address_type
        