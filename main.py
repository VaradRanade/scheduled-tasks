# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas as pd
import datetime as dt
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

data = pd.read_csv("birthdays.csv")
month = data["month"].head()
day = data["day"].head()


now = dt.datetime.now()
today_day = now.day
today_month = now.month


for index, row in data.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        

        random_letter_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(random_letter_file, "r") as letter_file:
            letter_contents = letter_file.read()
            personalized_letter = letter_contents.replace("[NAME]", row["name"])

        


        with smtplib.SMTP("smtp.gmail.com",587) as connection :
            connection.starttls()
            connection.login(user=my_email , password=password)
            connection.sendmail(from_addr=my_email , to_addrs= row["email"] , msg=f"Subject:Happy Birthday!\n\n{personalized_letter}")

        print(f"Birthday email successfully sent to {row['name']}!")


            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
