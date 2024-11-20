from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("Job Scrapper")
#데이터 베이스 생성 / 이전에 검색한 항목 빠르게 리턴
db = {}  #서버가 켜진 동안만 유지

@app.route("/")  # 함수 위에 위치해야함 (decorator)
def home():
  return render_template("home.html")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword == "":
    return redirect("/")
    
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    db[keyword] = jobs  #키워드 값 db에 jobs와 저장
  
  return render_template("search.html", keyword=keyword, jobs=jobs)
  # 키워드를  template에 보냄

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")

  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)
  #as_attatchment=True : 다운로드가 실행되도록 해줌


  
app.run("0.0.0.0")
