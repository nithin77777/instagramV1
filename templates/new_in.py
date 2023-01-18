from defines import getCreds, makeApiCall


def getUserMedia(params):
    """ Get users media

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,likes,comments,total_interactions,follows,shares,profile_visits,profile_activity'  # fields to get back
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'  # endpoint url

    return makeApiCall(url, endpointParams, params['debug'])  # make the api call


def getMediaInsights(params):
    """ Get insights for a specific media id

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}
    Returns:
        object: data from the endpoint
    """
    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['metric'] = params['metric']  # fields to get back
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['latest_media_id'] + '/insights'  # endpoint url
    print('The URL is',url)

    return makeApiCall(url, endpointParams, params['debug'])  # make the api call


def getUserInsights(params):
    """ Get insights for a users account

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['metric'] = 'impressions,reach'  # fields to get back
    endpointParams['period'] = 'days_28'  # period
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['instagram_account_id'] + '/insights'  # endpoint url

    return makeApiCall(url, endpointParams, params['debug'])  # make the api call


params = getCreds()  # get creds
response = getUserMedia(params)  # get users media from the api
print(response)


highlights = 'IMAGE'
for highlights in response['json_data']['data']:
    print("\n---- LATEST POST -----\n")  # section header
    print(highlights)
    print('Post ID : ', highlights['id'])
    try:
        print('MEDIA TYPE : ', highlights['media_type'])
    except:
        pass

    try:
        print('PERMALINK: ', highlights['permalink'])
    except:
        pass

    try:
        print("CAPTION: ", highlights['caption'])
    except:
        pass

    try:
        print(highlihgts['caption'])
    except:
        pass
    try:
        print("POSTED AT: ", highlights['timestamp']+'\n')
    except:
        pass



    params['latest_media_id'] = highlights['id']  # store latest post id

    if 'VIDEO' == highlights['media_type']:  # media is a video
        params['metric'] = 'engagement,impressions,reach,saved,video_views'
    else:  # media is an image
        params['metric'] = 'engagement,impressions,reach,saved,comments,likes,total_interactions,follows,shares,profile_visits,profile_activity,'

        response = getMediaInsights(params)  # get insights for a specific media id

        print( "\n---- LATEST POST INSIGHTS -----\n" )  # section header
    try:
        for insight in response['json_data']['data']:  # loop over post insights
            # print(insight)
            print( "\t" + insight['title'] + " (" + insight['period'] + "): " + str(insight['values'][0]['value']) )  # display info
    except:
        pass


    response = getUserInsights(params)  # get insights for a user
    print(response)

print( "\n---- DAILY USER ACCOUNT INSIGHTS -----\n" )  # section header

for insight in response['json_data']['data']:  # loop over user account insights
    # print(insight)
    print( "\t" + insight['title'] + " (" + insight['period'] + "): " + str(insight['values'][0]['value']) )  # display info

    for value in insight['values']:  # loop over each value
        print( "\t\t" + value['end_time'] + ": " + str(value['value']) )  # print out counts for the date



