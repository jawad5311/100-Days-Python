
"""
    Send emails using python.

"""
import smtplib

username = "miromuqadd-9430@yopmail.com"

with smtplib.SMTP("smtp.yopmail.com") as connection:
    connection.starttls()
    connection.login(user=username, password=None)
    connection.sendmail(
        from_addr=username,
        to_addrs="bosyxemmepy-3557@yopmail.com",
        msg="Subject: Checking\n\nthis is email body."
    )

