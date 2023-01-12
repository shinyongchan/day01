#교재 dictionary 예제

subjects={"의사소통 영어":"A+",
         '오래된 미래':"B+",
         '양자역학':"A0",}
student='신용찬'
subject='오래된 미래'
print(student,'학생의',subject,'성적은',subjects['오래된 미래'],'입니다.')
print(f'{student} 학생의 {subject} 성적은 {subjects[subject]}입니다.') #f스트링 사용 (, 쓸필요없음)
print("%s 학생의 %s 성적은 %s 입니다."% (student,subject,subjects[subject]))
print("{0} 학생의 {1} 과목 성적은 {2}입니다.".format(student,subject,subjects[subject]))