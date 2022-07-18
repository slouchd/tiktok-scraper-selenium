About
---
This is a quick and dirty script that uses selenium and a webdriver binary (either Firefox or Chrome) to scrape public TikTok profiles.

TikTok not so long ago changed the way you could scrape profiles using requests. So this is a newer more effective technique.

Installation
---
Firstly make sure you have either Firefox or Google Chrome installed on your device. It will try to detect if you have a webdriver installed already and if not remedy that for you. However, this sometimes fails.

Create a virtualenv if you wish to.
```
python3 -m venv .env
```

Install the requirements.txt generated from requirements.in (pip-compile).
```
python3 -m pip install -r requirements.txt
```

Usage
---
Refer to [src/example_user_lookup.py](src/example_user_lookup.py) to see how to use the class.

If it works correctly you should see a returned JSON object. This will contain the data of the user you have looked up. The format will look like:

```
{
    "username": "example", 
    "nickname": "example", 
    "uid": "123", 
    "secuid": "AAA234, 
    "description": "The official account for example", 
    "verified": true, 
    "private": false, 
    "avatarlarge": "https://...", 
    "avatarmedium": "https://...", 
    "avatarthumb": "https://...", 
    "followers": 2700, 
    "following": 1, 
    "videos": 100, 
    "hearts": 25600
}
```

License
---
MIT License
