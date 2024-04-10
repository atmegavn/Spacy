import data_processing as dp
import mysql.connector
from resume_parser import resumeparse
import os
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="resume_details"
)

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route('/resume', methods=['POST'])
def resume():
 import glob
 resume_file_name = (glob.glob("Resume/*"))
 print(resume_file_name)

 for i in range(len(resume_file_name)):
         #   print('More than one resume found in data/resume directory.')
         #   quit()
        resume_file_nam = 'C:\\Users\\Gaurav Sharma\\Documents\\frms\\' + str(resume_file_name[i])
     
        print(resume_file_nam)
        resume_data = resumeparse.read_file(resume_file_nam)
        data_resume = dp.data_load(resume_file_nam)
        keywords_resume = dp.nltk_keywords(data_resume)

                #Write output in a result file
        write_string2 = 'Keywords found in resume: ' + (', '.join(keywords_resume))
        #print(write_string2)
        mycursor = mydb.cursor()

        vrnp = str(resume_data['designition']) + ' ' + str(resume_data['Companies worked at'])

        sql = "INSERT INTO Resume (resume_file_name , Keywords_resume ,Email_Address ,Phone_Number ,Name ,Address ,Professional_Summary ,Education ,Skills ,Certifications ,Projects_Portfolio , Volunteer_Experience ,Additional_Information ,social_media ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(resume_file_nam),str(keywords_resume),str(resume_data['email']),str(resume_data['phone']),str(resume_data['name']),'',vrnp,str(resume_data['degree']),str(resume_data['skills']),'','','','','')

        mycursor.execute(sql, val)
        

        mydb.commit()

 return '', 201, { 'status': 'Done' }

@app.route('/jd', methods=['PUT'])
def jd():
  import glob
  from find_job_titles import FinderAcora
  finder=FinderAcora()
  jd_file_name = (glob.glob("JD/*"))

  for i in range(len(jd_file_name)):

         #   print('More than one resume found in data/resume directory.')
         #   quit()
        jd_file_nam = 'C:\\Users\\Gaurav Sharma\\Documents\\frms\\' + str(jd_file_name[i])
        print(jd_file_nam)
        data_jd = dp.data_load(jd_file_nam)
        keywords_jd = dp.spacy_keywords(data_jd)

                #Write output in a result file
        write_strings = 'Keywords found in JD: ' + (', '.join(keywords_jd))
                #Write output in a result file
        txt = []

        file = open(jd_file_nam, "r")
        while True:
            content=file.readline()
            if not content:
                break
            txt.append(content)
        file.close()
        #print(write_string2)
        abc = finder.findall(txt[1])
        job_name = abc[0][2]
        mycursor = mydb.cursor()

     

        sql = "INSERT INTO JD (JD_File,Keywords_JD,JOB_NAME) VALUES (%s, %s,%s)"
        val = (str(jd_file_nam),str(keywords_jd),str(job_name))

        mycursor.execute(sql, val)

        mydb.commit()
  return '', 201, { 'status': 'Done' }

@app.route('/match', methods=['DELETE'])
def match(id: int):
 import mysql.connector
 mycursor = mydb.cursor()
 mycursor.execute("Select convert(JD_File using utf8),convert(Keywords_JD using utf8),convert(JOB_NAME using utf8) from JD")
    # get all records
 jdrecords = mycursor.fetchall()
 mycursor.execute("Select convert(resume_file_name using utf8) , convert(Keywords_resume using utf8) ,convert(Email_Address using utf8) ,convert(Phone_Number using utf8) ,convert(Name using utf8) ,convert(Address using utf8),convert(Professional_Summary using utf8),convert(Education using utf8),convert(Skills using utf8) ,convert(Certifications using utf8),convert(Projects_Portfolio using utf8), convert(Volunteer_Experience using utf8) ,convert(Additional_Information using utf8),convert(social_media using utf8) from Resume")

  # get all records
 resumerecords = mycursor.fetchall()
 for i in range(len(jdrecords)):
    #van = (jdrecords)
    for j in range(len(resumerecords)):
        jd_keywords_in_resume_list = [w for w in jdrecords[i][1] if w in resumerecords[j][1]]
        jd_keywords_in_resume_list_count = len(jd_keywords_in_resume_list)
        jd_keywords_count_total = len(jdrecords[i][1])
        matchPercentage = (jd_keywords_in_resume_list_count/jd_keywords_count_total) * 100
        matchPercentage1 = round(matchPercentage, 2)
        per1 = '{}%'.format(matchPercentage1)
        print(per1)
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

            # A list of text
        data_jd = dp.data_load(jdrecords[i][0])      
        data_resume = dp.data_load(resumerecords[j][0])    
        text = [data_jd, data_resume]

        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)

            #get the match percentage
        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage2 = round(matchPercentage, 2)
        per2 = '{}%'.format(matchPercentage2)
        print(per2)
        #print((str(jdrecords[i][0]),str(resumerecords[j][0]))
        mycursor = mydb.cursor()

     

        sql = "INSERT INTO SCORE (resume_file_name , jd_file_name ,keyword_score ,cosine_score)  VALUES (%s, %s,%s,%s)"
        val = (str(jdrecords[i][0]),str(resumerecords[j][0]),str(per1),str(per2))
        print(val)

        mycursor.execute(sql, val)
        print('done')

        mydb.commit()
        
 return '', 201, { 'status': 'Done' }

if __name__ == '__main__':
   app.run(port=5000)