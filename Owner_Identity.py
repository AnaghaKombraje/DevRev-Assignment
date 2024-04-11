import requests

def dev_user(api_url,api_key):
    headers={"Authorization":api_key}

    try:
        response=requests.get(api_url,headers=headers)
        if response.status_code==200:
            return response.json()
        else:
            print(f"Error: {response.status_code}-{response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Connection Error:",e)
        return None
    
api_url="https://api.devrev.ai/dev-users.self"
api_key = "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFVQnZ3TjZ3WFg6ZGV2dS8xIiwiZXhwIjoxODA2OTQxODY3LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTE3Njk5OTc1OTI3OTY1MDQ5MzU3IiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMTc2OTk5NzU5Mjc5NjUwNDkzNTciLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFVQnZ3TjZ3WFgiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xVUJ2d042d1hYIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoiQW5hZ2hhIiwiaHR0cDovL2RldnJldi5haS9lbWFpbCI6IjRubTIwaXMwMTBAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9mdWxsbmFtZSI6IkFOQUdIQSBLIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjMzMzg2NywiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVVCdndONndYWDp0b2tlbi8xOWhYTWZmSFgiLCJvcmdfaWQiOiJvcmdfdjc2STFZd2l3emdzWFhZdCIsInN1YiI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xVUJ2d042d1hYOmRldnUvMSJ9.olM7btIyaQlr7ubATHGXqeaf3UHN-J1v6-liKF096WyVbtjLyIdqiiTj5WlAbUAkUknM6W9SlxGegk1U-EDK0vd-1FjxKjrKH6UhNZMlwiuUuzb_KwNb3sEpN0LCkunVqi0H6lIPzx3vfLr-wKycN-ZLU6Bl3KZS9s83LW7iVJD3kFY_c9TzlYkWWCLwwm2qO02H_dbj2jNlsPLDj8Njl_y5VF1F9Eg6Zaz5pZJEchiMqn6w0_fEJxfWNca4RkS3dDmOv6B6-JC6d8En9Stjxraf3sNkoSl_ku1RLcaChF3EeedAG5M2afNMTVrzfGwzbH825OS9NyBUTQ4RS4ku4A"

result=dev_user(api_url,api_key)
if result:
    print("Dev_user: ", result)
else:
    print("Failed to Dev_User")