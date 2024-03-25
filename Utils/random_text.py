from faker import Faker


class RandomText:
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()

    def get_random_title(self):
        return self.fake.name()

    def get_random_sentence(self):
        return self.fake.sentence()
