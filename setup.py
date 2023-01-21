from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

BASE_URL = 'https://isolatedboy38.pythonanywhere.com/'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

@app.route('/aws/<name>')
def aws(name):
    return send_from_directory(directory='Files/aws', path=name, as_attachment=True)

@app.route('/adhoc/<name>')
def adhoc(name):
    return send_from_directory(directory='Files/adhoc', path=name, as_attachment=True)

@app.route('/scm/<name>')
def scm(name):
    return send_from_directory(directory='Files/scm', path=name, as_attachment=True)

@app.route('/dm/<name>')
def dm(name):
    return send_from_directory(directory='Files/dm', path=name, as_attachment=True)

@app.route('/uml/<name>')
def uml(name):
    return send_from_directory(directory='Files/uml', path=name, as_attachment=True)

@app.route('/erp/<name>')
def erp(name):
    return send_from_directory(directory='Files/erp', path=name, as_attachment=True)


# Main Route
@app.route('/bot', methods=['POST', 'GET'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    phone = request.form.get("From").split("+")
    phone_number = phone[1]

    print(phone_number)
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'hi' or 'Hello' or 'Hi' or 'hello' or 'hey' or 'Hey' in incoming_msg:
        msg.body("Hi There! I'm material sharing chatbot\n"+
                "Materials Available for 7th Sem.\n"+
                "1. aws - Advanced Cloud Computing\n"+
                "2. adhoc - Adhoc Network\n"+
                "3. scm - Suppy Chain Management\n"+
                "4. erp - Enterprise Resource Planning\n"+
                "5. dm - Digital Marketing\n"+
                ".....\n"+
                "Type short form and get all material with qb.\n"+
                "created by Fenal"
                )
        responded=True
    
    if 'aws' in incoming_msg:
        aws1 = os.listdir('Files/aws/')
        aws_send_pdf(to=phone_number, file_list=aws1, sub='aws')
        responded=True
        
    if 'adhoc' in incoming_msg:
        adhoc1 = os.listdir('Files/adhoc/')
        aws_send_pdf(to=phone_number, file_list=adhoc1, sub='adhoc')
        responded=True
        
    if 'scm' in incoming_msg:
        scm1 = os.listdir('Files/scm/')
        aws_send_pdf(to=phone_number, file_list=scm1, sub='scm')
        responded=True
        
    if 'dm' in incoming_msg:
        dm1 = os.listdir('Files/dm/')
        aws_send_pdf(to=phone_number, file_list=dm1, sub='dm')
        responded=True
        
    if 'uml' in incoming_msg:
        uml1 = os.listdir('Files/aws/')
        aws_send_pdf(to=phone_number, file_list=uml1, sub='uml')
        responded=True

    if 'erp' in incoming_msg:
        erp1 = os.listdir('Files/erp/')
        aws_send_pdf(to=phone_number, file_list=erp1, sub='erp')
        responded=True
        
    if not responded:
        msg.body('....:/')
    return str(resp)

def aws_send_pdf(to, file_list, sub):
    for file_name in file_list:
        file_url = BASE_URL+'/'+sub+'/'+file_name
        message = client.messages.create(
            body='Important PDF files attached',
            from_='whatsapp:+14155238886',
            media_url=[file_url],
            to='whatsapp:+'+to
        )
    return message.sid

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
