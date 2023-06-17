from faker import Faker

from data.data import Person

faker = Faker(locale='en_US')


def generator():
    yield Person(
        first_name=faker.first_name(),
        zip_code=faker.postcode(),
        email=faker.email()

    )