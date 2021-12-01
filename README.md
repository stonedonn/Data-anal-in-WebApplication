# 🙌코로나가 먼지!
미세먼지,기온과 코로나 사망률은 상관관계가 있는지 데이터 분석 및 시각화를 진행한 뒤 Django를 이용해 웹페이지에 뿌려줍니다.


초기 시작 URL은 http://127.0.0.1:8000/noticeboard/ 입니다.


## 👍초기 Intro 화면
![인트로](https://user-images.githubusercontent.com/46741844/127413535-a4bc1560-2781-4b7f-a6b7-ceef5397b60a.PNG)
> 워딩클라우드로 이루어진 이미지를 클릭하면 Main 화면으로 넘어갑니다.

## 🎨Main 화면
![127 0 0 1_8000_noticeboard_covid](https://user-images.githubusercontent.com/46741844/127414774-074977be-0331-4144-98ad-10daa253a428.png)
> 각각의 메뉴바에서 시각화한 데이터들을 확인할 수 있습니다.


***
## 👀데이터 전처리 및 시각화 예시
> Excel파일을 csv파일로 변환 후에 원하는 시각화를 위해 데이터프레임을 전처리 해주었습니다.


![데이터1](https://user-images.githubusercontent.com/46741844/127415694-90c23565-0878-4a49-9d6e-276ecd463f2a.PNG)
> 초기 데이터프레임 
***
![데이터3](https://user-images.githubusercontent.com/46741844/127415710-5f6db527-ab98-4411-8131-d5343c4256dd.PNG)
> 누적확진자와 누적사망자에서 diff함수를 이용하여 일별확진자와 사망자를 뽑아냈습니다.
***
![데이터5](https://user-images.githubusercontent.com/46741844/127415717-a9bb5099-84c0-4e9d-90bc-f5590fccdf06.PNG)
> 일별확진자와 사망자를 이용해 사망률(치명률)을 뽑아낸뒤
***
![데이터6](https://user-images.githubusercontent.com/46741844/127415719-4ed56e95-89eb-43f3-8cd6-fe1e35baed63.PNG)
> 최종적으로 데이터를 전처리하여 지역 월별로 csv파일로 저장했습니다.
***
### 🧒데이터 시각화
![폴리움](https://user-images.githubusercontent.com/46741844/127418506-3ac8804c-c662-4443-9c49-8bd7bb7145b9.png)
***
![sejong](https://user-images.githubusercontent.com/46741844/127418637-2374cd12-9ae5-450f-aa90-e1ea6d6c7eab.png)
***
### 🕹Django 시스템 구조도
![시스템구조도](https://user-images.githubusercontent.com/46741844/127418500-e7483107-8984-42fd-a93c-7f16ebad6aa9.png)
> Model 부분에 데이터를 저장하지 않았기 때문에 연결만 한 뒤 사용하지 않았습니다.
***
