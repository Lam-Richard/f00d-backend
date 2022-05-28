# import requests
# import json

# hashes = {
#     "Sargent": "5b33ae291178e909d807593e",
#     "Allison": "5b33ae291178e909d807593d",
#     "Foster Walker Plex West": "5bae7de3f3eeb60c7d3854ba",
#     "Foster Walker Plex East": "5bae7ee9f3eeb60cb4f8f3af",
#     "Elder Dining Commons": "5d113c924198d409c34fdf5c"
# }

# periods = {
#     "Lunch": "62925a6ca9f13a00c5ad4393"
# }


# # date of form YYYY-M-D
# def dataPath(diningHall, date, period):
#     return f"https://api.dineoncampus.com/v1/location/{hashes[diningHall]}/periods{period}?platform=0&date={date}"

# def fetchData(diningHall, date):
#     data = requests.get(
#         dataPath(diningHall, date), 
#         headers=
#         {
#             "Content-Type":"text", 
#             "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36",
#             "Access-Control-Allow-Origin": "*" 
#         }
#     )
#     return json.loads(data.text)

# answer = fetchData('Sargent', '2022-6-3')

# section = answer['menu']['periods']['categories']
# for i in range(5):
#     print(section[0]['items'][i]['name'])
    


