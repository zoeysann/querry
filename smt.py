import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="zoey_464852",
  database="vocabulary")

mycursor=mydb.cursor()
sql_query = """
    SELECT questions.Questions, questions_true_answer.answer
    FROM questions
    JOIN questions_true_answer ON question_id = q_id;
"""
mycursor.execute(sql_query)
myresult= mycursor.fetchall()

vocabulary={}
for i in myresult:
    key=i[0]
    value=i[1]
    vocabulary[key]=value

print(vocabulary)
