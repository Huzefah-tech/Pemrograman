# Happy Birthday Elaina
import datetime

class Elaina:
  def _init_(self):
    self.name = "Elaina"
    self.birthday = datetime.date(2025, 10, 17)
    self.gift = "Endless Journey 🌸"
    self.wish = "May your days be filled with magic and smiles."
  
def wish(elaina):
  print(f"🎂 Happy birthday, {elaina.name}!")
  print(f"Gift: {elaina.gift}")
  print(f"Message: {elaina.wish}")

elaina = Elaina()
wish(elaina)