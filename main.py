#IMPORTS
from art import logo
from listas import preço_volume
from listas import preço_palete

#LISTS
resultado_final = 0

#GLOBAL
loop = True

# FUNÇÕES
def transf_peso(peso):
  """Transforma o peso real expedido no valor de peso registado na Tabela da Torrestir."""
  if peso <= 5:
    peso = 5
    return peso
  elif peso <= 10:
    peso = 10
    return peso
  elif peso <= 20:
    peso = 20
    return peso
  elif peso <= 30:
    peso = 30
    return peso
  elif peso <= 50:
    peso = 50
    return peso
  elif peso <= 75:
    peso = 75
    return peso
  elif peso <= 100:
    peso = 100
    return peso
  elif peso <= 125:
    peso = 125
    return peso
  elif peso <= 150:
    peso = 150
    return peso
  elif peso <= 175:
    peso = 175
    return peso
  elif peso <= 200:
    peso = 200
    return peso
  elif peso <= 250:
    peso = 250
    return peso
  elif peso <= 300:
    peso = 300
    return peso
  else:
    return peso
        

def transf_palete(num_pal):
  """Transforma o número de paletes enviadas em valores registados pela Tabela da Torrestir."""
  palete_loop = True
  while palete_loop:
    if num_pal >= 1 and num_pal <= 3:
      palete_loop = False
      num_pal = "1 a 3"
      return num_pal
    elif num_pal > 3:
      palete_loop = False
      num_pal = "Superior"
      return num_pal
    else:
      print("Número de paletes rejeitado. Por favor, insira um valor numérico inteiro acima de 0 para o valor das paletes. Reiniciando...")
      print("...")
      paletes()
    
def zona(codigo_postal):
  """Transforma o código postal em Zona registada na Tabela da Torrestir"""
  if codigo_postal >= 4700 and codigo_postal < 5000:
    zona = 1
    return zona
  elif (codigo_postal >= 3000 and codigo_postal < 4700) or (codigo_postal >= 5000 and codigo_postal < 6000):
    zona = 2
    return zona
  elif (codigo_postal >= 1000 and codigo_postal < 3000) or (codigo_postal >= 6000 and codigo_postal < 7000):
    zona = 3
    return zona
  elif codigo_postal >= 7000 and codigo_postal < 9000:
    zona = 4
    return zona

def peso_sup_300(peso, codigo_postal):
  """Valor de 1.024 na variável peso_sup_300xSCUT, devido a uma alteração nos valores da SCUT. Valor final da Tabela foi acrescentado como 2.1%, mas para facilitar nesta contagem e não alterar o código todo, acrescentou-se um valor médio. A alterar em novas Tabelas!"""
  diferença = peso - 300
  if zona(codigo_postal) == 1:
    peso_sup_300x = (diferença * 0.12611) + preço_volume[300][zona(codigo_postal)-1]
    return peso_sup_300x
  elif zona(codigo_postal) == 2:
    peso_sup_300x = (diferença * 0.15212) + preço_volume[300][zona(codigo_postal)-1]
    return peso_sup_300x
  elif zona(codigo_postal) == 3:
    peso_sup_300x = (diferença * 0.16122) + preço_volume[300][zona(codigo_postal)-1]
    return peso_sup_300x
  elif zona(codigo_postal) == 4:
    peso_sup_300x = (diferença * 0.18971) + preço_volume[300][zona(codigo_postal)-1]
    return peso_sup_300x

def volumes():
  """Gera preços para os envios de volumes."""
  resultado_final = 0
  while loop:
    zip = int(input("Inserir os primeiro quatro números do código postal do destinatário:\n"))
    wt = int(input("Inserir peso da mercadoria enviada, sem casas decimais, arredondado para cima:\n"))
    peso_transformado = transf_peso(peso=wt)
    zona_final = zona(codigo_postal=zip)
    activation()
    print("")
    print(f"Peso transformado: {peso_transformado} kg.")
    print(f"Zona: {zona_final}.")
    if wt <= 300:
      preço_final_inf300 = preço_volume[transf_peso(peso=wt)][zona(codigo_postal=zip)-1]
      print(f"Valor Torrestir: {preço_final_inf300}€.")
      resultado_final += preço_final_inf300
      print(f"Resultado Total: {round(resultado_final, 2)}€.")
    else:
      preço_final_sup300 = round(peso_sup_300(peso=wt, codigo_postal=zip), 2)
      print(f"Valor Torrestir: {preço_final_sup300}€.")
      resultado_final += preço_final_sup300
      print(f"Resultado Total: {round(resultado_final, 2)}€.")
  
    print("""
    ----------
    """)

def paletes():
  while loop:
    zip = int(input("Inserir os primeiro quatro números do código postal do destinatário:\n"))
    num_pal = int(input("Inserir número de paletes enviadas:\n"))
    print("")
    print(f"Paletes enviadas: {num_pal}.")
    print(f"Zona: {zona(codigo_postal=zip)}.")
    print(f"Valor Torrestir: {round((preço_palete[transf_palete(num_pal=num_pal)][zona(codigo_postal=zip)-1])*num_pal, 2)}€.")
      
    print("""
    ----------
    """)

def activation():
  print(logo)
  print("Bem-vindo ao preçario da Torrestir!\n")
    
activation ()

#correção_ou_expedição = input("")

vol_ou_pal = input("Deseja ver o preço de volumes ou de paletes? Escreva 'v' para volumes, ou 'p' para paletes: \n").lower()

if vol_ou_pal == "v":
  volumes()
elif vol_ou_pal == "p":
  paletes()
