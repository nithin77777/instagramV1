'json_data': {'data': [{'id': '17987651149656395'

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My First Campaign',
  'objective': 'PAGE_LIKES',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print AdAccount(id).create_campaign(
  fields=fields,
  params=params,
)

