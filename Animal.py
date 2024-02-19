#Animal.py
#Gabriel Trace
#created 2-19-24

class Animal: 
  has_brain = True
  is_alive = True
  age = 0
  name = None

  def move(speed, direction, distance):
    pass

class Bird(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def cakaw(self):
    print("CAKAW")
    print("""
                                     _.--.__                                             _.--.
                                    ./'       `--.__                                   ..-'   ,'
                       _________   ,/               |`-.__                            .'     ./
                       |         | :,                 :    `--_    __                .'   ,./'_.....
                       |  CAKAW  | :                  :   /    `-:' _\.            .'   ./..-'   _.'
                       |  CAKAW  |  :                  ' ,'       : / \ :         .'    `-'__...-'
                       |_______  |   `.               .'  .        : \@/ :       .'       '------.,
                              \|       ._....____  ./    :     .. `     :    .-'      _____.----'
                                                `------------' : |     `..-'        `---.
                                                            .---'  :    ./      _._-----'
                                    .---------._____________ `-.__/ : /`      ./_-----/':
                                    `---...--.              `-_|    `.`-._______-'  /  / ,-----.__----.
                                    ,----' ,__.  .          |   /  `\.________./  ====__....._____.'
                                    `-___--.-' ./. .-._-'----\.                  ./.---..____.--.
                                            :_.-' '-'            `..            .-'===.__________.'
                                                                    `--...__.--'
        """)

Billy = Bird("billy", 16)
Billy.cakaw()
print(f"This is {Billy.name}, he is {Billy.age}")
print(f"Isn't he totally tubular? His clout is off the charts!")
ani = Animal()
print(ani.name)
