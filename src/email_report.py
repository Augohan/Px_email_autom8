from email_utils import send_email
from config.settings import RECEIVER_EMAIL

def generate_report():
    # Logic to generate the report
    report_content = "This is your daily report."
    return report_content

def main():
    report = generate_report()
    send_email("Daily Report", report)

if __name__ == "__main__":
    main()
