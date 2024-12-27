from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {} # { username : pokemon}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.power = randint(30, 60)
        self.hp = randint(200, 400)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Cила покемона: {self.power}
Здоровье покемона: {self.hp}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}
Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"""
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):

    def info(self): # доп. задание
        return "У тебя покемон-волшебник \n\n" + super().info()

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "

    def info(self): # доп. задание
        return "У тебя покемон-боец \n\n" + super().info()

from datetime import datetime, timedelta

class Pokemon:
    def __init__(self):
        self.hp = 100
        self.last_feed_time = datetime.now()  

    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  # изменено на seconds
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time
            return f"Следующее время кормления покемона: {next_feed_time}"

class Wizard(Pokemon):
    def feed(self):
        feed_interval = 15  
        hp_increase = 5    
        return super().feed(feed_interval, hp_increase)

class Fighter(Pokemon):
    def feed(self):
        feed_interval = 20  
        hp_increase = 20    
        return super().feed(feed_interval, hp_increase)


if __name__ == "__main__":
    pikachu = Pokemon()
    wizard = Wizard()
    fighter = Fighter()

    print(pikachu.feed())  
    print(wizard.feed())   
    print(fighter.feed())  

