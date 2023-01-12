import requests
import json


def getCreds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """

    creds = dict()  # dictionary to hold everything
    # creds['access_token'] = 'EAArzIaDdM60BABy25jm83ZAFZBaMI8cCBKdwaadtbHuJNwB9UYlwZARfvpa4VC5uZAmXnSVhGYqwDt4FZBZAcM2If9IV1T68cDtFxGZBMBOxGQnDJtg6EzZAtDBuM2wYfZC3lnrblhHs0S2ZCWyB8PzAuWWCbaeZAAJDbutON3RQHCRk5xOUlZAjUs05swYMWIS8IiT3kcutPbiWLYjY1BZAbpnQS'  # access token for use with all api calls
    creds['access_token'] = 'EAArzIaDdM60BABLJGijhsBMaHTE6Q77HTZCMGNBr2KoKNsZBsOkaOcZCJgGjZBrAwgAR8lY7ZAKWgtxY0Nr1mCVObkQnHqSauWSdCgWAOwVYZCUI0uZC9UAx03DDKdvnS5LA2Quw3U03Sn1HIHR7OsBpxn1RBgMHUFHkiijqNtrAQ39S7e6OZCW4dKjZAGgqhX5Hs6FBAukqsn8DElrR5zd6E'  # access token for use with all api calls
    creds['client_id'] = '3082075525428141'  # client id from facebook app IG Graph API Test
    creds['client_secret'] = 'f0237c5b16c45b6dd80cc50f9f36d6c1'  # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v6.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'  # base endpoint with domain and version
    creds['debug'] = 'no'  # debug mode for api call
    creds['page_id'] = '108483032130694'  # users page id
    creds['instagram_account_id'] = '17841456927336966'  # users instagram account id
    creds['ig_username'] = 'capnxtglobaltech'  # ig username

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """

    data = requests.get(url, endpointParams)  # make get request

    response = dict()  # hold response info
    response['url'] = url  # url we are hitting
    response['endpoint_params'] = endpointParams  # parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    if ('yes' == debug):  # display out response info
        displayApiCallData(response)  # display response

    return response  # get and return content


def displayApiCallData(response):
    """ Print out to cli response from api call """

    print( "\nURL: " )  # title
    print( response['url'] )  # display url hit
    print( "\nEndpoint Params: " )  # title
    print( response['endpoint_params_pretty'] )  # display params passed to the endpoint
    print( "\nResponse: " )  # title
    print( response['json_data_pretty'] )  # make look pretty for cli
print('defines complete')