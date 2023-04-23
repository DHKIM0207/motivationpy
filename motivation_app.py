import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import openai
import schedule
import time

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
email_username = os.environ.get("EMAIL_USERNAME")
email_password = os.environ.get("EMAIL_PASSWORD")

def generate_motivational_sentence():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Generate a motivational sentence korean languae",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text.strip()

def send_email(sentence):
    msg = EmailMessage()
    msg.set_content(sentence)

    msg['Subject'] = 'Motivational Sentence'
    msg['From'] = email_username
    msg['To'] = 'blizard4479@gmail.com'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_username, email_password)
    server.send_message(msg)
    server.quit()

def scheduled_task():
    sentence = generate_motivational_sentence()
    send_email(sentence)
    print("Email sent with the motivational sentence.")

# Schedule the task, for example, every day at 9:00 AM
schedule.every().day.at("07:00").do(scheduled_task)

while True:
    schedule.run_pending()
    time.sleep(60)
