def scrape_data(soup):
    job_card=soup.find_all('div',class_="internship_meta experience_meta")
    job_data=[]
    jobcard_length = 0
    for job in job_card:
        jobb=job.find('a',id='job_title').text.strip() if job.find('a',id='job_title') else None
        comp=job.find('p',class_="company-name").text.strip() if job.find('p',class_="company-name") else None
        status=job.find('div',class_="actively-hiring-badge").text.strip() if job.find('div',class_="actively-hiring-badge") else None
        sal=job.find('span',class_="desktop").text.strip() if job.find('span',class_="desktop") else None
        jobcard_length+=1
        job_data.append({"job":jobb,
                         "company":comp,
                         "status":status,
                         "Salary":sal})
    return job_data