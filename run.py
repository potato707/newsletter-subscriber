from modules.paulmccartney import Paulmccartney_newspaper
from modules.taylorswift import Taylor_newspaper
from modules.topps import topps_newspaper
from faker import Faker

emails = ["d838246554@mymaily.lol",
          "d838246554@mymaily.lol",
          "d838246554@mymaily.lol"]

faker = Faker('en_US')
name = faker.name()
firstname, lastname = name.strip().split(' ')[:2]

for email_address in emails:
    Paulmccartney_newspaper().subscribe(firstname=firstname, lastname=lastname, email_address=email_address)
    Taylor_newspaper().subscribe(email_address=email_address)
    topps_newspaper().subscribe(email_address=email_address)