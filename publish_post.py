import httpx
import requests
import sys

file = {"content": open(sys.argv[0], "rb")}
user = 'conor@conor.com'
pwd = 'aphextwin21'
data = {"username": "conor@conorcunningham.net", "password": "UHiavJs6NBHrD8KpELP^GND2;y7*c@XL"}

URL = 'http://localhost:8000/'
URL = 'https://blog.conorcunningham.net/'

LOGIN_URL = URL + 'accounts/login/'
BLOG_URL = URL + 'post/new/'
title = "My title!"

with requests.Session() as session:

    login = session.get(LOGIN_URL)
    print(f"Login Get Login Page Code: {login.status_code}")

    csrf_token = login.cookies['csrftoken']
    print(f"CSRF Token: {csrf_token}")

    data['csrfmiddlewaretoken'] = csrf_token

    session.headers.update({'referer': "https://blog.conorcunningham.net/accounts/login/"})
    session.headers.update({'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0"})
    post = session.post(
        LOGIN_URL,
        data=data,
        auth=("conor@conorcunningham.net", "UHiavJs6NBHrD8KpELP^GND2;y7*c@XL")
    )

    # get = session.get("http://localhost:8000/post/new/")
    print(f"Login Status Code: {post.status_code}")
    # print(post.text)
    print(f"Session Cookie {session.cookies['sessionid']}")

    csrf_token = session.cookies['csrftoken']

    data = {
        'csrfmiddlewaretoken': csrf_token,
        "title": title
    }

    upload = session.post(
        BLOG_URL,
        files=file,
        data=data
    )
    print(upload.headers)
    print(f"Blog Create Status Code:  {upload.status_code}")
    print(upload.text)

