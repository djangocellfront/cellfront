# Cell Front



## Settings

설정 파일은 `settings/settings.py`에 있습니다.

url 연결의 경우 `settings/urls.py`확인하면 됩니다. `app/`파일과 연결되어 있습니다.  



## 기술스택

### 1. Django

django: model, view를 통해 연산 진행



### 2. DB

djongo: django mongoDB

pymongo: python mongoDB (ver. 3.12.1)



### 3. Server

gunicorn: WSGI Middleware

whitenoise: static file 제공

django-cors-headers: CORS 설정 (Cross-Origin Resource Sharing, Front, Back 자원교환용)  
