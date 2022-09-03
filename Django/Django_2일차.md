# Django

---

### ◆ 목차

1. [Namespace](##◆-namespace)

2. [Django Model](##◆-django-model)

3. [Queryset API](##◆-queryset-api)

4. [CRUD with view functions](##◆-crud-with-view-functions)

5. [Admin site](##◆-admin-site)

---

---

## ◆ Namespace

- 개체를 구분할 수 있는 범위

- Namespace의 필요성

![](Django_2일차_assets/2022-09-01-12-16-02-image.png) ①

![](Django_2일차_assets/2022-09-01-12-16-20-image.png) ②

![](Django_2일차_assets/2022-09-01-12-16-57-image.png) ③

![](Django_2일차_assets/2022-09-01-12-17-24-image.png) ④

위의 경우, 2가지 문제가 발생한다.

1. articles app index 페이지에 작성한 두번째 앱 index로 이동하는 하이퍼 링크를 클릭 시 현재 페이지로 다시 이동
   
   - URL namespace : ①, ④

2. pages app의 index url `(http://127.0.0.1:8000/pages/index/)`로 직접 이동해도 articles app의 index 페이지가 출력됨
   
   - Template namespace : ②, ③

\_

#### ◆ URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음

- app_name =  attribute를 작성해 URL namespace를 설정  **(①)**

![](Django_2일차_assets/2022-09-01-12-29-12-image.png)

- URL tag의 변화 **(④)**
  
  ![](Django_2일차_assets/2022-09-01-12-38-34-image.png)
  
  - 방문할 URL이 속한 앱의 이름을 앞에 적어준다.
  
  - app_name을 지정한 후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야 한다. << 그렇지 않으면 NoReverceMatch 에러 발생

\_

#### ◆ Template namespace

- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서대로 template을 검색 후 렌더링 함.

- 디렉토리 생성을 통해 물리적인 이름공간 구분
  
  - Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를  
    `app_name/templates/app_name/` 형태로 변경
  
  - Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것
  
  ![](Django_2일차_assets/2022-09-01-12-56-52-image.png)
  
  - 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분 수정 **(②)**

![](Django_2일차_assets/2022-09-01-12-58-32-image.png)

 \_                                                                       

---

## ◆ Django Model

- Model(이하 모델)의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해

- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공함

#### ◈ Database

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

- 데이터베이스 기본 구조
  
  1. 스키마(Schema)
     
     - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
     
     - | column | datatype |
       |:------:|:--------:|
       | id     | INT      |
       | name   | TEXT     |
       | age    | INT      |
       | email  | TEXT     |
  
  2. 테이블(Table)
     
     - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합 =  관계(Relation)
       
       1. 필드(field) : 속성, 열(column)
          
          - 각 필드에는 고유한 데이터 형식이 지정됨
       
       2. 레코드(record) : 튜플, 행(row)
          
          - 테이블의 데이터는 레코드에 저장됨
     
     - PK(Primary Key/기본 키)
       
       - 각 레코드의 고유한 값(식별자로 사용)
       
       - 기술적으로 `다른 항목과 절대로 중복되어 나타날 수 없는 단일 값(unique)`을 가짐
       
       - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨
  
  3. 쿼리(Query)
     
     - 데이터를 조회하기 위한 명령어를 일컬음
     
     - 조건에 맞는 데이터를 추출하거나 조작하는 명령어(주로 테이블형 자료구조)
     
     - Query를 날린다 > 데이터베이스를 조작한다.

\_

#### ◈ Model

**`웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구`**

- Django는 Model을 통해 데이터에 접속하고 관리(단일한 데이터에 대한 정보를 가짐)

- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함

- 저장된 데이터베이스의 구조(layout)

- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
  
  - 모델 클래스 1개 == 데이터베이스 테이블 1개
  
  - 매핑 = 하나의 값을 다른 값으로 대응시키는 것

- Models.py 작성
  
  - 모델 클래스를 작성하는 것은 데이터베이스 `테이블의 스키마를 정의`하는 것
  
  - **모델 클래스 == 테이블 스키마**
  
  ![](Django_2일차_assets/2022-09-01-16-26-43-image.png)
  
  - 'DB 필드의 이름' = '클래스 변수 값(DB 필드의 데이터 타입)'
  
  - id 컬럼은 테이블 생성 시 Django가 자동으로 생성

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
  
  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
  
  - 클래스 상속 기반 형태의 Django 프레임워크 개발
    
    - 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것
  
  - models 모듈을 통해 어떠한 DB 필드(컬럼)을 정의할 것인지 정의
    
    - 클래스 변수 title과 content은 DB 필드를 나타냄

- 예시 모델 필드 일람
  
  - CharField(max_length=None, \*\*options)
    
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    
    - max_length : 필드의 최대 길이(필수 인자)
      
      - 데이터베이스와 Django의 유효성 검사에 활용됨
  
  - TextField(\*\*options)
    
    - 글자의 수가 많을 때 사용

\_

#### ◈ Migrations

- 모델에 대한 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정

- Django가 모델에 생긴 변화(필드 추가, 모델 삭제 등)를 DB에 반영하는 방법

- :cherry_blossom:**주요 명령어**:cherry_blossom:
  
  1. python manage.py **makemigrations**
     
     - 모델을 작성, 혹은 변경한 것에 기반한 새로운 설계도를 생성할 때 사용
     
     - migrations/000*\_initial.py의 형태
  
  2. python manage.py **migrate**
     
     - makemigrations로 생성한 설계도를 실제 db.sqlite3 DB에 반영
     
     - 모델과 DB의 동기화

- 기타 명령어
  
  1. python manage.py showmigrations
     
     - migrations 파일들이 migrate 되었는지 여부 확인 : ([X] = 완료됨)
  
  2- python manage.py sqlmigrate articles 0001
  
  - 0001 migrations 파일이 SQL 문으로 어덯게 해석되는지 미리 확인

- 설계도를 해석하여 DB의 동기화를 해주는 것이 ORM

\_

#### ◈ ORM(Object-Relational-Mapping)

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django <-> SQL) 데이터를 변환하는 프로그래밍 기술

- 내장 Django ORM을 사용

- 장점
  
  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
  
  - 객체 지향적 접근으로 인한 높은 생산성

- 단점
  
  - ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음

- `생산성`이 탁월하여 사용함

\_

#### ◈ 추가 필드 정의 과정

1. models.py에 **컬럼 추가(변경)** 한 뒤 **python manage.py makemigrations** 실행

2. Django가 추가 컬럼에 기본값을 어떻게 설정할지 물어봄  
   \1) 다음 화면으로 넘어가서 새 컬럼의 기본 값 직접 입력  
   \2) 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성  
   **보통, '1'을 입력 후 Enter**

3. 기본적으로 파이썬의 timezone 모듈의 now 메서드 반환값을 기본 값으로 사용할 수 있음 >> **Enter** 를 누르든지, **timezone.now**를 입력해라

4. 새로운 migration 파일 생성됨

5. **python manage.py migrate** 명령어로 DB와 동기화 진행

```
1. models.py에서 변경사항이 발생하면
2. migrations 파일 생성(설계도 생성) : makemigrations
3. DB 반영 (모델과 DB의 동기화) : migrate
```

\_

##### ▣ DateTimeField()

- python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드

- DateField를 상속하는 클래스

- 선택 인자
  
  1. auto_now_add
     
     - 최초 생성 일자(Useful for creation of timestamps)
     
     - Django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)
  
  2- auto_now
  
  - 최초 수정 일자(Useful for "last-modified" timestamps)
  
  - Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

\_

---

## ◆ Queryset API

---

## ◆ CRUD with view funcions

120p

---

## ◆ Admin site

DB 삭제
서버 끄고
db.sqlite3 삭제
migrations 폴더에서 000*들 지워준다.

DB 삭제하면
python manage.py makemigration
python manage.py migrate

python manage.py createsuperuser
아이디
비번(안보이는게 정상)
bypass : y하고 넘겨도 무방
