import pandas as pd
from datetime import datetime
from storage import load_events
import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load sensitive info from .env file
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv(465))

def send_event_reminders():
    try:
        df = pd.read_excel("attendees.xlsx")
        if "Email" not in df.columns:
            print("Error: The 'attendees.xlsx' file must contain an 'Email' column.")
            return
        attendee_emails = df["Email"].dropna().tolist()
    except FileNotFoundError:
        print("Error: 'attendees.xlsx' not found. Please create it to send reminders.")
        return
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return

    if not attendee_emails:
        print("No attendee emails found in 'attendees.xlsx'.")
        return

    events = load_events()
    today_str = datetime.now().strftime("%d-%m-%Y")
    todays_events = [e for e in events if e["date"] == today_str]

    if not todays_events:
        print("No events scheduled for today. No reminders sent.")
        return

    print(f"Found {len(todays_events)} event(s) for today and {len(attendee_emails)} attendee(s).")

    context = ssl.create_default_context()

    for event in todays_events:
        print(f"\n--- Sending reminders for: '{event['name']}' at {event['time']} ---")
        for email in attendee_emails:
            try:
                msg = EmailMessage()
                msg['Subject'] = f"Reminder: {event['name']} Today at {event['time']}"
                msg['From'] = SENDER_EMAIL
                msg['To'] = email
                
                body = f"""
                Hi,

                This is a friendly reminder for the following event scheduled for today:

                Event: {event['name']}
                Date: {event['date']}
                Time: {event['time']}
                Type: {event['type']}
                Location: {event['location']}

                We look forward to seeing you there!

                Best,
                Smart Event Manager
                """
                msg.set_content(body)

                with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                    server.login(SENDER_EMAIL, APP_PASSWORD)
                    server.send_message(msg)
                    print(f"  -> Successfully sent reminder to: {email}")

            except Exception as e:
                print(f"  -> Failed to send reminder to {email}. Error: {e}")
    
    print("\nAll reminders have been processed.")
