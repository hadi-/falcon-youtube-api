# falcon-youtube-api
GET data from youtube api v3 with falcon framework

# how to run
```
pip install -r requirements.txt
```

# run server
```
gunicorn falconapi.app
```
server will run on port 8000

# get list with search
```
http://localhost:8000/?q=python
```

# get detail video 
```
http://localhost:8000/details/VtF-Ucj4aAM
```
