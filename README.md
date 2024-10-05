# Email Automation Project

## Overview

This project automates the process of sending daily email reports using Python. It utilizes the `smtplib` library for sending emails and the `schedule` library for scheduling tasks. The script is designed to send a daily reminder email with a customizable subject and body.

## Features

- Sends daily email reports at a specified time.
- Customizable email subject and body.
- Supports attachments (e.g., reports).
- Logs errors to a file for troubleshooting.

## Project Structure


]```
Px_email_autom8/
│
├── src/
│   ├── email_report.py          # Main script that sends the daily report
│   ├── email_utils.py           # Helper functions for email formatting and sending
│   └── scheduler.py             # Script for scheduling the email at a specific time
│
├── config/
│   └── settings.py              # Configuration settings (SMTP details, email credentials)
│
├── logs/
│   └── daily_report.log         # Log file to track successes and errors
│
├── reports/
│   └── sample_report.pdf        # Example or generated reports to be sent
│
├── README.md                    # Project overview and instructions
├── requirements.txt             # Python dependencies (e.g., smtplib, schedule)
├── venv/                        # Virtual environment (optional)
└── .env                         # Environment variables (email credentials, etc.)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Px_email_autom8.git
   cd Px_email_autom8
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your email settings in `config/settings.py`:
   - Set your SMTP server, port, email address, and password (use an App Password if using Gmail with 2-Step Verification).

## Usage

1. Run the scheduler script:
   ```bash
   python -m Px_email_autom8.src.scheduler
   ```

2. The script will send an email with the subject "Go To Sleep Mafaka!" every day at 9:30 PM.

## Logging

- Any errors encountered during email sending will be logged in `logs/email_errors.log`.

## Troubleshooting

- Ensure that your email settings are correct in `config/settings.py`.
- If using Gmail, make sure to enable "Less secure app access" or use an App Password if 2-Step Verification is enabled.
- Check the logs for any error messages if emails are not being sent.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Python](https://www.python.org/) - The programming language used for this project.
- [smtplib](https://docs.python.org/3/library/smtplib.html) - Python's built-in library for sending emails.
- [schedule](https://schedule.readthedocs.io/en/stable/) - A simple library for scheduling tasks in Python.
