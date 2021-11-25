# obejeto do tipo EntityPersonalData com seus getters e seters
class EntityPersonalData():
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone