import requests, json

# Link should be set for the subreddit desired
link = "https://www.reddit.com/r/funny/hot/.json"
session = requests.Session()

#Headers is necessary to get a response from the server
headers = {'accept': 'application/json, text/javascript',
           'cache-control': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Sec-Fetch-Dest': 'empty',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
           }

#Get request
r = session.get(link, timeout=5, headers = headers)
#Load the JSON into a variable
datajson = json.loads(r.content)

#Loop though everypost on the subreddit
for x in datajson["data"]["children"]:
    print(x)
    #Check if thumbnail is present, if not add a default one
    if "http" not in x["data"]["thumbnail"]:
        x["data"]["thumbnail"] = "https://cdn.1min30.com/wp-content/uploads/2017/05/Reddit-logo-1.jpg"

#Format json with all necessary information
    testmsg = {
      "username": x["data"]["subreddit"],
      "embeds": [
        {
          "title": x["data"]["title"],
          "url": x["data"]["url"],
          "color": 15258703,
          "fields": [
            {
              "name": "[ Author ]",
              "value":  x["data"]["author"],
              "inline": True
            },
            {
              "name": "[ Upvotes ]",
              "value": x["data"]["score"],
              "inline": True
            },
              {
              "name": "[ Comments ]",
              "value": x["data"]["num_comments"],
              "inline": True
            },
            {
                  "name": "[ USEFUL LINKS ]",
                  "value": " [ [Subreddit](http://www.reddit.com/"+x["data"]["subreddit_name_prefixed"]+") ] [ [Link to Comments](http://www.reddit.com"+x["data"]["permalink"]+") ] [ [Link]("+x["data"]["url"]+") ]",
              }
          ],
          "thumbnail": {
            "url": x["data"]["thumbnail"]
          },
          "footer": {
            "text": "TArvela",
            "icon_url": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"
          }
        }
      ]
    }
    # Post request to the discord webhook
    r2 = requests.post("https://discordapp.com/api/webhooks/696636622904623135/U_paJHGtROo9Y1cvwPpbRUrPdlIVJTsIuhi0kIMCGK0wYWQWmgjH4dUVArHBaV7Qv9xw",
                        data=json.dumps(testmsg), headers={"Content-Type":"application/json"})



