import httpx
import requests
import sys

file = {"content": open(sys.argv[0], "rb")}
user = 'conor@conor.com'
pwd = 'aphextwin21'
login_data = {"username": user, "password": pwd}
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

    login_data['csrfmiddlewaretoken'] = csrf_token

    post = session.post(
        LOGIN_URL,
        data=login_data,
        auth=(user, pwd),
    )

    # get = session.get("http://localhost:8000/post/new/")
    print(f"Login Status Code: {post.status_code}")
    print(post.cookies)
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

