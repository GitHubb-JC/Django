# Django Quick Start

---

---

---

# 기본 설정

## Django 설치

- #### **설치 전 가상환경 설정 및 활성화를 마치고 진행!!**

- Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
  - 버전 명시 않으면 4 버전이 설치되니 주의
  - 참고 [Long Term Support] 장기 지원 버전
    - 보다 장기간에 걸쳐 지원하도록 고안된 버전
    - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장한다.

###### 

## Django Project

- 프로젝트 생성

  ```
  django-admin startproject firstpjt .
  ```

  - 프로젝트 이름에는 python 이나 django 에서 사용중인 키워드 및 ' - '(하이픈) 사용 불가
  - ' . '(닷) 을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨

- 서버 실행

  ```
  python manage.py runserver
  ```

  

## 프로젝트 구조

<img src="Django Quick Start.assets/image-20220922153137775.png" alt="image-20220922153137775" style="zoom:71%;" align='left'/>

- \__init__.py

  - Python 에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드를 작성하지 않음

- asgi.py

  - Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정하지 않음

- settings.py

  - Django 프로젝트 설정을 관리

- urls.py

  - 사이트의 url과 적절한 views의 연결을 지정

- wsgi.py

  - Web Server Gateway Interface
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포시에 사용하며 지금은 수정하지 않음

- manage.py

  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

    ```
    python manege.py <command> [options]
    ```

    

## Django Application

- 애플리케이션(앱) 생성

  ```
  python manage.py startapp articles
  ```

  - 일반적으로 애플리케이션 이름은 '복수형'으로 작성하는 것을 권장

## 애플리케이션 구조

<img src="Django Quick Start.assets/image-20220922154731657.png" alt="image-20220922154731657" style="zoom:100%;" align='left'/>

- admin.py
  - 관리자용 페이지를 설정 하는 곳
- apps.py
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않음
- models.py
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
- tests.py
  - 프로젝트의 테스트 코드를 작성하는 곳

- views.py
  - view 함수들이 정의 되는 곳
  - MTV 패턴의 V에 해당



## 애플리케이션 구조

- 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 **반드시** 추가해야 함!!!

  <img src="Django Quick Start.assets/image-20220922155428591.png" alt="image-20220922155428591" style="zoom:71%;" align='left'/>

- INSTALLED_APPS
  - Django installaion에 활성화 된 모든 앱을 지정하는 문자열 목록
  - 반드시 생성후 등록!!
  - 가장 윗줄에 등록!!

- 아래 순서를 지키지 않아도 상관은 없지만 나중에 advanced 한 내용을 대비하기 위해 지키는 것을 권장

  <img src="Django Quick Start.assets/image-20220922155951715.png" alt="image-20220922155951715" style="zoom:71%;" align='left'/>



## Project & Application

- Project
  - "collection of apps"
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함





# 요청과 응답

---

---

---

# 요청과 응답

## 요청과 응답

- URL ==> VIEW ==> TEMPLATE 순의 작성 순서로 코드를 작성해보고 데이터의 흐름을 이해하기



## URLs

<img src="Django Quick Start.assets/image-20220922161050348.png" alt="image-20220922161050348" style="zoom:71%;" align='left'/>

- URL ==> VIEW ==> TEMPLATE
- 기초 과정을 작성해보고
- 데이터의 흐름을 이해하기



## Views

<img src="Django Quick Start.assets/image-20220922161434440.png" alt="image-20220922161434440" style="zoom:72%;" align='left'/>

- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template 에게 HTTP 응답 서식을 맡김



## render()

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수

  - request
    - 응답을 생성하는 데 사용되는 요청 객체
  - template_name
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
  - context
    - 템플릿에서 사용할 테디어 (딕셔너리 타입으로 작성)

  ```
  render(request, template_name, context)
  ```



## Templates

<img src="Django Quick Start.assets/image-20220922172107715.png" alt="image-20220922172107715" style="zoom:71%;" align='left'/>

- 템플릿 폴더 이름은 반드시 **templates** 라고 지정해야함

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- Template 파일의 기본 경로
  - app 폴더 안의 templates 폴더
  - app_name/templates/



## 코드 작성 순서

<img src="Django Quick Start.assets/image-20220922172331372.png" alt="image-20220922172331372" style="zoom:71%;" align='left'/>

- 앞으로 Django 에서 코드 작성은 URL ==> View ==> Template 순으로 작성
- "데이터의 흐름 순서"



## 추가 설정

<img src="Django Quick Start.assets/image-20220922172550947.png" alt="image-20220922172550947" style="zoom:72%;" align='left'/>

- LANGUAGE_CODE
  - 모든 사용자에게 제공되는 번역을 결정
  - 이 설정이 적용 되려면 USE_I18N 이 활성화 (True) 되어 있어야 함
  - http://www.i18nguy.com/unicode/language-identifiers.html
- TIME_ZONE
  - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
  - USE_TZ가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜 & 시간이 반환된
  - USE_TZ 이 False 인 상태로 이 값을 설정하는 것은 error 가 발생하므로 주의
  - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

- USE_I18N
  - Django의 번역 시스템을 활성화해야 하는지 여부를 지정
- USE_L10N
  - 데이터의 지역화 된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
  - True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시
- USE_TZ
  - datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
  - True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용