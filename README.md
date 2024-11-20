# Webcrawling_job-search
python + flask 를 이용한 간단한 크롤링 웹사이트

## 소개
  1.	구인 정보 검색:
	사용자가 입력한 키워드를 바탕으로 Indeed와 WWR에서 구인 정보를 스크래핑
<img width="681" alt="스크린샷 2024-11-20 오후 8 47 46" src="https://github.com/user-attachments/assets/78d5a4aa-91a0-4e71-8ce0-e594cfa23bff">

	2.	결과 출력:
	검색된 구인 정보는 웹 애플리케이션에서 테이블 형태로 확인
	직무명(Position), 회사명(Company), 위치(Location), 지원 링크(Link) 정보를 포함
 <img width="1057" alt="스크린샷 2024-11-20 오후 8 35 35" src="https://github.com/user-attachments/assets/4c87eded-a31b-4033-ae50-fd3b84eb4722">

	3.	파일 내보내기:
	검색 결과를 CSV 파일로 내보내기 기능을 제공
<img width="116" alt="스크린샷 2024-11-20 오후 8 45 30" src="https://github.com/user-attachments/assets/98df0880-7d13-43c9-b053-49093f88b346">

## 구조
  • indeed.py : Indeed 사이트에서 구인 정보를 스크래핑
  
	•	wwr.py : WWR(We Work Remotely) 사이트에서 구인 정보를 스크래핑
 
	•	main.py : Flask를 사용하여 웹 서버를 실행하고, 검색 및 데이터 내보내기를 처리
 
	•	home.html : 검색 키워드를 입력하는 메인 페이지
 
	•	search.html : 검색 결과를 테이블 형태로 보여주는 결과 페이지

## 라이브러리
	•	Selenium: 구인 사이트에서 동적으로 데이터를 가져오기 위해 사용.
	•	BeautifulSoup: HTML 파싱 및 데이터 추출.
	•	Flask: 웹 애플리케이션 서버 구현.
	•	Pico.css: 간단하고 아름다운 UI를 위한 CSS 프레임워크.
