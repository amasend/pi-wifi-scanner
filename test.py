<<<<<<< HEAD
class Cars():
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year

    def info(self) -> str:
        result = f'Nazwa: '+self.name+'\nRok: '+str(self.year)
        return result

    def get_name(self) -> None:
        print(self.name)


car_one = Cars("BWM", 2021)
print(car_one.info())

car_one.get_name()
=======
def welcomeUser(user: str):
    """
    The function returns the user's greeting
    welcomeUser(userName)
    """
    message = f"Welcome {user}!"
    return message

print(welcomeUser("mbism"))
>>>>>>> main
