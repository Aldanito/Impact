from flask import *
from flask_mail import Mail
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
app.config['MAIL_SERVER']='smtp.office365.com' 
#  smtp.yandex.com         mail.nccr.kz       smtp.office365.com
app.config['MAIL_PORT'] = 587
# 587    43      465
app.config['MAIL_USERNAME'] = '1155121354@link.cuhk.edu.hk'  
app.config['MAIL_PASSWORD'] = 'Wuk2c8$gBqFJh=9'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download1')
def downloadFile1():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "Информация для родителей.docx"
    return send_file(path, as_attachment=True)


@app.route('/download2')
def downloadFile2():
    path = "Полезные советы.docx"
    return send_file(path, as_attachment=True)


@app.route('/download3')
def downloadFile3():
    path = "Регламент госуслуг.docx"
    return send_file(path, as_attachment=True)


@app.route('/success', methods = ['GET','POST'])
def success():
    if request.method == 'POST':
       sender = "salomat423@gmail.com"
       password = "221502Ernur@"
       server = smtplib.SMTP("smtp.office365.com", 587)
       server.starttls()
    
       name = request.form.get("name")
       email = request.form.get("email")
       message = request.form.get("message")
       ms ='Поступило сообщение от:\nКлиент:' +name +'\nEmail:' +email +'\n'+'\n'+message
       server.login(sender, password)
       msg = MIMEText(ms, _charset='utf-16')
       msg["Subject"] = "КГУ 'ПСИХОЛОГО-МЕДИКО-ПЕДАГОГИЧЕСКАЯ КОНСУЛЬТАЦИЯ №2' АКИМАТА Г. НУР-СУЛТАН"
       msg["Body"] = 'Поступил заказ от:\nКлиент:' +name +'\nEmail: ' +email +'\n'+'\n'+message

       server.sendmail(sender, ['aldan.moldabekov@gmail.com'], msg.as_string())
       return redirect("/")

# @app.route('/success', methods = ['GET','POST'])
# def success():
#     if request.method == 'POST':
#        name = request.form.get("name")
#        email = request.form.get("email")
#        message = request.form.get("message")
    
#        msg = Message(
#                     'Вы получили заявку [ПМПК] ',
#                     sender ='1155121354@link.cuhk.edu.hk',
#                     recipients = ['aldan.moldabekov@gmail.com', 'pmpk2_astana@mail.ru' ]
#                 ) 
#        msg.body = 'Поступил заказ от:\nКлиент:' +name +'\nEmail:' +email +'\n'+'\n'+message
#        mail.send(msg)

#        return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True, host='127.1.4.5')