import schedule
import time
from Px_email_autom8.src.email_utils import send_report  # This line is correct

#The scheduling code is be moved to a separate script dedicated to scheduling tasks, such as scheduler.py.
#This keeps your email utility functions focused solely on sending emails and allows for better organization of your code.

# Define the daily report sending function
def job():
    print("Job is running...")  # This will print to the console when the job runs
    attachment_path = "/path/to/report.pdf"  # Update this path as needed
    send_report(attachment_path)

# Scheduling the script to run daily at 9:30 PM
schedule.every().day.at("21:55").do(job)  # 21:30 is 9:30 PM in 24-hour format

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
