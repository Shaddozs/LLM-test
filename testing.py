from ibm_cloud_sdk_core import IAMTokenManager

api_key = "FBDKpxKGSvBA1rYGf4MHWrnZXVHeREWpJfMPLrscfNbn"  # Replace with your actual API key
iam_url = "https://iam.cloud.ibm.com/identity/token"

try:
    token_manager = IAMTokenManager(apikey=api_key, url=iam_url)
    access_token = token_manager.get_token()
    print("Access Token:", access_token)
except Exception as e:
    print("Error:", e)