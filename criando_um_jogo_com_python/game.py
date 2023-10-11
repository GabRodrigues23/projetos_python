import pygame

pygame.init() #Inicia o processo de codagem com pygame

#Define as coordenadas e velocidade do "Player"
x = 400
y = 300
velocidade = 10

#Definir o tamanho da janela
largura = 800; altura = 600
janela = pygame.display.set_mode((largura,altura)) #Implementar os valores dentro da janela
pygame.display.set_caption('Meu 1° jogo em python') #Título da janela

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50) #Delay para abrir a janela 
   #Criar o evento de fechar a janela
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #Verifica se o usuário clicou em fechar a janela
            janela_aberta = False


    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade

    janela.fill((0,0,0,)) #Caso o círculo se mova, ele deixa um rasto da cor do obj, com o uso da função fill, ela pinta (sobrescreve) o rastro do personagem com a cor de fundo ou a cor definida entre parenteses 

    pygame.draw.circle(janela,(0,255,0),(x,y),(50)) #Define onde o circulo vai ser desenhado, a cor, as coordenadas em que ele vai aparecer (largura x altura) e o raio do diâmetro / Pode ser visto se passado o mouse por cima da tag .circle
    pygame.display.update() #Atualiza a janela para que o circulo apareça

# 1° Criar a janela
# 2° Criar e colocar o circulo (personagem) dentro da tela
# 3° Configurar os botões

# Tela:
#   y ___________________________ x
#    |
#    |
#    |
#    |
#    |
#    |
#    |
#    |