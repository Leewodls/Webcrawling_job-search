from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("what do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)  #리스트 형태
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")

file.write("position, company, Location, URL\n")

for job in jobs:
  file.write(
    f"{job['position']},{job['company']}, {job['location']},{job['link']}\n")

file.close()
