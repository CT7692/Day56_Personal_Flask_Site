from flask import Flask, render_template, request

import smtplib
import os

app = Flask(import_name="my_website")

@app.route('/')
def open_home():
    return render_template('index.html')

@app.route('/sent', methods=['post'])
def send_email():
    output = request.form.to_dict()
    gmail_pw = os.environ.get("PW")
    sender = output['email']
    name = output['name']
    msg_content = output['message']

    if sender != "" and msg_content != "":
        my_email = "jrydel92@gmail.com"
        message = f"Subject: New Email from {name}\n\n{msg_content}".encode('utf-8')
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=gmail_pw)
            connection.sendmail(from_addr=sender, to_addrs=my_email, msg=message)
            return render_template('sent.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)