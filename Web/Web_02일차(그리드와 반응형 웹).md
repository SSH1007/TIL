# CSS Layout

--- 

---

- float는 IE 쓰던 때 쓰던 유물. 요즘은 Flexbox 씀

> CSS layout techniques

- Display, Position

- Float(1996)

- Flexbox(2012)

- Grid(2017)

- 반응형 웹 디자인(2010), Media Queries(2012)

--- 

> #### CSS 원칙

##### Normal Flow

- Inline Direction : 왼쪽에서 오른쪽

- Block Direction : 위에서 아래로

##### 모든 요소는 네모(박스 모델)이고, 위에서부터 아래로, 왼쪽에서 아래쪽으로 쌓인다.

> #### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함.  
  인라인 요소들이 주변을 wrapping 하도록 함

- 요소가 Normal flow를 벗어나도록 함

- Float 속성
  
  - none : 기본값
  
  - left : 요소를 왼쪽으로 띄움
  
  - right : 요소를 오른쪽으로 띄움

---

> ## CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델(ie 부분 지원)

- 축
  
  - main axis(메인 축) 
    
    - flex-direction : 좌 > 우(123)
  
  - cross axis(교차 축) : 상 > 하

- 구성 요소
  
  - Flex Container(부모 요소) :
    
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    
    - Flex Itemm들이 놓여있는 영역
    
    - display 속성을 flex 혹은 inline-flex로 지정
  
  - Flex Item(자식 요소)
    
    - 컨테이너에 속해 있는 컨텐츠(박스)

> ### Flex 속성

- 부모 요소에 display: flex 혹은 inline-flex

- 배치 설정
  
  - flex-direction
    
    - Main axis 기준 방향 설정
      
      - row (>123)
      
      - row-reverse (321<)
      
      - column(△123)
      
      - column-reverse(▽321)
    
    - 역방향의 경우, HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
  
  - flex-wrap
    
    - 아이템이 컨테이너를 벗어나는 경우, 해당 영역 내에 배치되도록 설정
    
    - 즉 기본적으로 컨테이너 영역을 벗어나지 않도록 함
      
      - wrap : 넘치면 줄바꿈도 해줌(wrap-reverse 시 역순)
      
      - nowrap : 기본값. 어떻게든 끼워맞춰서 한 줄에 넣어줌
  
  - flex-flow : flex-flow : direction과 wrap을 같이 쓰기
    
    - 예) row nowrap;

- 공간 나누기
  
  - justify-content(main axis 기준으로 공간 배분)
    
    - flex-start [123     ]
    
    - flex-end  [     123]
    
    - center [    123    ]
    
    - space-between  [1  2  3]
      
      - 아이템 사이의 간격을 균일 분배
    
    - space-around [ 1  2  3 ] : 여백은 1:2:2:1인 셈
      
      - 아이템을 둘러싼 영역을 균일 분배
    
    - space-evenly [  1  2  3  ] :
      
      - 전체 영역에서 아이템 간 간격을 균일 분배
  
  - align-content(cross axis)
    
    - justify를 세로로 바꾼 버전

- 정렬
  
  - align-items (모든 아이템을 cross axis 기준으로)
    
    - stretch : (기본값) 컨테이너를 가득 채움
    
    - flex-start : 위
    
    - flex-end : 아래
    
    - center : 가운데
    
    - baseline : 텍스트 밑줄에 기준선을 맞춤
  
  - align-self (개별 아이템)
    
    - 컨테이너 전체에 적용하는게 아니라  
      아이템 각각에 적용
* flex-grow : 남은 영역을 아이템에 분배

* order : 배치 순서
  
  * ```html
    <div class="flex_item" grow-1 order-3">1</div>
    ```

---

---

## Bootstrap

bootstrap 검색 후, Docs 탭의 CDN via jsDelivr의 코드를 html에 붙여넣어 사용한다.

- 위의 link(css)는 head의 최하단부에

- 아래의 script(javascript)는 body의 최하단부에

> ### CDN(Content Distribution) Network

- 컨텐츠(CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.

- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능

- 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

---

> ## spacing (margin or padding)

- {property}{sides}-{size} (예시 : mt-3)

- ```html
  <div class="mt-3 ms-5">bootstrap-spacing</div>
  ```

- 위의 예는 Margin Top 3(16px)를 의미

- side
  
  - t :  top,  b : bottom
  
  - s : start,  e : end
  
  - x : 양 옆, y : 위 아래
  
  - blank : 상하좌우

- size
  
  - | class name | rem  | px  |
    | ---------- | ---- | --- |
    | 1          | 0.25 | 4   |
    | 2          | 0.5  | 8   |
    | 3          | 1    | 16  |
    | 4          | 1.5  | 24  |
    | 5          | 3    | 48  |
  
  - 예) .mx-0은 margin 좌우를 0px로 설정 
  
  - 예) .mx-auto는 margin 가로 가운데 정렬

> ## Color

```html
<div class="bg-primary">이건 파랑</div>
<div class="bg-secondary">이건 회색</div>
<div class="bg-danger">이건 빨강</div>
<p class="text-success">이건 초록색</p>
<p class="text-danger">이건 빨간색</p>
```

> ## Text

```html
  <p class="text-start">text-start</p>
  <p class="text-center">text-center</p>
  <p class="text-end">text-end</p>
  <a href="#" class="text-decoration-none text-dark">Non-underline-Link</a>
  <p class="fw-bold">Bold Text</p>
  <p class="fw-normal">Normal weight Text</p>
  <p class="fw-light">Light weight</p>
  <p class="fst-italic">Italic</p>
```

- fw(font weight) : 폰트의 굵기 결정

- text-decoration-none : URL등의 밑줄 제거

> ## Display

```html
<h2>Display</h2>
<div class="d-inline p-2 text-bg-primary">d-inline</div>
<div class="d-inline p-2 text-bg-dark">d-inline</div>
<div class="d-none p-2 text-bg-primary">d-inline</div>
<div class="box bg-warning d-sm-none d-md-block">보이나? 안보이나?</div>
<div class="box bg-success d-md-none d-xl-block">보이나? 안 보이나?</div>
```

- d-inline : d(isplay)-inline : 인라인 형식으로 보이도록

- d-block : 블록 형식으로 보이도록

- d-sm-none : small size보다 페이지가 작아지면 사라짐

> ## Position

```html
<h2>Position</h2>
<div class="box fixed-top">fixed-top</div>
<div class="box fixed-bottom">fixed-bottom</div>
<div class="box position-absolute top-0 end-0">top0/end0</div>
<div class="box position-absolute bottom-0 start-0">bottom0/start0</div>
```

- fixed-top : 위에 고정

- position-absolute : absolute로 포지션 설정

- top-0 end-0 : 위에서 0, 끝에서 0 (우상단 끝)에 위치

- bottom-0 start-0 : 아래에서 0, 시작에서 0(좌하단 끝)

> ## Components

- Bootstrap의 다양한 UI 요소를 활용할 수 있음

- 아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음

- 기본 제공된 Components를 변환해서 활용

> ## Buttons

- 클릭했을 때 어떤 동작이 일어나도록 하는 요소

```html
<button type="button" class="btn btn-primary">Primary</button>
```

> ## Dropdowns

- dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있습니다.

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

> ## Forms > Form controls

- form-control 클래스를 사용해 \<input> 및 \<form> 태그를 스타일링할 수 있습니다.

> ## Navbar

- navbar 클래스를 활용하면 내비게이션 바를 제작할 수 있습니다.

> ## Carousel

- 콘텐츠(사진)을 순환시키기 위한 슬라이드 쇼

> ## Modal

- 사용자와 상호작용하기 위해서 사용하며, 긴급 상황을 알리는 데 주로 사용

- 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움

- 페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐)

> ## Flexbox in Bootstrap

```html
<div class="d-flex justify-content-stary">...</div>
<div class="d-flex align-items-start">...</div>
<div class="d-flex">
  <div class="align-self-start">Aligned flex item</div>
</div>
```

> ## Card > Grid Card

- 화면이 작아지면 1줄에 표시되는 카드의 개수가 줄어듬

> ## Responsive Web(반응형 웹)

- 각기 다른 디바이스에 따라 같은 컨텐츠라도 다르게 보여지게 만드는 기술

- 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 언어

- 예시
  
  - Media Queries, Flexbox, Bootstrap Grid System,  The viewport meta tag

---

## Bootstrap Grid System

> ## Grid system(Web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본 요소
  
  - Column : 실제 컨텐츠를 포함하는 부분
  
  - Gutter : 칼럼과 칼럼 사이의 공간(사이 간격)
  
  - Container : Column들을 담고 있는 공간

- Bootstrap Grid System은 flexbox로 제작됨

- 반드시 기억할 것!
  
  - 12개의 column
  
  - 6개의 grid breakpoints

-  사이즈 일람
  
  - xs, sm, md, lg, xl, xxl
  
  - col-3 : 사이즈가 xs에 해당할 경우, 3개분량의 그리드로 취급
    
    -  xs는 안 적어야 한다.
