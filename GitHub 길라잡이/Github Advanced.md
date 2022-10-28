# Git / Github Advanced

---

- git restore 파일 이름
  
  - 워킹 디렉토리 내의 파일을 마지막 커밋 상태로 되돌림
  
  - 파일 이름에는 .이 들어올 수 있음(해당 폴더 내 파일 전체)
  
  - 기존에 커밋이 존재해야 가능



- git restore --staged 파일 이름
  
  - 워킹 디렉토리 내의 파일을 스테이징 에리어에서 내림
  
  - 기존에 커밋이 존재해야 가능



- git rm --cached 파일 이름
  
  - git이 더 이상 관리하지 않도록 함
  
  - 아예 git이 관리하지 않도록 빼버린다(있다는 걸 인식은 함).
  
  - rm --cached한 이후에는 ignore 가능





.gitignore는 실제 폴더의 파일을 git이 인식을 못하게 함





- git commit --amend
  
  - 커밋 수정
    
    - 파일, 메시지 둘 다 수정 가능
  
  - vim 에디터가 나옴
    
    - i => 수정(insert) 모드
    
    - esc => 수정 모드 탈출
    
    - :wq => vim 종료
    
    - :q! -> 그냥 나가기



### ※ reset은 협업, remote 환경에선 쓰지 않는 것을 추천

- git reset --hard 커밋id
  
  - 커밋을 과거로 이동
    
    - 예) d87e828 a.py로 돌아가고 싶은 경우, git reset --hard d87e 입력 
    
    - git reflog로 과거 기록들을 조회한 뒤 이동하고 싶은 id를 선택하라
      
      - git reflog로 reset 하기 전의 로그 확인 가능
  
  - 워킹 디렉토리도 과거인 상태
  
  - 스테이징 에리어도 비어있는 상태
  
  - 기존의 untracked 파일은 사라지지 않고 untracked로 남아있음



- git reset --soft 커밋id
  
  - 커밋을 과거로 이동
  
  - 워킹 디렉토리는 최신인 상태
  
  - 스테이징 에리어에 최신 상태가 추가되어 있음



- git reset 커밋id
  
  - 또는 reset mixed 커밋id
  
  - 커밋을 과거로 이동
  
  - 워킹 디렉토리는 최신인 상태
  
  - 스테이징 에리어에 최신 상태가 추가되어 있음



### reset과 달리 revert는 협업, remote 환경에도 사용 가능

- git revert 커밋id
  
  - 과거일을 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함
  
  - vim 에디터로 이동. :wq로 탈출
  
  - 취소했다는 커밋을 생성









브랜치는 독립 공간을 분리, 형성하여 원본에 대해 안전함











### ◆ git flow

5개의 브랜치로 나누어 소스 코드를 관리

- 마스터 : 제품으로 출시될 수 있는 브랜치

- 디벨롭 : 다음 출시 버전을 개발하는 브랜치

- 피쳐 : 기능을 개발하는 브랜치 (머지한 뒤에는 삭제)

- 릴리즈 : 이번 출시 버전을 준비하는 브랜치

- 핫픽스 : 출시 버전에서 발생한 버그를 수정하는 브랜치

대규모 프로젝트에 적합한 브랜치 전략



브랜치 하나로만 작업하는 형태는 지양해야 함



Branch와 원격 저장소를 이용해 협업을 하는 두가지 방법

1. 원격 저장소 소유권이 있는 경우 : Shared repository model

2. 원격 저장소 소유권이 없는 경우 : Fork & Pull model



## | Shared repository model

- 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어있는 경우

- Pull Request를 사용하여 팀원 간 변경 내용에 대한 소통 진행

- master 브랜치에 직접 개발하는 것이 아니라 기능별로 브랜치를 따로 만들어 개발



- git stash
  
  - 커밋을 남기지 않고 임시로 저장하는 명령어
  
  - 버전 기록을 남기지 않는 임시 커밋 개념

- git stash pop
  
  - 







## ◆ git branch

- git log --oneline --all --graph
  
  - 나눠진 브랜치들을 모두 한줄짜리 로그가 적힌 그래프로 표현해서 출력



- git branch
  
  - 로컬 저장소의 브랜치 목록 확인

- git branch -r
  
  - 원격 저장소의 브랜치 목록 확인

- git branch -a
  
  - 모든 저장소의 브랜치 목록 확인



- git merge 브랜치이름
  
  - 현재 있는 브랜치에다가 브랜치를 병합



- git branch -d 브랜치이름
  
  - 브랜치 지우기
  
  - git branch -D 브랜치이름 : 강제 삭제



- git switch 브랜치이름
  
  - 현재 브랜치에서 다른 브랜치로 이동하는 명령어

- git switch -c 브랜치이름 
  
  - 브랜치를 새로 생성 및 이동

※ switch하기 전에 해당 브랜치의 변경사항을 반드시 커밋해야함

※ 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨



- git merge 서브브랜치이름
  
  - 브랜치 병합
  
  - 병합 주체가 될 브랜치로 switch한뒤 실행
  
  - conflict가 일어낫다
    
    - status 확인
    
    - conflict가 일어난 파일들을 보여줌
  
  - 또는 파일 트리(vsCode에서 실행 시)에 ! 표시
  
  - 수정 => add => commit
























