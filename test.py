class Cars():
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year

    def info(self) -> str:
        result = f'Nazwa: '+self.name+'\nRok: '+str(self.year)
        return result

    def get_name(self) -> None:
        print(self.name)

def welcomeUser(user: str):
    """
    The function returns the user's greeting
    welcomeUser(userName)
    """
    message = f"Welcome {user}!"
    return message

print(welcomeUser("mbism"))

asda
