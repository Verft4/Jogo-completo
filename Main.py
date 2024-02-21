from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from random import randint
import random
from classes.personagem import Person
from classes.item import Item
from classes.magic import Spell
from kivymd.uix.widget import Widget
from kivy.animation import Animation



potion = Item("Potion", "potion", "Heals 50 HP", 25)
blizzard = Item("Blizzard", "attack","não tem esse item",250 )
player_items = [{"item": potion, "quantity": 15},{"item":blizzard,"quantity":1}]
player1 = Person("Valos:", 250, 25,  34, player_items )
enemy1= Person("Esqueleto:", 180, 35, 34, player_items)
enemy2=Person("Salazar:",210,50,34,player_items)
enemy3=Person("Alduin:",500,100,40,player_items)
players=[player1]
enemies=[enemy1]
enemies2=[enemy2]
enemies3=[enemy3]

Builder.load_string("""
<MenuScreen>:
    canvas:
        Color:
            rgba: [1, 1, 1, 1]
    
    
        Rectangle:
            size:self.size[0],self.size[1]
            pos: self.pos
            source:"images/image.jpg"
    FloatLayout:
        
        
        orientation: 'vertical'
  
    
       
        MDTopAppBar:
             
            title:"Dungeons"
            pos_hint:{"top": 1.0}
        Image:
            source: "images/kindpng_290633.png"
            pos_hint:{"center_x": 0.45, "center_y":0.7}
            
            
        MDFillRoundFlatButton:
            text: 'Começar'
            font_size:30
            pos_hint:{"center_x":0.5,"center_y":0.59}       
            on_press: root.manager.current = 'jogo'
           
      

<SettingsScreen>:
    canvas:
        
        Color:
            rgba: [1, 1, 1, 1]
            
    
    
        Rectangle:
            size:self.size[0],self.size[1]
            pos: self.pos
            source:"images/Pixel-Copia.jpg"
        
          
    FloatLayout:
        id:float
        
        orientation: 'vertical'
        MDRectangleFlatButton:
            id:ATT
            
          
            text:'           ATAQUE'
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.3}
            on_press:root.atackk()
            
            
        MDRectangleFlatButton: 
            id:magica
            text:'MAGIA     '
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.3}
            on_press:root.scroll()
            
            
    
        MDRectangleFlatButton:
            id:cura
            text:"            POÇÃO_CURA"
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.1}
            on_press:root.item()
            
        
    
        MDRectangleFlatIconButton:
            id:sair
            text:"Sair        "
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.1}
            on_press:root.sair()
        MDRectangleFlatButton:
            id:PROXT            
            text:" Proximo "
            font_size:50
            size_hint:(0.5,0.1)
            pos_hint:{"center_x":0.5,"center_y":2}
            on_press:root.manager.current='terceira'
   
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.1, "center_y":0.85}
           
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.8, "center_y":0.85}
        Image:
            image_num: 11
            id:esqueleto
            size_hint:(0.5,0.5)
            source: "images/esqueleto%d.png" % int(self.image_num)
            pos_hint: {'center_x': 0.55,'center_y': 0.6}
        Image:
            image_num: 10
            id:prsn
            size_hint:(0.5,0.5)
            source: "image/person%d.png" % int(self.image_num)
            pos_hint: {'center_x': 0.45,'center_y': 0.6}
        MDLabel:
            color:1,1,1,1
            text:"Valos"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint: {'center_x': 0.1,'center_y': 0.95}
            font_style:"H6"
           
        MDLabel:
            id:NA
            color: 1,1,1,1
            text:"20"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.85}
            font_style:"H6"
                
        MDLabel:
            id:INI
            color: 1,1,1,1
            text:"20"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.85}
            font_style:"H6"
                
        MDLabel:
            text:"Vida="
            color: 1,1,1,1
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.1,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HP
            color: 1,1,1,1
            text:"250"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            color: 1,1,1,1
            text:"Vida="
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.8,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HPI
            color: 1,1,1,1
            text:"150"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:pocao
            text:""
            halign:("center")
            size_hint:(0.2,0.5)
            pos_hint:{"center_x":0.38,"center_y":0.10}
            font_style:"H4"
      
        MDLabel:
            id:MAGIA
            text:""
            halign:("center")
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.955,"center_y":0.3}
            font_style:"H4"
        MDLabel:
            id:FRSI
            text:""
            color:1,1,1,1
            haling:("center")
            size_hint: (0.45,1)
            pos_hint: {'center_x': 0.6,'center_y': 0.9}
            font_style:"H6"
      
<TerceiraTela>:
    canvas:
        Color:
            rgba: [1, 1, 1, 1]
    
    
        Rectangle:
            size:self.size[0],self.size[1]
            pos: self.pos
            source:"images/Pixel-Copia.jpg"
    FloatLayout:
        orientation: 'vertical'
        MDRectangleFlatButton:
            id:ATT
            text:'         ATAQUE'
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.3}
            on_press:root.atackk()
        MDRectangleFlatButton:
            id:PROXT            
            text:" Proximo "
            font_size:50
            size_hint:(0.5,0.1)
            pos_hint:{"center_x":0.5,"center_y":2}
            on_press:root.manager.current='quarta'
          
            
            
        MDRectangleFlatButton: 
            id:magica
            text:'MAGIA      '
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.3}
            on_press:root.scroll()
            
            
    
        MDRectangleFlatButton:
            id:cura
            text:"          POÇÃO_CURA"
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.1}
            on_press:root.item()
            
        
    
        MDRectangleFlatIconButton:
            id:sair
            text:"Sair        "
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.1}
            on_press:root.sair()
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.1, "center_y":0.85}
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.8, "center_y":0.85}
        Image:
            image_num:11
            id:esqueleto
            size_hint:(0.5,0.5)
            source: "images/mago%d.png" % (self.image_num)
            pos_hint: {'center_x': 0.55,'center_y': 0.6}
     
        Image:
            image_num: 10
            id:prsn
            size_hint:(0.5,0.5)
            source: "image/person%d.png" % int(self.image_num)
            pos_hint: {'center_x': 0.45,'center_y': 0.6}
            
           
        MDLabel:
            id:NA
            color: 1,1,1,1
            text:"20"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.85}
            font_style:"H6"
      
        MDLabel:
            color:1,1,1,1
            text:"Valos"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint: {'center_x': 0.1,'center_y': 0.95}
            font_style:"H6"
                
        MDLabel:
            id:INI
            text:"20"
            color: 1,1,1,1
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.85}
            font_style:"H6"
                
        MDLabel:
            text:"Vida="
            color:1,1,1,1
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.1,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HP
            text:"50"
            color: 1,1,1,1
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.9}
            font_style:"H6"
       
        MDLabel:
            text:"Vida="
            halign:"center"
            color: 1,1,1,1
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.8,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HPI
            color: 1,1,1,1
            text:"210"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:pocao
            text:""
            halign:("center")
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.38,"center_y":0.10}
            font_style:"H4"

        MDLabel:
            id:MAGIA
            text:"=0"
            halign:("center")
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.955,"center_y":0.3}
            font_style:"H4"
        MDLabel:
            id:FRSI
            color: 1,1,1,1
            text:""
            haling:("center")
            size_hint: (0.5,1)
            pos_hint: {'center_x': 0.6,'center_y': 0.9}
            font_style:"H6"
            
<Quartatela>:
    canvas:
        Color:
            rgba: [1, 1, 1, 1]
    
    
        Rectangle:
            size:self.size[0],self.size[1]
            pos: self.pos
            source:"images/Caverna.jpg"
    FloatLayout:
        orientation: 'vertical'
        MDRectangleFlatButton:
            id:ATT
            text:'         ATAQUE'
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.3}
            on_press:root.atackk()
        MDRectangleFlatButton:
            id:PROXT            
            text:" Proximo "
            font_size:50
            size_hint:(0.5,0.1)
            pos_hint:{"center_x":0.5,"center_y":2}
            on_press:root.manager.current = 'menu'
           
            
            
        MDRectangleFlatButton: 
            id:magica
            text:'MAGIA      '
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.3}
            on_press:root.scroll()
            
            
    
        MDRectangleFlatButton:
            id:cura
            text:"          POÇÃO_CURA"
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.12,"center_y":0.1}
            on_press:root.item()
            
        
    
        MDRectangleFlatIconButton:
            id:sair
            text:"Sair        "
            font_size:50
            size_hint:(0.76,0.2)
            pos_hint:{"center_x":0.88,"center_y":0.1}
            on_press:root.sair()
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.1, "center_y":0.85}
            
        Image:
            size_hint:(0.05,0.05)
            source:"images/d20.png"
            pos_hint: {"center_x": 0.8, "center_y":0.85}
        Image:
            id:esqueleto
            size_hint:(0.7,0.7)
            source: "images/drag.png"
            pos_hint: {'center_x': 0.58,'center_y': 0.6}
        Image:
            image_num: 10
            id:prsn
            size_hint:(0.4,0.4)
            source: "image/person%d.png" % int(self.image_num)
            pos_hint: {'center_x': 0.45,'center_y': 0.6}
            
           
        MDLabel:
            id:NA
            text:"20"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.85}
            font_style:"H6"
        MDLabel:
            color:1,1,1,1
            text:"Valos"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint: {'center_x': 0.1,'center_y': 0.95}
            font_style:"H6"
                
        MDLabel:
            id:INI
            text:"20"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.85}
            font_style:"H6"
                
        MDLabel:
            text:"Vida="
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.1,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HP
            text:"50"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.15,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            text:"Vida="
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.8,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:HPI
            text:"500"
            halign:"center"
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.85,"center_y":0.9}
            font_style:"H6"
        MDLabel:
            id:pocao
            text:""
            halign:("center")
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.38,"center_y":0.10}
            font_style:"H4"
       
        MDLabel:
            id:MAGIA
            text:"=1"
            halign:("center")
            size_hint:(0.8,1)
            pos_hint:{"center_x":0.955,"center_y":0.3}
            font_style:"H4"
        MDLabel:
            id:FRSI
            color: 1,1,1,1
            text:""
            haling:("center")
            size_hint: (0.6,1)
            pos_hint: {'center_x': 0.5,'center_y': 0.9}
            font_style:"H6"
         
              
""")

# Declare both screens
class MenuScreen(MDScreen):
  pass
 
class SettingsScreen(MDScreen):
   
    
    
    def atackk (self):
      
        a=random.randint(1,20)
        b=random.randint(1,18)
        self.ids.NA.text=str(a)
        self.ids.INI.text=str(b)
        self.ids.esqueleto.source="images/esqueleto11.png"
       
        defeated_enemies = 0
        defeated_players = 0

        for player in players:
            d=player.get_hp()
            self.ids.HP.text=str(d)
            for enemy in enemies:
           
                inimihp=enemy.get_hp()
                self.ids.HPI.text=str(inimihp)
                if a>b and enemy.get_hp()>0:

                    dmg = player.generate_damage()
                    enemy=player.choose_target(enemies)
                    self.ids.FRSI.text="Valos atacou o Esqueleto por "+ str(dmg)
                    enemies[enemy].take_damage(dmg)
                    
                    for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                    person_animate.start(self.ids.prsn)
                    for i in range(21,24):
                      self.ids.esqueleto.image_num=21
                      image_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                    image_animate.start(self.ids.esqueleto)

                    if enemies[enemy].get_hp() == 0:
                            
                            for i in range (41,44):
                                self.ids.esqueleto.image_num=41
                                image_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                            image_animate.start(self.ids.esqueleto)
                            defeated_enemies += 1
                            if defeated_enemies==1:
                                    self.ids.FRSI.text="clique em proximo"
                                   
                            print(enemies[enemy].name.replace(" ", "") + " has died.")
                            
            if a==20:
                dmg= player.generate_damage()+20
                enemy=player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                  
                inimihp=enemies[enemy].get_hp()
                for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                person_animate.start(self.ids.prsn)
                for i in range(21,24):
                      self.ids.esqueleto.image_num=21
                      image_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                image_animate.start(self.ids.esqueleto)
                self.ids.HPI.text=str(inimihp)
                self.ids.FRSI.text="Acerto crítico por "+str(dmg)
                if enemies[enemy].get_hp() == 0:
                    for i in range (41,44):
                     self.ids.esqueleto.image_num=41
                     image_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                    image_animate.start(self.ids.esqueleto)
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Você Ganhou /Clique em Proximo")
                            
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                
            else:
                dmg=0
                enemy=player.choose_target(enemies)
                enemies2[enemy].take_damage(dmg)
                  
                inimihp=enemies[enemy].get_hp()
                self.ids.HPI.text=str(inimihp)
                if enemies[enemy].get_hp() == 0:
                  
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Você Ganhou")

                    
         #ATAQUE INIMIGO:     
        for enemy in enemies:
            
                
                if b>a :
                    target = 0
                    enemy_dmg = enemy.generate_damage()
                    self.ids.esqueleto.source="images/esqueleto31.png"
                    
                    if enemy.get_hp()<=0:
                         players[target].take_damage(0)
                    players[target].take_damage(enemy_dmg)
                    d=player.get_hp()
                    self.ids.HP.text=str(d)
                    self.ids.FRSI.text=" Esqueleto atacou Valos por "+ str(enemy_dmg)
                    for i in range(21,23):
                      self.ids.prsn.image_num=21
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                    person_animate.start(self.ids.prsn)
                    for i in range (31,34):
                      self.ids.esqueleto.image_num=31
                      image_animates=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                    image_animates.start(self.ids.esqueleto)
                    if players[target].get_hp() == 0:
                        for i in range(31,35):
                          self.ids.prsn.image_num=31
                          person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                        person_animate.start(self.ids.prsn)
                        
                        print(players[target].name.replace(" ", "") + " has died.")
                          
                        defeated_players += 1
                        if defeated_players==1:
                            self.ids.FRSI.text=("Você Perdeu, o esqueleto conseguio lhe matar")
                            
                       

                else:
                 target = 0
                 enemy_dmg =0

                 players[target].take_damage(enemy_dmg)
                 d=player.get_hp()
                 self.ids.HP.text=str(d)
               
               
                 
               

                 if players[target].get_hp() == 0:
                        print(players[target].name.replace(" ", "") + " has died.")
                       
        defeated_enemies = 0
        defeated_players = 0

        for enemy in enemies:
         if enemy.get_hp() == 0:
           
            
            image_animate.start(self.ids.esqueleto)

            defeated_enemies += 1

        for player in players:
         if player.get_hp() == 0:
            defeated_players += 1    
        if defeated_enemies == 1:
             self.ids.FRSI.text="Você Ganhou!+20ATK/Clique em Proximo"
             self.ids.FRSI.color=1,0,0,1
             self.ids.PROXT.pos_hint={'center_x': 0.5,'center_y': 0.8}
             
          
    # Check if Enemy won
        elif defeated_players == 1:
             self.ids.FRSI.text="Você Perdeu!!!, O esqueleto lhe matou,Clique em Sair"
             self.ids.ATT.pos_hint={'center_x':2.0,'center_y': 2.0}
             self.ids.magica.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.cura.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.sair.pos_hint={'center_x': 0.5,'center_y': 0.25}
             self.ids.pocao.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.MAGIA.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.FRSI.color=1,0,0,1

             

             
             
#criar botão item
#função do botao de item:
 #==============POÇÃO================================
    def item(self):   
        for player in players:  
         player.choose_item()
         item_choice =(0)
         if item_choice == -1:
                    continue

         item = player.items[item_choice]["item"]
         player_hp=player.get_hp()
         if player_hp==250:
             self.ids.FRSI.text="Vida está completa"
             continue
         if player.items[item_choice]["quantity"] == 0:
                    self.ids.FRSI.text="As poções acabaram"
                    continue
         player.items[item_choice]["quantity"] -= 1
         self.ids.pocao.text="="+str(player.items[item_choice]["quantity"])
         if item.type == "potion":
                    player.heal(item.prop)
                    player.heal(item.prop)
                    d=player.get_hp()
                    
                    self.ids.HP.text=str(d)
                    self.ids.FRSI.text="Curou 25 de vida"
                    
   
    def sair(self):
      
        return TestApp().stop()
 
    def scroll(self):
     for player in players:  
        player.choose_item()
        item_choice =(1)
        if item_choice ==-1:
                    continue
        
        item = player_items[item_choice]["item"]
        
        if player_items[item_choice]["quantity"] == 0:
                
                self.ids.FRSI.text="Você não tem  magia"

                continue
        player_items[item_choice]["quantity"] -= 1
          
                
        if  item.type == "attack":
         enemy = player.choose_target(enemies)
         enemies[enemy].take_damage(0)
         if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has died.")
                        del enemies[enemy]
class TerceiraTela(MDScreen):
    def a(self):
        a=player1.get_hp()
        b=self.ids.HP.text=str(a)
        return b
    a

    def atackk (self):
        
        a=random.randint(1,20)
        b=random.randint(1,18)
        self.ids.NA.text=str(a)
        self.ids.INI.text=str(b)
        self.ids.esqueleto.source="images/mago11.png"
       
        defeated_enemies = 0
        defeated_players = 0

        for player in players:
          d=player.get_hp()
          self.ids.HP.text=str(d)
          for enemy in enemies2:
           
            inimihp=enemy.get_hp()
            self.ids.HPI.text=str(inimihp)
            if a>b :

    
                dmg = player.generate_damage()+20
                enemy=player.choose_target(enemies2)
                self.ids.FRSI.text="Valos atacou  Salazar por "+ str(dmg)
           
                
                enemies2[enemy].take_damage(dmg)
                for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                person_animate.start(self.ids.prsn)
                for i in range(31,33):
                     self.ids.esqueleto.image_num=31
                     image_mago=Animation(x=(i+10),image_num=i,d=(0.30*1))
                image_mago.start(self.ids.esqueleto)
               

                if enemies2[enemy].get_hp() == 0:
                    for i in range(41,44):
                        self.ids.esqueleto.image_num=41
                        img_mago=Animation(x=(i+10),image_num=i,d=(0.30*1))
                    img_mago.start(self.ids.esqueleto)    
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Você Ganhou  /Clique Proximo")
                            
                            
                    print(enemies2[enemy].name.replace(" ", "") + " has died.")
                
            if a==20:
                dmg= player.generate_damage()+35
                enemy=player.choose_target(enemies2)
                enemies2[enemy].take_damage(dmg)
                self.ids.FRSI.text="Acerto crítico atacou o Salazar por "+str(dmg)
                for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                person_animate.start(self.ids.prsn)
                for i in range(31,33):
                     self.ids.esqueleto.image_num=31
                     image_mago=Animation(x=(i+10),image_num=i,d=(0.30*1))
                image_mago.start(self.ids.esqueleto)
               
                
                
            
                inimihp=enemies2[enemy].get_hp()
                self.ids.HPI.text=str(inimihp)

                if enemies2[enemy].get_hp() == 0:
                    for i in range(41,44):
                        self.ids.esqueleto.image_num=41
                        img_mago=Animation(x=(i+10),image_num=i,d=(0.30*1))
                    img_mago.start(self.ids.esqueleto)  
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Você Ganhou /Clique em Proximo")
                            
                            
                    print(enemies2[enemy].name.replace(" ", "") + " has died.")
                
            else:
                dmg=0
                enemy=player.choose_target(enemies2)
                enemies2[enemy].take_damage(dmg)
                  
                inimihp=enemies2[enemy].get_hp()
                self.ids.HPI.text=str(inimihp)
                if enemies2[enemy].get_hp() == 0:
                    print(enemies2[enemy].name.replace(" ", "") + " has died.")
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text="Você Ganhou"
                    
         #ATAQUE INIMIGO:     
        for enemy in enemies2:
                if b>a :
                 target = 0
                 enemy_dmg = enemy.generate_damage()
                 for i in range(21,23):
                      self.ids.prsn.image_num=21
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                 person_animate.start(self.ids.prsn)
                 for i in range(21,24):
                      self.ids.esqueleto.image_num=21
                      image_mago=Animation(x=(i+10),image_num=i,d=(0.30*1))
                 image_mago.start(self.ids.esqueleto)
                
                 if enemy.get_hp()<=0:
                         players[target].take_damage(0)
                 players[target].take_damage(enemy_dmg)
                 d=player.get_hp()
                 self.ids.HP.text=str(d)
                 self.ids.FRSI.text=" Salazar atacou Valos por "+str(enemy_dmg)
                
                 if players[target].get_hp() == 0:
                        
                        print(players[target].name.replace(" ", "") + " has died.")
                        for i in range(31,35):
                          self.ids.prsn.image_num=31
                          person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                        person_animate.start(self.ids.prsn)
                          
                        defeated_players += 1
                        if defeated_players==1:
                            self.ids.FRSI.text=("Você Perdeu, Salazar conseguio lhe matar")
        
                else:
                 target = 0
                 enemy_dmg =0

                 players[target].take_damage(enemy_dmg)
                 d=player.get_hp()
                 self.ids.HP.text=str(d)
               
                 self.a=print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)
                 if players[target].get_hp() == 0:
                        print(players[target].name.replace(" ", "") + " has died.")
                       
        defeated_enemies = 0
        defeated_players = 0

        for enemy in enemies2:
         if enemy.get_hp() == 0:
            defeated_enemies += 1

        for player in players:
         if player.get_hp() == 0:
            defeated_players += 1    
        if defeated_enemies == 1:
             self.ids.FRSI.text="Você Ganhou!,Adiquirio Magia:Nevasca,+10ATK/Clique em Proximo"
             self.ids.PROXT.pos_hint={'center_x': 0.5,'center_y': 0.8}
             self.ids.FRSI.color=1,0,0,1
             
    
        elif defeated_players == 1:
             self.ids.FRSI.text="Valos sucumbio a magia de Salazar,Clique em sair"
             self.ids.ATT.pos_hint={'center_x': 2.0,'center_y': 2.0}
             self.ids.FRSI.color=1,0,0,1
             self.ids.magica.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.cura.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.sair.pos_hint={'center_x': 0.5,'center_y': 0.25}
             self.ids.pocao.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.MAGIA.pos_hint={'center_x': 2.0,'center_y': 2.0}

 #==============POÇÃO================================
    def item(self):   
        for player in players:  
         player.choose_item()
         item_choice =(0)
         if item_choice == -1:
                    continue

         item = player.items[item_choice]["item"]
         player_hp=player.get_hp()
         if player_hp==250:
             self.ids.FRSI.text="Vida está completa"
             continue
         if player.items[item_choice]["quantity"] == 0:
                    self.ids.FRSI.text="Valos não tem poção"
                    print("None left..." )
                    continue
         player.items[item_choice]["quantity"] -= 1
         self.ids.pocao.text="="+str(player.items[item_choice]["quantity"])
         if item.type == "potion":
                    player.heal(item.prop)
                    d=player.get_hp()
                    self.ids.HP.text=str(d)
                    self.ids.FRSI.text="Curou 25 de vida"
                    

    
    
        
    #BOTÃO DE SAIR=============================================================      
    def sair(self):
        return   TestApp().stop()
    
    #=====================BLIZARD==============================================
    def scroll(self):
     for player in players:  
        player.choose_item()
        item_choice =(1)
        if item_choice ==-1:
                    continue
        
        item = player_items[item_choice]["item"]
        
        if player_items[item_choice]["quantity"] == 0:
                self.ids.FRSI.text="Você não tem Magia"

                continue
        player_items[item_choice]["quantity"] -= 1
          
                
        if  item.type == "attack":
         enemy = player.choose_target(enemies2)
         enemies2[enemy].take_damage(0)
         
         if enemies2[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") + " has died.")
                        del enemies[enemy]
class Quartatela(MDScreen):
    
    def atackk (self):
        
        a=random.randint(1,20)
        b=random.randint(1,18)
        self.ids.NA.text=str(a)
        self.ids.INI.text=str(b)
        self.ids.esqueleto.source="images/drag3.png"
       
        defeated_enemies = 0
        defeated_players = 0

        for player in players:
          d=player.get_hp()
          self.ids.HP.text=str(d)
          for enemy in enemies3:
           
            inimihp=enemy.get_hp()
            self.ids.HPI.text=str(inimihp)
            if a>b :

    
             dmg = player.generate_damage()+30
             enemy=player.choose_target(enemies3)
             self.ids.FRSI.text="Valos atacou o Dragão por "+str(dmg)
             
                
             enemies3[enemy].take_damage(dmg)
             for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
             person_animate.start(self.ids.prsn)
             self.ids.esqueleto.source="images/drag3.png"

             if enemies3[enemy].get_hp() == 0:
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Você Ganhou  /Clique Proximo")
                            self.ids.esqueleto.source="images/drag4.png"
                    print(enemies2[enemy].name.replace(" ", "") + " has died.")
                
            if a==20:
                dmg= player.generate_damage()+50
                enemy=player.choose_target(enemies3)
                enemies3[enemy].take_damage(dmg)
                self.ids.FRSI.text="Acerto crítico atacou Alduin por "+str(dmg)
                
                for i in range(11,14):
                      self.ids.prsn.image_num=11
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                person_animate.start(self.ids.prsn)
                inimihp=enemies3[enemy].get_hp()
                self.ids.HPI.text=str(inimihp)

                if enemies3[enemy].get_hp() == 0:
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text=("Parabéns,você derrotou os monstros,Valos terá sua liberdade")
                            self.ids.esqueleto.source="images/drag4.png"
                    print(enemies3[enemy].name.replace(" ", "") + " has died.")
                
            else:
                dmg=0
                enemy=player.choose_target(enemies2)
                enemies3[enemy].take_damage(dmg)
                  
                inimihp=enemies3[enemy].get_hp()
                self.ids.HPI.text=str(inimihp)
                if enemies3[enemy].get_hp() == 0:
                    print(enemies3[enemy].name.replace(" ", "") + " has died.")
                    defeated_enemies += 1
                    if defeated_enemies==1:
                            self.ids.FRSI.text="Você Ganhou"
                    
         #ATAQUE INIMIGO:     
        for enemy in enemies3:
                if b>a :
                 target = 0
                 enemy_dmg = enemy.generate_damage()
                 self.ids.esqueleto.source="images/drag2.png"
                 for i in range(21,23):
                      self.ids.prsn.image_num=21
                      person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                 person_animate.start(self.ids.prsn)
                 if enemy.get_hp()<=0:
                         players[target].take_damage(0)
                 players[target].take_damage(enemy_dmg)
                 d=player.get_hp()
                 self.ids.HP.text=str(d)
                 self.ids.FRSI.text=" Alduin atacou Valos por "+str(enemy_dmg)
                 
                
                 if players[target].get_hp() == 0:
                        
                        print(players[target].name.replace(" ", "") + " has died.")
                        for i in range(31,35):
                          self.ids.prsn.image_num=31
                          person_animate=Animation(x=(i+10),image_num=i,duration=(0.30*1))
                        person_animate.start(self.ids.prsn)
                          
                        defeated_players += 1
                        if defeated_players==1:
                            self.ids.FRSI.text=("Você Perdeu,Valos queimou pelo fogo de Alduin")
        
                else:
                 target = 0
                 enemy_dmg =0

                 players[target].take_damage(enemy_dmg)
                 d=player.get_hp()
                 self.ids.HP.text=str(d)
               
                 self.a=print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)
                 if players[target].get_hp() == 0:
                        print(players[target].name.replace(" ", "") + " has died.")
                       
        defeated_enemies = 0
        defeated_players = 0

        for enemy in enemies3:
         if enemy.get_hp() == 0:
            defeated_enemies += 1

        for player in players:
         if player.get_hp() == 0:
            defeated_players += 1    
        if defeated_enemies == 1:
             self.ids.FRSI.text="Parabéns,você derrotou os monstros,Valos terá sua liberdade"
             self.ids.esqueleto.source="images/drag4.png"
             self.ids.PROXT.pos_hint={'center_x': 0.5,'center_y': 0.8}
             self.ids.FRSI.color=1,0,0,1

        elif defeated_players == 1:
             self.ids.FRSI.text="Valos queimou pelo fogo de Alduin,Clique em Sair"
             self.ids.ATT.pos_hint={'center_x': 2.0,'center_y': 2.0}
             self.ids.FRSI.color=1,0,0,1
             self.ids.magica.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.cura.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.sair.pos_hint={'center_x': 0.5,'center_y': 0.25}
             self.ids.pocao.pos_hint= {'center_x': 2.0,'center_y': 2.0}
             self.ids.MAGIA.pos_hint={'center_x': 2.0,'center_y': 2.0}

 #==============POÇÃO================================
    def item(self):   
        for player in players:  
         player.choose_item()
         item_choice =(0)
         if item_choice == -1:
                    continue

         item = player.items[item_choice]["item"]
         player_hp=player.get_hp()
        
         if player_hp==250:
            self.ids.FRSI.text="Vida está completa"
            continue
         player.items[item_choice]["quantity"] -= 1
         if player.items[item_choice]["quantity"] <= 0:
                    self.ids.FRSI.text="Valos não tem poçao"
         self.ids.pocao.text="="+str(player.items[item_choice]["quantity"])
         if item.type == "potion":
                    player.heal(item.prop)
                 
                    self.ids.HP.text=str(player_hp)
                    self.ids.FRSI.text="Curou 25 de vida"
    #BOTÃO DE SAIR=============================================================      
    def sair(self):
        return TestApp().stop()
    #=====================BLIZARD==============================================
    def scroll(self):
     for player in players: 
        for enemy in enemies3: 
         player.choose_item()
         item_choice =(1)
         if item_choice ==-1:
                    continue
        
         item = player_items[item_choice]["item"]
         player_items[item_choice]["quantity"] -= 1
         self.ids.MAGIA.text="=0"
          
         if player_items[item_choice]["quantity"]==0 :
          self.ids.FRSI.text="Valos não tem Mana o suficiente"
         
         if  item.type == "attack":
          enemy = player.choose_target(enemies3)
          enemies3[enemy].take_damage(item.prop)
          self.ids.FRSI.text="Uma Nevasca se forma, dano= "+str(250)
          self.ids.esqueleto.source="images/drag3.png"
          d=enemies3[enemy].get_hp()
          self.ids.HPI.text=str(d)
                  
          if enemies3[enemy].get_hp() == 0:
                        d=enemies3[enemy].get_hp()
                        self.ids.HPI.text=str(d)
                        print(enemies3[enemy].name.replace(" ", "") + " has died.")
                        self.ids.FRSI.text="Parabéns,você derrotou os monstros,Valos terá sua liberdade"
                        self.ids.FRSI.color=1,0,0,1
                        self.ids.esqueleto.source="images/drag4.png"
                        del enemies3[enemy]
     
      
class TestApp(MDApp):
  
    def build(self):
        
        
        self.theme_cls.primary_palette ="DeepOrange"
       
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='jogo'))
        sm.add_widget(TerceiraTela(name='terceira'))
        sm.add_widget(Quartatela(name='quarta'))
        
        return sm

if __name__ == '__main__':
    TestApp().run()