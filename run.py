from modules.paulmccartney import Paulmccartney_newspaper
from modules.taylorswift import Taylor_newspaper
from modules.topps import topps_newspaper
from modules.rihannanow import Rihannanow_newspaper
from modules.livenation import Livenation_newspaper
from modules.mileycyrus import Mileycyrus_newspaper

from faker import Faker
import random
from time import sleep

def extract_emails_from_csv():
    with open('emails.csv', 'r') as emails_csv:
        emails = emails_csv.read().strip().split('\n')
        return emails

emails = extract_emails_from_csv()

faker = Faker('en_US')
name = faker.name()
firstname, lastname = name.strip().split(' ')[:2]
year = random.randint(1970, 2004)
month = random.randint(1, 12)
day = random.randint(1, 28)
postal_code = faker.postalcode()

for email_address in emails:
    print(email_address)
    Paulmccartney_newspaper().subscribe(firstname=firstname, lastname=lastname, email_address=email_address)
    Taylor_newspaper().subscribe(email_address=email_address)
    topps_newspaper().subscribe(email_address=email_address)
    Rihannanow_newspaper().subscribe(firstname=firstname, lastname=lastname, year=year, month=month, day=day, postal_code=postal_code, email_address=email_address)
    Livenation_newspaper().subscribe(postal_code=postal_code, email_address=email_address)
    Mileycyrus_newspaper().subscribe(email_address=email_address)
    sleep(5)