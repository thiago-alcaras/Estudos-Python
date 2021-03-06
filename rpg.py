import sys #relacionado ao sistema (sair do programa)
import os #relacionado a arquivos, pra salvar arquivo, carregar um arquivo salvo
import random #serve pra randomizar um valor (dano, vida)
import pickle 

#lista de armas com o preço
#{nome:valor}
weapons = {"Great Sword":40}

#CLASSE DO JOGADOR
class Player:
  def __init__(self,name):
    self.name = name
    self.maxhealth = 100
    self.health = self.maxhealth
    self.base_attack = 10 
    self.attack = 10
    self.gold = 40
    self.pots = 0
    self.weap = ["Rusty Sword"] #lista de armas
    self.curweapon = ["Rusty Sword"] #lista com a arma equipada

    @property
    def attack(self):
      if self.curweapon == "Rusty Sword":
        self.attack += 5
      if self.curweapon == "Great Sword":
        self.attack += 15
      
      return attack

#CLASSE DO GOBLIN
class Goblin:
  def __init__(self,name):
    self.name = name
    self.maxhealth = 50
    self.health = self.maxhealth
    self.attack = 5
    self.goldgain = 10
GoblinIG = Goblin("Goblin")

#CLASSE DO ZOMBIE
class Zombie:
  def __init__(self,name):
    self.name = name
    self.maxhealth = 70
    self.health = self.maxhealth
    self.attack = 7
    self.goldgain = 15
ZombieIG = Zombie("Zombie")

#FUNÇÃO PARA INICIALIZAR O JOGO
def main():
  os.system("clear") #comando no meu sistema para limpar a tela
  print("Bem Vindo! \n")
  print("1) Start")
  print("2) Load")
  print("3) Sair")
  option = input("-> ")

  if option == "1":
    start() #É PARA UM NOVO JOGO
  elif option == "2":
    if os.path.exists("savefile") == True:
      os.system("clear")
      with open("savefile","rb") as f:
        global PlayerIG
        PlayerIG = pickle.load(f)
      print("Save carregado")
      option = input(' ')
      start1() #START1 É PARA JOGO SALVO
    else:
      print ("Sem arquivo salvo")
      option = input(' ')
      main()
  elif option == 3:
    sys.exit()
  
  else:
    main()

#FUNÇÃO START
def start():
  os.system('clear')
  print("Olá, qual é o seu nome?")
  option = input("--> ")
  global PlayerIG
  PlayerIG = Player(option)
  start1()

#FUNÇÃO START1
def start1():
  os.system('clear')
  print("Nome: %s" %PlayerIG.name)
  print("Ataque: %i" % PlayerIG.attack)
  print("Gold: %i" %PlayerIG.gold)
  print("Arma equipada: %s" %PlayerIG.curweapon)
  print("Poções: %i" %PlayerIG.pots)
  print("Vida: %i/%i" % (PlayerIG.health,PlayerIG.maxhealth)) #30/100
  print("\n")
  #OPÇÕES
  print("1) Lutar")
  print("2) Loja")
  print("3) Salvar")
  print("4) Sair")
  print("5) Inventário")

  option = input("--> ")
  if (option == "1"):
    prefight()
  elif (option == "2"):
    store()
  elif option == "3":
    os.system("clear")
    with open("savefile","wb") as f:
      pickle.dump(PlayerIG,f)
      print("\nJogo salvo!")
    option = input(' ')
    start1()
  elif option == "4":
    sys.exit()
  elif option == "5":
    inventory()
  else:
    start1()

#FUNÇÃO INVENTÁRIO
def inventory():
  os.system("clear")
  print("O que você deseja fazer? ")
  print("1) Equipar arma")
  print("2) Voltar")
  option = input(">> ")
  if option == "1":
    equip()
  elif option == "2":
    start1()

#FUNÇÃO EQUIPAR
def equip():
  os.system("clear")
  print("O que deseja equipar?")
  for weapon in PlayerIG.weap:
    print(weapon)
  print("'b' para voltar")
  option = input(">> ")
  if option == PlayerIG.curweapon:
    print("Você já está equipado com esta arma.")
    option = input(" ")
    equip()
  elif option == "b":
    inventory()
  elif option in PlayerIG.weap:
    PlayerIG.curweap = option
    print("Você equipou %s" %option)
    option(" ")
    equip()
  else:
    print("Você não possui %s no seu inventário" %option)


#FUNÇÃO PREFIGHT
def prefight():
  global enemy;
  enemynum = random.randint(1,2)
  if enemynum == "1":
    enemy = GoblinIG
  else:
    enemy = ZombieIG
  fight()

#FUNÇÃO LUTA
def fight():
  os.system("clear")
  print("%s     vs     %s" % (PlayerIG.name,enemy.name))
  print("Vida atual de %s : %i/%i     Vida atual de %s : %i/%i" %  (PlayerIG.name,PlayerIG.health,PlayerIG.maxhealth,enemy.name, enemy.health, enemy.maxhealth))
  print("Poções: %i\n" %PlayerIG.pots)
  print("1) Atacar")
  print("2) Beber Poção")
  print("3) Correr")
  option = input("--> ")
  if option == "1":
    attack()
  elif option == "2":
    drinkpot()
  elif option == "3":
    run()
  else:
    fight()

#FUNÇÃO PARA ATACAR
def attack():
  os.system("clear")
  PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
  EAttack = random.randint(1,10)
  if PAttack == PlayerIG.attack / 2:
    print("Você errou")
  else:
    enemy.health -= PAttack
    print("Você deu %i de dano" %PAttack)
  option = input(" ")
  if enemy.health<=0:
    win()
  if EAttack == 1:
      print("O inimigo errou")
  else:
    PlayerIG.health -= EAttack
    print("O inimigo deu %i de dano" %EAttack)
  option = input(" ")
  if PlayerIG.health <=0:
    dead()
  else:
    fight()


#FUNÇÃO PARA BEBER POÇÃO
def drinkpot():
  os.system("clear")
  if PlayerIG.pots == 0:
    print("Você não possui nenhuma poção")
  else:
    PlayerIG.health += 50
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("Poção consumida")
  option = input(" ")
  fight()

#FUNÇÃO PARA CORRER
def run():
  os.system("clear")
  runnum = random.randint(1,3)
  if runnum == 1:
    print("Você fugiu!")
    option = input(" ")
    start1()
  else:
    print ("Falhou")
    option = input(" ")
    os.system("clear")
    EAttack = random.randint(1,3)
    if EAttack == 1:
      print("O inimigo errou")
    else:
      PlayerIG.health -= EAttack
      print("O inimigo deu %i de dano" %EAttack)
    option = input(" ")

    if (PlayerIG.health <= 0):
      dead()
    else:
      fight()

#FUNÇÃO WIN
def win():
  os.system('clear')
  enemy.health = enemy.maxhealth
  PlayerIG.gold += enemy.goldgain
  print("Você derrotou o %s" %enemy.name)
  print("Você ganhou %i de gold" %enemy.goldgain)
  option = input("")
  start1()

#FUNÇÃO DEAD
def dead():
  os.system("clear")
  print("Você morreu")
  option = input(" ")

def store():
  os.system("clear")
  print("Bem vindo a loja")
  print("\nO que você quer comprar?\n")
  print("1) Great Sword")
  print("2) back")
  option = input(" ")

  if option in weapons:
    if PlayerIG.gold >= weapons[option]:
      os.system("clear")
      PlayerIG.gold -= weapons[option]
      PlayerIG.weap.append(option)
      print("Você comprou a arma!")
      option = input(" ")
      store()
    
    else:
      os.system("clear")
      print("Você não possui gold")
      option = input(" ")
      store()

  elif option == 2:
    start1()
  
  else:
    store()

main()