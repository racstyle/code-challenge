import pytest


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    print(address_string)

    expected_output = {
        'input_string': '123 main st chicago il',
        'address_components': {
            '123': 'AddressNumber',
            'main': 'StreetName',
            'st': 'StreetNamePostType',
            'chicago': 'PlaceName',
            'il': 'StateName'
        },
        'address_type': 'Street Address'
    }

    try:
        res = client.get(f'/api/parse/?address={address_string}', format='json')
        print(res.json())
        print(res.json()['input_string'])

        assert res.json()['input_string'] == expected_output['input_string']
        assert res.json()['address_components'] == expected_output['address_components']
        assert res.json()['address_type'] == expected_output['address_type']
    except Exception:
        pytest.fail()


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'

    try:
        res = client.get(f'/api/parse/?address={address_string}', format='json').json()
        print(res)
        assert res == {'detail': 'An error has occurred'}
    except Exception:
        pytest.fail()
