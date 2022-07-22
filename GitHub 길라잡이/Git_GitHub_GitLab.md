# Git

## 초기 설정

- 깃허브 유저 네임, 이메일로 아래 설정
  
  - git config --global user.name 깃허브유저네임
    
    - 초기설정, commit하기 전에는 해줘야 함
    
    - 유저 네임 등록
  
  - git config --global user.email 깃허브이메일주소 
    
    - 초기설정, commit하기 전에는 해줘야 함
    
    - 유저 이메일 등록
    
    - 유저네임과 이메일 주소 넣었다고 깃허브랑 연결된건 아님

- 깃랩 유저 네임, 이메일로 repo마다 아래 설정
  
  - git config --local user.name 유저 이름
    
    - 유저 네임 등록(로컬)
  
  - git config --local user.email 유저 이메일

---

## 명령어

- git init
  
  - git 사용 가능 상태(git repository)로 변경
  - .git 폴더가 생성된다(숨김 파일)
  - 상위 폴더 보다는 각각 폴더에서 init을 해주는게 더 나은 것 같다.

- git status
  
  - 내 상태를 학인하는 것
  - add로 추가하면 new file로 표기됨
  - add로 추가된 놈을 수정하면 modified로 표기됨.

- git add (file_name)
  
  - 파일을 staging area에 추가
  - git add .
    - 폴더 안의 모든 놈들을 staging area에 추가한다.

- git commit -m 'commit message'
  
  - 커밋(버전 기록 남기기)
  - commit message는 필수. 협업이 얼마나 잘 되어있는지를 보여주는 증표

- git config --global -l
  
  - 현재 git 설정 리스트 출력

- git log
  
  - 그 동안의 동작 로그를 출력
  - git log --oneline : commit 아이디 앞의 7자리와 commit 메시지만 출력

- git add . 한 뒤, git commit만 치면 Vim 에디터로 이동함(시안색)
  
  - i를 누르면 insert 모드로 변경
  - 엔터 두번 누르면 제목으로 이동, 또 두 번 누르면 본문 작성 가능
  - esc 키 누르고 :wq누르면 commit 내용을 저장하고 탈출함

- **ctrl+l으로 화면 정리 가능**

---

## 순서

1. Working Directory(**Local**)
   - 개인 코드 작성
2. Staging 영역
   - git add를 통해서 수정된 코드를 올리는 영역(임시 저장)
3. Repository
   - git commit을 통해서 최종 수정본을 제출

git init >> touch, start... >> git status >> git add . >> git status >> git commit -m '커밋 메시지' >> git status >> git log --oneline

**로컬 컴퓨터에서의 commit은 완료**

mv 원래이름 .확장자 바꿀이름.확장자 : 이름 바꾸기

이름을 바꾸면 git status에선 원래 이름 파일을 deleted로 표기하며, 바뀐 이름 파일은 Untracked로 표기된다.

--- 

# GitHub와 연결

- git remote add origin 깃허브 주소
  
  - (git bash에선 shift + Insert가 ctrl + V 역할)
  
  - 깃허브 주소와 origin이라는 이름의 깃을 연결.

- git remote -v
  
  - 현재 git에 등록된 원격 저장소 리스트를 보여줌

- git push origin master (=git push <romote/저장소명> <branch/브랜치명>)
  
  - 브랜치는 작업 공간을 의미
  - 마스터 브랜치를 origin(git repo)에 추가
  - 깃허브와 연동하여 전송
  - git push -u origin master 
    - 해당 브랜치 안에서는 이후 git push만 쳐도 푸시할 수 있다.

- git remote rm (저장소명)
  
  - git에 등록된 원격 저장소 리스트에 있는 저장소명 제거

---

# GitHub 순서

#### 올리는 순서

- 로컬에서 git init > 깃 레포 만들기
- GitHub에서 create Repository
- git remote add origin 깃허브 레포 URL 로 연결
- .gitignore 추가
- 변경 사항 생긴 뒤
  - git add .
  - git commit -m 'commit message'
  - git push origin master

#### 내려받는 순서

- 이미 clone한 폴더가 없다면 init 되지 않은(.git 폴더가 없는)
  폴더에서 git clone 깃허브 주소로 클론 실행

- 그 후 pull

---

# Pull로 GitHub에서 로컬의 Git으로 가져오기

- **git init 한 폴더가 아니라 깨끗한 폴더에서 clone 진행**

- git clone 깃허브주소 :
  
  - 해당 폴더에 repo 폴더를 만들고 그 안에 클론 생성

- git clone 깃허브주소 . 
  
  - repo 폴더 없이 바로 클론 생성
  
  - repo 폴더 이름은 후에 바뀌어도 무방

- git pull
  
  - git repo의 커밋을 local로 다운로드
  
  - 한번 clone으로 복사한 이후는 pull로
  
  - pull부터 하는 습관을 들이자.

---

# Git 안에 Git이 들어있으면 안돼

---

# 비밀번호 같은 개인정보의 경우,

# .gitignore를 생성하여 업로드를 방지한다.

- 커밋을 남기기 전에 추가

- .gitignore 안에 해당 파일, 폴더(/) 등을 적는다. (메모장 등으로)

- 여러 개의 경우 엔터로 구분
  
  - 프로젝트 시작할 때 git init 한 뒤, 
    맨 처음에 만들어두고 그 안에 비밀 정보를 넣어두는 것을 추천

- gitignore.io 사이트에 접속해서 생성한 리스트를 .gitignore 파일에 넣어라

- 레포지토리를 만들 때 .gitignore 생성 옵션은 체크 안 하는 걸 추천

---

# push했는데 reject가 뜬 경우

- **pull해라**
  
  - merge한다고 하면 다행
  
  - conflict한다고 하면 해당 부분을 해결하고 add > commit > push

---

# 해당 컴퓨터를 더 이상 사용하지 않게 되었을 때

- 윈도우 검색창에서 **자격 증명 관리자** 를 입력해 접속

- Windows 자격 증명 >> 일반 자격 증명에 있는 자신의 git 증명들을 제거하면 된다.

---

# commit message 수정

**협업할 때 절대 이런 케이스는 일어나지 말아야 한다!**

***(commit이 꼬이게 됨)***

- git commit --amend

- vim editer
  
  - i : insert mode
  
  - :wq : 저장하고 나가기

- git push -f : 강제적으로 push
