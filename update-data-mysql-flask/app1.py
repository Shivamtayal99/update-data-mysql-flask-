from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('test.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="shivam"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        result=request.form
        name=result['Name']
        physics=int(result['Physics'])
        chemistery = int(result['chemistery'])
        maths = int(result['Mathematics'])

        s=str(physics+chemistery+maths)


        mycursor.execute("update students set physics=%s,chemistery=%s,maths=%s,total=%s where name=%s",(physics,chemistery,maths,s,name))

        mydb.commit()
        mycursor.close()
        # return render_template('test.html',result=result)
        return render_template('index.html',result=result)

app.run(debug=True)