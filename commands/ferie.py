import requests
import datetime

class Ferie:

    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.name = "Ferié"
        self.description = "Affiche les jours feriés"

    async def execute(self):
        d = datetime.date.today()
        today = datetime.datetime(d.year, d.month, d.day)

        ferie_metropole      = requests.get(f"https://calendrier.api.gouv.fr/jours-feries/metropole/{d.year}.json").json()
        ferie_aslace_moselle = requests.get(f"https://calendrier.api.gouv.fr/jours-feries/alsace-moselle/{d.year}.json").json()

        for (date, day) in ferie_aslace_moselle.items():
            public_holiday = datetime.datetime.strptime(date, "%Y-%m-%d")
                
            if public_holiday > today: # next holiday
                await self.message.channel.send(f"Le prochain jour férié pour les bg qui bossent en Alsace-Moselle est le {date} - {day}")
                break
            
        for (date, day) in ferie_metropole.items():
            public_holiday = datetime.datetime.strptime(date, "%Y-%m-%d")
                
            if public_holiday > today: # next holiday
                await self.message.channel.send(f"Le prochain jour férié pour les crasseux qui bossent autre part est le {date} - {day}")
                break