# Django 시작하기

## '.gitignore' 파일로 가상환경이랑 db는 빼놔줘!!

1. 가상 환경 만들기

```shell
# 가상환경 이름은 venv 로 하는게 편해
python -m venv [가상환경이름]
```

2. 가상 환경 시작하기

```shell
source [가상환경이름]/Scripts/activate
```

3. --1 환경 설정( requirements.txt 파일 있을 경우 )

```shell
pip install -r requirements.txt
```

3. -- 2 환경 설정( requirements.txt.파일 없을 경우 )

```shell
pip install [원하는 환경==버전]
...
... 
#여러 환경들 설치후 다 완료하면
#freeze 로 requirements.txt 파일 만들어 줘
pip freeze > requirements.txt
```

4. black formmater 설정

- black 패키지 설치(가상환경 마다)

   ```bash
   pip install black
   ```

- vscode python formatting provider 설정

   ![Untitled](Django 시작하기.assets/Untitled-16654679659732.png)

- vscode format on save 체크

   ![Untitled (1)](Django 시작하기.assets/Untitled (1).png)

- 파이썬 코드 수정 후 저장하기

- (위 설정으로 적용이 안되면) vscode **@id:editor.defaultFormatter @lang:python defaultFormatter 설정**

   ![Untitled (2)](Django 시작하기.assets/Untitled (2).png)





5. Django 프로젝트 생성

```shell
# 프로젝트 이름 뒤에 . 을 찍어줘야 manage.py 파일이 밖에 생겨!!
django-admin startproject [프로젝트이름] .
# 프로젝트를 생성한뒤 [프로젝트이름]/settings.py 에서 시간 바꿔주면 좋아
```

```python
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False
```

6. 앱 생성

```shell
python manage.py startapp [앱이름]
# 앱을 생성한 뒤에는 꼭 [프로젝트이름]/settings.py 에 앱 추가해줘!
```

```python
INSTALLED_APPS = [
    '[앱 이름]',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

7. url 분리 해주기

```python 
# [앱이름]/urls.py 파일을 만들어주고
from django.urls import path
from . import views

app_name = '[앱이름]'
urlpatterns = [
    path('', views.[함수 or 클래스 이름], name="[함수 or 클래스 이름]"),
]
```

```python
# [프로젝트이름]/url.py 에서 앱 url을 따로 분리해줘
from django.contrib import admin
# import 에 include 추가해주고
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path 에 앱의 url.py 추가해줘
    path('[앱이름]/', include('[앱이름].urls')),
]
```

8. 헤로쿠 배포 후에는 .env 파일 만들어 줘야한다

```
MAPKEY = "77f920d00b20f032ef7aa8cff4ff1e10"
AWS_ACCESS_KEY_ID = "AKIA4L3V3G5BMSDH2PGK"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "intellilabs"
DEBUG="True"
DATABASE_NAME="intellilabs"
DATABASE_PASSWORD="crud1234"
DATABASE_HOST="intellilabs.cxlqacuipc01.ap-northeast-2.rds.amazonaws.com"
```

