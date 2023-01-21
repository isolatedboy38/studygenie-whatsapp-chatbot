import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC532f34b4775e3ca613e2e7284194235d'
auth_token = '7d92b208d508afc8472d107fa6260400'
client = Client(account_sid, auth_token)

# Send the PDF file to the user
def send_pdf(to, file_list):
    for file_name in file_list:
        file_url = 'https://181e-103-47-124-100.in.ngrok.io/aws/' + file_name
        message = client.messages.create(
            body='Please find the important PDF file attached',
            from_='whatsapp:+14155238886',
            media_url=[file_url],
            to='whatsapp:+'+to
        )
    return message.sid

file_list = ['1-1.pdf', '1-2.pdf', '2-1.pdf', '2-2.pdf', '3-1.pdf', '3-2.pdf', '4-1.pdf', '4-2.pdf', '5-1.pdf', '5-2.pdf']
to = '919537165396'
send_pdf(to, file_list)