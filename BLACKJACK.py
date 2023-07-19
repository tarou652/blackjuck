import pygame
from pygame.locals import*			#pygameの使用を簡単にする
import sys					#sysをインポート
import random
import time
import app 
import webbrowser
import datetime
imgD1=pygame.image.load("aseet/D1.png")
imgD1= pygame.transform.scale(imgD1, (89, 126))
imgD2=pygame.image.load("aseet/D2.png")
imgD2= pygame.transform.scale(imgD2, (89, 126))
imgD3=pygame.image.load("aseet/D3.png")
imgD3= pygame.transform.scale(imgD3, (89, 126))
imgD4=pygame.image.load("aseet/D4.png")
imgD4= pygame.transform.scale(imgD4, (89, 126))
imgD5=pygame.image.load("aseet/D5.png")
imgD5= pygame.transform.scale(imgD5, (89, 126))
imgD6=pygame.image.load("aseet/D6.png")
imgD6= pygame.transform.scale(imgD6, (89, 126))
imgD7=pygame.image.load("aseet/D7.png")
imgD7= pygame.transform.scale(imgD7, (89, 126))
imgD8=pygame.image.load("aseet/D8.png")
imgD8= pygame.transform.scale(imgD8, (89, 126))
imgD9=pygame.image.load("aseet/D9.png")
imgD9= pygame.transform.scale(imgD9, (89, 126))
imgD10=pygame.image.load("aseet/D10.png")
imgD10= pygame.transform.scale(imgD10, (89, 126))
imgDJ=pygame.image.load("aseet/DJ.png")
imgDJ= pygame.transform.scale(imgDJ, (89, 126))
imgDQ=pygame.image.load("aseet/DQ.png")
imgDQ= pygame.transform.scale(imgDQ, (89, 126))
imgDK=pygame.image.load("aseet/DK.png")
imgDK= pygame.transform.scale(imgDK, (89, 126))
imgS1=pygame.image.load("aseet/S1.png")
imgS1= pygame.transform.scale(imgS1, (89, 126))
imgS2=pygame.image.load("aseet/S2.png")
imgS2= pygame.transform.scale(imgS2, (89, 126))
imgS3=pygame.image.load("aseet/S3.png")
imgS3= pygame.transform.scale(imgS3, (89, 126))
imgS4=pygame.image.load("aseet/S4.png")
imgS4= pygame.transform.scale(imgS4, (89, 126))
imgS5=pygame.image.load("aseet/S5.png")
imgS5= pygame.transform.scale(imgS5, (89, 126))
imgS6=pygame.image.load("aseet/S6.png")
imgS6= pygame.transform.scale(imgS6, (89, 126))
imgS7=pygame.image.load("aseet/S7.png")
imgS7= pygame.transform.scale(imgS7, (89, 126))
imgS8=pygame.image.load("aseet/S8.png")
imgS8= pygame.transform.scale(imgS8, (89, 126))
imgS9=pygame.image.load("aseet/S9.png")
imgS9= pygame.transform.scale(imgS9, (89, 126))
imgS10=pygame.image.load("aseet/S10.png")
imgS10= pygame.transform.scale(imgS10, (89, 126))
imgSJ=pygame.image.load("aseet/SJ.png")
imgSJ= pygame.transform.scale(imgSJ, (89, 126))
imgSQ=pygame.image.load("aseet/SQ.png")
imgSQ= pygame.transform.scale(imgSQ, (89, 126))
imgSK=pygame.image.load("aseet/SK.png")
imgSK= pygame.transform.scale(imgSK, (89, 126))
imgK1=pygame.image.load("aseet/K1.png")
imgK1= pygame.transform.scale(imgK1, (89, 126))
imgK2=pygame.image.load("aseet/K2.png")
imgK2= pygame.transform.scale(imgK2, (89, 126))
imgK3=pygame.image.load("aseet/K3.png")
imgK3= pygame.transform.scale(imgK3, (89, 126))
imgK4=pygame.image.load("aseet/K4.png")
imgK4= pygame.transform.scale(imgK4, (89, 126))
imgK5=pygame.image.load("aseet/K5.png")
imgK5= pygame.transform.scale(imgK5, (89, 126))
imgK6=pygame.image.load("aseet/K6.png")
imgK6= pygame.transform.scale(imgK6, (89, 126))
imgK7=pygame.image.load("aseet/K7.png")
imgK7= pygame.transform.scale(imgK7, (89, 126))
imgK8=pygame.image.load("aseet/K8.png")
imgK8= pygame.transform.scale(imgK8, (89, 126))
imgK9=pygame.image.load("aseet/K9.png")
imgK9= pygame.transform.scale(imgK9, (89, 126))
imgK10=pygame.image.load("aseet/K10.png")
imgK10= pygame.transform.scale(imgK10, (89, 126))
imgKJ=pygame.image.load("aseet/KJ.png")
imgKJ= pygame.transform.scale(imgKJ, (89, 126))
imgKQ=pygame.image.load("aseet/KQ.png")
imgKQ= pygame.transform.scale(imgKQ, (89, 126))
imgKK=pygame.image.load("aseet/KK.png")
imgKK= pygame.transform.scale(imgKK, (89, 126))
imgH1=pygame.image.load("aseet/H1.png")
imgH1= pygame.transform.scale(imgH1, (89, 126))
imgH2=pygame.image.load("aseet/H2.png")
imgH2= pygame.transform.scale(imgH2, (89, 126))
imgH3=pygame.image.load("aseet/H3.png")
imgH3= pygame.transform.scale(imgH3, (89, 126))
imgH4=pygame.image.load("aseet/H4.png")
imgH4= pygame.transform.scale(imgH4, (89, 126))
imgH5=pygame.image.load("aseet/H5.png")
imgH5= pygame.transform.scale(imgH5, (89, 126))
imgH6=pygame.image.load("aseet/H6.png")
imgH6= pygame.transform.scale(imgH6, (89, 126))
imgH7=pygame.image.load("aseet/H7.png")
imgH7= pygame.transform.scale(imgH7, (89, 126))
imgH8=pygame.image.load("aseet/H8.png")
imgH8= pygame.transform.scale(imgH8, (89, 126))
imgH9=pygame.image.load("aseet/H9.png")
imgH9= pygame.transform.scale(imgH9, (89, 126))
imgH10=pygame.image.load("aseet/H10.png")
imgH10= pygame.transform.scale(imgH10, (89, 126))
imgHJ=pygame.image.load("aseet/HJ.png")
imgHJ= pygame.transform.scale(imgHJ, (89, 126))
imgHQ=pygame.image.load("aseet/HQ.png")
imgHQ= pygame.transform.scale(imgHQ, (89, 126))
imgHK=pygame.image.load("aseet/HK.png")
imgHK= pygame.transform.scale(imgHK, (89, 126))
imgback=pygame.image.load("aseet/back.png")
imgback=pygame.transform.scale(imgback,(89,126))

round=0



      
def text2(screen,Pcount,Dcount):
    font2 = pygame.font.Font(None, 40) 

    playIsuu=font2.render(str(Pcount),True,(255,255,255))
    
    deler=font2.render("Dealer",True,(255,255,255))
    delersuu=font2.render(str(Dcount),True,(255,255,255))
    playI=font2.render("Player",True,(255,255,255))               
    screen.blit(deler,[50,100])
    screen.blit(playI,[50,300])
    screen.blit(delersuu,(50,150))
    screen.blit(playIsuu,(50,350))   
def end(screen,money):
    time=datetime.datetime.now()
    money=int(money)
    score=str(money)
    screen.fill((0,100,0))
    font = pygame.font.Font(None, 50) 
    font2 = pygame.font.Font(None, 100) 
    stare=font2.render("Press N key to restart",True,(255,255,255))
    scoretext=font.render("SCORE  "+score,True,(255,255,255))
    gameover=font2.render("GAMEOVER",True,(255,255,255))
    with open("score.txt","r") as f:
        high = f.read()
        if int(high)<int(score):
            with open("score.txt","w") as q:
                q.write(score)
            with open("score.txt","r") as a:
                high=  a.read()
        highscore=font.render("HIGHSCORE  "+high,True,(255,255,255))    
    with open("lastscore.txt","a",encoding='UTF-8') as p:
          p.write("{0}\n".format(score))
    with open("time.txt","a",encoding='UTF-8') as e:
          e.write("{0}年{1}月{2}日\n".format(time.year,time.month,time.day))
    screen.blit(highscore,[50,80])
    screen.blit(gameover,[180,180])
    screen.blit(stare,[80,350])
    screen.blit(scoretext,[50,50])
    pygame.display.update()  
    run=True
    while run:
         for event in pygame.event.get():
            

            
            if event.type == KEYDOWN: 
                if event.key==K_q:
                   pygame.display.update()   
                               
                if event.key==K_ESCAPE:
                   
                 webbrowser.open("http://localhost:5000/")
                 pygame.quit()
                 sys.exit() # キーを押したとき
                if event.key==K_n:
                    round=0
                    run=False
                    main()

            if event.type == QUIT:
                webbrowser.open("http://localhost:5000/")  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
                
def text(screen,money,kakemoney):
    
    
    font2 = pygame.font.Font(None, 40)  
    screen.fill((0,100,0))
    kane=font2.render("Money   "+str(money), True, (255,255,255))
    kake=font2.render("Bet   "+str(kakemoney), True, (255,255,255))
    screen.blit(kane, [50, 450]) 
    screen.blit(kake, [50, 500])
    pygame.display.update() 
def drow(screen,money,kakemoney):
    font2 = pygame.font.Font(None, 40) 
    Drowttext=font2.render("DROW",True,(255,255,255))
    screen.blit(Drowttext,[50,250])
    money=money+kakemoney
    pygame.display.update() 
    time.sleep(3)
    screen.fill((0,100,0))
    pygame.display.update() 
    Game(screen,money)
    
    
def Strat(screen):
    font1 = pygame.font.Font(None, 150) 
    font = pygame.font.Font(None, 100) 
    text1 = font.render("Spece to Strat", True, (255,255,255))   # 画面を更新
    text = font1.render("Black Jack", True, (255,255,255))   
    
    
    screen.fill((0,100,0)) 
    screen.blit(text, [100, 100]) 
    screen.blit(text1, [120, 350]) 
    pygame.display.update() 
def Pbarst(screen,money):
    font2 = pygame.font.Font(None, 40) 
    Dbardttext=font2.render("BURST",True,(255,255,255))
    screen.blit(Dbardttext,[50,250])
    pygame.display.update() 
    time.sleep(3)
    screen.fill((0,100,0))
    pygame.display.update() 
    Game(screen,money)
def Dbarst(screen,money):
    font2 = pygame.font.Font(None, 40) 
    Pbardttext=font2.render("BURST",True,(255,255,255))
    screen.blit(Pbardttext,[50,50])
    pygame.display.update() 
    
def Pwin(screen,money,kakemoney):
    font2 = pygame.font.Font(None, 40) 
    Winttext=font2.render("WIN",True,(255,255,255))
    screen.blit(Winttext,[50,250])
    money=money+kakemoney*2
    pygame.display.update() 
    time.sleep(3)
    Game(screen,money)
def Ploose(screen,money):
    font2 = pygame.font.Font(None, 40) 
    loosettext=font2.render("LOSE",True,(255,255,255))
    screen.blit(loosettext,[50,250])
    pygame.display.update() 
    time.sleep(3)
    screen.fill((0,100,0))
    pygame.display.update() 
    Game(screen,money)
def Pblack(screen,money,kakemoney):
    font2 = pygame.font.Font(None, 40) 
    blackttext=font2.render("BLACK JACK",True,(255,255,255))
    screen.blit(blackttext,[50,250])
    money=money+kakemoney*2.5
    pygame.display.update() 
    time.sleep(3)


    Game(screen,money)   
def kardP5(P5,screen):

    if P5=="D1":
                   
        screen.blit(imgD1,(610,280))
    if P5=="D2":
                    
        screen.blit(imgD2,(610,280))
    if P5=="D3":
                    
        screen.blit(imgD3,(610,280))
    if P5=="D4":
                   
        screen.blit(imgD4,(610,280))
    if P5=="D5":
                   
        screen.blit(imgD5,(610,280))
    if P5=="D6":
                   
        screen.blit(imgD6,(610,280))
    if P5=="D7":
                   
        screen.blit(imgD7,(610,280))
    if P5=="D8":
                    
        screen.blit(imgD8,(610,280))
    if P5=="D9":
                    
        screen.blit(imgD9,(610,280))  
    if P5=="D10":
                   
        screen.blit(imgD10,(610,280)) 
    if P5=="DJ":
                   
        screen.blit(imgDJ,(610,280)) 
    if P5=="DQ":
                   
        screen.blit(imgDQ,(610,280)) 
    if P5=="DK":
                    
        screen.blit(imgDK,(610,280)) 
    if P5=="K1":
                   
        screen.blit(imgK1,(610,280))
    if P5=="K2":
                    
        screen.blit(imgK2,(610,280))  
    if P5=="K3":
                   
        screen.blit(imgK3,(610,280))   
    if P5=="K4":
                    
        screen.blit(imgK4,(610,280))  
    if P5=="K5":
                    
        screen.blit(imgK5,(610,280))  
    if P5=="K6":
                   
        screen.blit(imgK6,(610,280))  
    if P5=="K7":
                    
        screen.blit(imgK7,(610,280))  
    if P5=="K8":
                   
        screen.blit(imgK8,(610,280))  
    if P5=="K9":
                   
        screen.blit(imgK9,(610,280))  
    if P5=="K10":
                   
        screen.blit(imgK10,(610,280))  
    if P5=="KJ":
                    
        screen.blit(imgKJ,(610,280))  
    if P5=="KQ":
         screen.blit(imgKQ,(610,280)) 
    if P5=="KK" :       
        screen.blit(imgKK,(610,280)) 
                     
    if P5=="H1":
                    
        screen.blit(imgH1,(610,280)) 
    if P5=="H2":
                  
        screen.blit(imgH2,(610,280)) 
    if P5=="H3":
                   
        screen.blit(imgH3,(610,280)) 
    if P5=="H4":
                   
        screen.blit(imgH4,(610,280)) 
    if P5=="H5":
                    
        screen.blit(imgH5,(610,280)) 
    if P5=="H6":
                   
        screen.blit(imgH6,(610,280)) 
    if P5=="H7":
                    
        screen.blit(imgH7,(610,280)) 
    if P5=="H8":
                    
        screen.blit(imgH8,(610,280)) 
    if P5=="H9":
                    
        screen.blit(imgH9,(610,280)) 
    if P5=="H10":
                    
        screen.blit(imgH10,(610,280)) 
    if P5=="HJ":
                   
        screen.blit(imgHJ,(610,280)) 
    if P5=="HQ":
                    
        screen.blit(imgHQ,(610,280)) 
    if P5=="HK":
                    
        screen.blit(imgHK,(610,280))
    if P5=="S1":
                    
        screen.blit(imgS1,(610,280))  
    if P5=="S2":
                   
        screen.blit(imgS2,(610,280)) 
    if P5=="S3":
                   
        screen.blit(imgS3,(610,280)) 
    if P5=="S4":
                    
        screen.blit(imgS4,(610,280)) 
    if P5=="S5":
                    
        screen.blit(imgS5,(610,280))
    if P5=="S6":
                 
        screen.blit(imgS6,(610,280)) 
                    
    if P5=="S7":
                   
        screen.blit(imgS7,(610,280)) 
    if P5=="S8":
                   
        screen.blit(imgS8,(610,280)) 
    if P5=="S9":
                   
        screen.blit(imgS9,(610,280)) 
    if P5=="S10":
                    
        screen.blit(imgS10,(610,280))
    if P5=="SJ":
                   
        screen.blit(imgSJ,(610,280))  
    if P5=="SQ":
                  
        screen.blit(imgSQ,(610,280)) 
    if P5=="SK":
                    
        screen.blit(imgSK,(610,280)) 
def kardP4(P4,screen):

    if P4=="D1":
                   
        screen.blit(imgD1,(500,280))
    if P4=="D2":
                    
        screen.blit(imgD2,(500,280))
    if P4=="D3":
                    
        screen.blit(imgD3,(500,280))
    if P4=="D4":
                   
        screen.blit(imgD4,(500,280))
    if P4=="D5":
                   
        screen.blit(imgD5,(500,280))
    if P4=="D6":
                   
        screen.blit(imgD6,(500,280))
    if P4=="D7":
                   
        screen.blit(imgD7,(500,280))
    if P4=="D8":
                    
        screen.blit(imgD8,(500,280))
    if P4=="D9":
                    
        screen.blit(imgD9,(500,280))  
    if P4=="D10":
                   
        screen.blit(imgD10,(500,280)) 
    if P4=="DJ":
                   
        screen.blit(imgDJ,(500,280)) 
    if P4=="DQ":
                   
        screen.blit(imgDQ,(500,280)) 
    if P4=="DK":
                    
        screen.blit(imgDK,(500,280)) 
    if P4=="K1":
                   
        screen.blit(imgK1,(500,280))
    if P4=="K2":
                    
        screen.blit(imgK2,(500,280))  
    if P4=="K3":
                   
        screen.blit(imgK3,(500,280))   
    if P4=="K4":
                    
        screen.blit(imgK4,(500,280))  
    if P4=="K5":
                    
        screen.blit(imgK5,(500,280))  
    if P4=="K6":
                   
        screen.blit(imgK6,(500,280))  
    if P4=="K7":
                    
        screen.blit(imgK7,(500,280))  
    if P4=="K8":
                   
        screen.blit(imgK8,(500,280))  
    if P4=="K9":
                   
        screen.blit(imgK9,(500,280))  
    if P4=="K10":
                   
        screen.blit(imgK10,(500,280))  
    if P4=="KJ":
                    
        screen.blit(imgKJ,(500,280))  
    if P4=="KQ":
         screen.blit(imgKQ,(500,280)) 
    if P4=="KK" :       
        screen.blit(imgKK,(500,280)) 
                     
    if P4=="H1":
                    
        screen.blit(imgH1,(500,280)) 
    if P4=="H2":
                  
        screen.blit(imgH2,(500,280)) 
    if P4=="H3":
                   
        screen.blit(imgH3,(500,280)) 
    if P4=="H4":
                   
        screen.blit(imgH4,(500,280)) 
    if P4=="H5":
                    
        screen.blit(imgH5,(500,280)) 
    if P4=="H6":
                   
        screen.blit(imgH6,(500,280)) 
    if P4=="H7":
                    
        screen.blit(imgH7,(500,280)) 
    if P4=="H8":
                    
        screen.blit(imgH8,(500,280)) 
    if P4=="H9":
                    
        screen.blit(imgH9,(500,280)) 
    if P4=="H10":
                    
        screen.blit(imgH10,(500,280)) 
    if P4=="HJ":
                   
        screen.blit(imgHJ,(500,280)) 
    if P4=="HQ":
                    
        screen.blit(imgHQ,(500,280)) 
    if P4=="HK":
                    
        screen.blit(imgHK,(500,280))
    if P4=="S1":
                    
        screen.blit(imgS1,(500,280))  
    if P4=="S2":
                   
        screen.blit(imgS2,(500,280)) 
    if P4=="S3":
                   
        screen.blit(imgS3,(500,280)) 
    if P4=="S4":
                    
        screen.blit(imgS4,(500,280)) 
    if P4=="S5":
                    
        screen.blit(imgS5,(500,280))
    if P4=="S6":
                   
        screen.blit(imgS6,(500,280)) 
                    
    if P4=="S7":
                   
        screen.blit(imgS7,(500,280)) 
    if P4=="S8":
                   
        screen.blit(imgS8,(500,280)) 
    if P4=="S9":
                   
        screen.blit(imgS9,(500,280)) 
    if P4=="S10":
                    
        screen.blit(imgS10,(500,280))
    if P4=="SJ":
                   
        screen.blit(imgSJ,(500,280))  
    if P4=="SQ":
                  
        screen.blit(imgSQ,(500,280)) 
    if P4=="SK":
                    
        screen.blit(imgSK,(500,280)) 
def kardP3(P3,screen):

    if P3=="D1":
                   
        screen.blit(imgD1,(390,280))
    if P3=="D2":
                    
        screen.blit(imgD2,(390,280))
    if P3=="D3":
                    
        screen.blit(imgD3,(390,280))
    if P3=="D4":
                   
        screen.blit(imgD4,(390,280))
    if P3=="D5":
                   
        screen.blit(imgD5,(390,280))
    if P3=="D6":
                   
        screen.blit(imgD6,(390,280))
    if P3=="D7":
                   
        screen.blit(imgD7,(390,280))
    if P3=="D8":
                    
        screen.blit(imgD8,(390,280))
    if P3=="D9":
                    
        screen.blit(imgD9,(390,280))  
    if P3=="D10":
                   
        screen.blit(imgD10,(390,280)) 
    if P3=="DJ":
                   
        screen.blit(imgDJ,(390,280)) 
    if P3=="DQ":
                   
        screen.blit(imgDQ,(390,280)) 
    if P3=="DK":
                    
        screen.blit(imgDK,(390,280)) 
    if P3=="K1":
                   
        screen.blit(imgK1,(390,280))
    if P3=="K2":
                    
        screen.blit(imgK2,(390,280))  
    if P3=="K3":
                   
        screen.blit(imgK3,(390,280))   
    if P3=="K4":
                    
        screen.blit(imgK4,(390,280))  
    if P3=="K5":
                    
        screen.blit(imgK5,(390,280))  
    if P3=="K6":
                   
        screen.blit(imgK6,(390,280))  
    if P3=="K7":
                    
        screen.blit(imgK7,(390,280))  
    if P3=="K8":
                   
        screen.blit(imgK8,(390,280))  
    if P3=="K9":
                   
        screen.blit(imgK9,(390,280))  
    if P3=="K10":
                   
        screen.blit(imgK10,(390,280))  
    if P3=="KJ":
                    
        screen.blit(imgKJ,(390,280))  
    if P3=="KQ":
         screen.blit(imgKQ,(390,280)) 
    if P3=="KK" :       
        screen.blit(imgKK,(390,280)) 
                     
    if P3=="H1":
                    
        screen.blit(imgH1,(390,280)) 
    if P3=="H2":
                  
        screen.blit(imgH2,(390,280)) 
    if P3=="H3":
                   
        screen.blit(imgH3,(390,280)) 
    if P3=="H4":
                   
        screen.blit(imgH4,(390,280)) 
    if P3=="H5":
                    
        screen.blit(imgH5,(390,280)) 
    if P3=="H6":
                   
        screen.blit(imgH6,(390,280)) 
    if P3=="H7":
                    
        screen.blit(imgH7,(390,280)) 
    if P3=="H8":
                    
        screen.blit(imgH8,(390,280)) 
    if P3=="H9":
                    
        screen.blit(imgH9,(390,280)) 
    if P3=="H10":
                    
        screen.blit(imgH10,(390,280)) 
    if P3=="HJ":
                   
        screen.blit(imgHJ,(390,280)) 
    if P3=="HQ":
                    
        screen.blit(imgHQ,(390,280)) 
    if P3=="HK":
                    
        screen.blit(imgHK,(390,280))
    if P3=="S1":
                    
        screen.blit(imgS1,(390,280))  
    if P3=="S2":
                   
        screen.blit(imgS2,(390,280)) 
    if P3=="S3":
                   
        screen.blit(imgS3,(390,280)) 
    if P3=="S4":
                    
        screen.blit(imgS4,(390,280)) 
    if P3=="S5":
                    
        screen.blit(imgS5,(390,280))
    if P3=="S6":
                   
        screen.blit(imgS6,(390,280)) 
                    
    if P3=="S7":
                   
        screen.blit(imgS7,(390,280)) 
    if P3=="S8":
                   
        screen.blit(imgS8,(390,280)) 
    if P3=="S9":
                   
        screen.blit(imgS9,(390,280)) 
    if P3=="S10":
                    
        screen.blit(imgS10,(390,280))
    if P3=="SJ":
                   
        screen.blit(imgSJ,(390,280))  
    if P3=="SQ":
                  
        screen.blit(imgSQ,(390,280)) 
    if P3=="SK":
                    
        screen.blit(imgSK,(390,280)) 
def kardD5(D5,screen):

    if D5=="D1":
                    
           screen.blit(imgD1,(610,60))
    if D5=="D2":
                   
           screen.blit(imgD2,(610,60))
    if D5=="D3":
                    
           screen.blit(imgD3,(610,60))
    if D5=="D4":
                    
           screen.blit(imgD4,(610,60))
    if D5=="D5":
                    
           screen.blit(imgD5,(610,60))
    if D5=="D6":
                    
           screen.blit(imgD6,(610,60))
    if D5=="D7":
                   
           screen.blit(imgD7,(610,60))
    if D5=="D8":
                   
           screen.blit(imgD8,(610,60))
    if D5=="D9":
                    
           screen.blit(imgD9,(610,60))  
    if D5=="D10":
                    
           screen.blit(imgD10,(610,60)) 
    if D5=="DJ":
                    
           screen.blit(imgDJ,(610,60)) 
    if D5=="DQ":
                    
           screen.blit(imgDQ,(610,60)) 
    if D5=="DK":
                   
           screen.blit(imgDK,(610,60)) 
    if D5=="K1":
                   
           screen.blit(imgK1,(610,60))
    if D5=="K2":
                   
           screen.blit(imgK2,(610,60))  
    if D5=="K3":
                    
           screen.blit(imgK3,(610,60))   
    if D5=="K4":
                    
           screen.blit(imgK4,(610,60))  
    if D5=="K5":
                   
           screen.blit(imgK5,(610,60))  
    if D5=="K6":
                   
           screen.blit(imgK6,(610,60))  
    if D5=="K7":
                   
           screen.blit(imgK7,(610,60))  
    if D5=="K8":
                    
           screen.blit(imgK8,(610,60))  
    if D5=="K9":
                   
           screen.blit(imgK9,(610,60))  
    if D5=="K10":
                   
           screen.blit(imgK10,(610,60))  
    if D5=="KJ":
                   
           screen.blit(imgKJ,(610,60)) 
    if D5=="KQ":
                   
           screen.blit(imgKQ,(610,60))  
    if D5=="KK":
                    
           screen.blit(imgKK,(610,60)) 
                     
    if D5=="H1":
                   
           screen.blit(imgH1,(610,60)) 
    if D5=="H2":
                   
           screen.blit(imgH2,(610,60)) 
    if D5=="H3":
                   
           screen.blit(imgH3,(610,60)) 
    if D5=="H4":
                    
           screen.blit(imgH4,(610,60)) 
    if D5=="H5":
                    
           screen.blit(imgH5,(610,60)) 
    if D5=="H6":
                   
           screen.blit(imgH6,(610,60)) 
    if D5=="H7":
                   
           screen.blit(imgH7,(610,60)) 
    if D5=="H8":
                    
           screen.blit(imgH8,(610,60)) 
    if D5=="H9":
                    
           screen.blit(imgH9,(610,60)) 
    if D5=="H10":
                   
           screen.blit(imgH10,(610,60)) 
    if D5=="HJ":
                    
           screen.blit(imgHJ,(610,60)) 
    if D5=="HQ":
                    
           screen.blit(imgHQ,(610,60)) 
    if D5=="HK":
                    
           screen.blit(imgHK,(610,60))
    if D5=="S1":
                   
           screen.blit(imgS1,(610,60))  
    if D5=="S2":
                   
           screen.blit(imgS2,(610,60)) 
    if D5=="S3":
                   
           screen.blit(imgS3,(610,60)) 
    if D5=="S4":
                   
           screen.blit(imgS4,(610,60)) 
    if D5=="S5":
                    
           screen.blit(imgS5,(610,60))
    if D5=="S6":
                    
           screen.blit(imgS6,(610,60)) 
                    
    if D5=="S7":
                    
           screen.blit(imgS7,(610,60)) 
    if D5=="S8":
                    
           screen.blit(imgS8,(610,60)) 
    if D5=="S9":
                   
           screen.blit(imgS9,(610,60)) 
    if D5=="S10":
                   
           screen.blit(imgS10,(610,60))
    if D5=="SJ":
                   
           screen.blit(imgSJ,(610,60))  
    if D5=="SQ":
                    
           screen.blit(imgSQ,(610,60)) 
    if D5=="SK":
                  
           screen.blit(imgSK,(610,60)) 
def kardD4(D4,screen):

    if D4=="D1":
                    
           screen.blit(imgD1,(500,60))
    if D4=="D2":
                   
           screen.blit(imgD2,(500,60))
    if D4=="D3":
                    
           screen.blit(imgD3,(500,60))
    if D4=="D4":
                    
           screen.blit(imgD4,(500,60))
    if D4=="D5":
                    
           screen.blit(imgD5,(500,60))
    if D4=="D6":
                    
           screen.blit(imgD6,(500,60))
    if D4=="D7":
                   
           screen.blit(imgD7,(500,60))
    if D4=="D8":
                   
           screen.blit(imgD8,(500,60))
    if D4=="D9":
                    
           screen.blit(imgD9,(500,60))  
    if D4=="D10":
                    
           screen.blit(imgD10,(500,60)) 
    if D4=="DJ":
                    
           screen.blit(imgDJ,(500,60)) 
    if D4=="DQ":
                    
           screen.blit(imgDQ,(500,60)) 
    if D4=="DK":
                   
           screen.blit(imgDK,(500,60)) 
    if D4=="K1":
                   
           screen.blit(imgK1,(500,60))
    if D4=="K2":
                   
           screen.blit(imgK2,(500,60))  
    if D4=="K3":
                    
           screen.blit(imgK3,(500,60))   
    if D4=="K4":
                    
           screen.blit(imgK4,(500,60))  
    if D4=="K5":
                   
           screen.blit(imgK5,(500,60))  
    if D4=="K6":
                   
           screen.blit(imgK6,(500,60))  
    if D4=="K7":
                   
           screen.blit(imgK7,(500,60))  
    if D4=="K8":
                    
           screen.blit(imgK8,(500,60))  
    if D4=="K9":
                   
           screen.blit(imgK9,(500,60))  
    if D4=="K10":
                   
           screen.blit(imgK10,(500,60))  
    if D4=="KJ":
                   
           screen.blit(imgKJ,(500,60)) 
    if D4=="KQ":
                   
           screen.blit(imgKQ,(500,60))  
    if D4=="KK":
                    
           screen.blit(imgKK,(500,60)) 
                     
    if D4=="H1":
                   
           screen.blit(imgH1,(500,60)) 
    if D4=="H2":
                   
           screen.blit(imgH2,(500,60)) 
    if D4=="H3":
                   
           screen.blit(imgH3,(500,60)) 
    if D4=="H4":
                    
           screen.blit(imgH4,(500,60)) 
    if D4=="H5":
                    
           screen.blit(imgH5,(500,60)) 
    if D4=="H6":
                   
           screen.blit(imgH6,(500,60)) 
    if D4=="H7":
                   
           screen.blit(imgH7,(500,60)) 
    if D4=="H8":
                    
           screen.blit(imgH8,(500,60)) 
    if D4=="H9":
                    
           screen.blit(imgH9,(500,60)) 
    if D4=="H10":
                   
           screen.blit(imgH10,(500,60)) 
    if D4=="HJ":
                    
           screen.blit(imgHJ,(500,60)) 
    if D4=="HQ":
                    
           screen.blit(imgHQ,(500,60)) 
    if D4=="HK":
                    
           screen.blit(imgHK,(500,60))
    if D4=="S1":
                   
           screen.blit(imgS1,(500,60))  
    if D4=="S2":
                   
           screen.blit(imgS2,(500,60)) 
    if D4=="S3":
                   
           screen.blit(imgS3,(500,60)) 
    if D4=="S4":
                   
           screen.blit(imgS4,(500,60)) 
    if D4=="S5":
                    
           screen.blit(imgS5,(500,60))
    if D4=="S6":
                    
           screen.blit(imgS6,(500,60)) 
                    
    if D4=="S7":
                    
           screen.blit(imgS7,(500,60)) 
    if D4=="S8":
                    
           screen.blit(imgS8,(500,60)) 
    if D4=="S9":
                   
           screen.blit(imgS9,(500,60)) 
    if D4=="S10":
                   
           screen.blit(imgS10,(500,60))
    if D4=="SJ":
                   
           screen.blit(imgSJ,(500,60))  
    if D4=="SQ":
                    
           screen.blit(imgSQ,(500,60)) 
    if D4=="SK":
                  
           screen.blit(imgSK,(500,60)) 
def kardD1(D1,screen):

    if D1=="D1":
                    
           screen.blit(imgD1,(170,60))
    if D1=="D2":
                   
           screen.blit(imgD2,(170,60))
    if D1=="D3":
                    
           screen.blit(imgD3,(170,60))
    if D1=="D4":
                    
           screen.blit(imgD4,(170,60))
    if D1=="D5":
                    
           screen.blit(imgD5,(170,60))
    if D1=="D6":
                    
           screen.blit(imgD6,(170,60))
    if D1=="D7":
                   
           screen.blit(imgD7,(170,60))
    if D1=="D8":
                   
           screen.blit(imgD8,(170,60))
    if D1=="D9":
                    
           screen.blit(imgD9,(170,60))  
    if D1=="D10":
                    
           screen.blit(imgD10,(170,60)) 
    if D1=="DJ":
                    
           screen.blit(imgDJ,(170,60)) 
    if D1=="DQ":
                    
           screen.blit(imgDQ,(170,60)) 
    if D1=="DK":
                   
           screen.blit(imgDK,(170,60)) 
    if D1=="K1":
                   
           screen.blit(imgK1,(170,60))
    if D1=="K2":
                   
           screen.blit(imgK2,(170,60))  
    if D1=="K3":
                    
           screen.blit(imgK3,(170,60))   
    if D1=="K4":
                    
           screen.blit(imgK4,(170,60))  
    if D1=="K5":
                   
           screen.blit(imgK5,(170,60))  
    if D1=="K6":
                   
           screen.blit(imgK6,(170,60))  
    if D1=="K7":
                   
           screen.blit(imgK7,(170,60))  
    if D1=="K8":
                    
           screen.blit(imgK8,(170,60))  
    if D1=="K9":
                   
           screen.blit(imgK9,(170,60))  
    if D1=="K10":
                   
           screen.blit(imgK10,(170,60))  
    if D1=="KJ":
                   
           screen.blit(imgKJ,(170,60))  
    if D1=="KQ":
                   
           screen.blit(imgKQ,(170,60))  
    if D1=="KK":
                    
           screen.blit(imgKK,(170,60)) 
                     
    if D1=="H1":
                   
           screen.blit(imgH1,(170,60)) 
    if D1=="H2":
                   
           screen.blit(imgH2,(170,60)) 
    if D1=="H3":
                   
           screen.blit(imgH3,(170,60)) 
    if D1=="H4":
                    
           screen.blit(imgH4,(170,60)) 
    if D1=="H5":
                    
           screen.blit(imgH5,(170,60)) 
    if D1=="H6":
                   
           screen.blit(imgH6,(170,60)) 
    if D1=="H7":
                   
           screen.blit(imgH7,(170,60)) 
    if D1=="H8":
                    
           screen.blit(imgH8,(170,60)) 
    if D1=="H9":
                    
           screen.blit(imgH9,(170,60)) 
    if D1=="H10":
                   
           screen.blit(imgH10,(170,60)) 
    if D1=="HJ":
                    
           screen.blit(imgHJ,(170,60)) 
    if D1=="HQ":
                    
           screen.blit(imgHQ,(170,60)) 
    if D1=="HK":
                    
           screen.blit(imgHK,(170,60))
    if D1=="S1":
                   
           screen.blit(imgS1,(170,60))  
    if D1=="S2":
                   
           screen.blit(imgS2,(170,60)) 
    if D1=="S3":
                   
           screen.blit(imgS3,(170,60)) 
    if D1=="S4":
                   
           screen.blit(imgS4,(170,60)) 
    if D1=="S5":
                    
           screen.blit(imgS5,(170,60))
    if D1=="S6":
                    
           screen.blit(imgS6,(170,60)) 
                    
    if D1=="S7":
                    
           screen.blit(imgS7,(170,60)) 
    if D1=="S8":
                    
           screen.blit(imgS8,(170,60)) 
    if D1=="S9":
                   
           screen.blit(imgS9,(170,60)) 
    if D1=="S10":
                   
           screen.blit(imgS10,(170,60))
    if D1=="SJ":
                   
           screen.blit(imgSJ,(170,60))  
    if D1=="SQ":
                    
           screen.blit(imgSQ,(170,60)) 
    if D1=="SK":
                  
           screen.blit(imgSK,(170,60)) 
def kardD2(D2,screen):

    if D2=="D1":
            
       screen.blit(imgD1,(280,60))
            
    if D2=="D2":
            
       screen.blit(imgD2,(280,60))
            
    if D2=="D3":
            
       screen.blit(imgD3,(280,60))
            
    if D2=="D4":
            
       screen.blit(imgD4,(280,60))
            
    if D2=="D5":
            
       screen.blit(imgD5,(280,60))
            
    if D2=="D6":
          
       screen.blit(imgD6,(280,60))
            
    if D2=="D7":
           
       screen.blit(imgD7,(280,60))
            
    if D2=="D8":
            
       screen.blit(imgD8,(280,60))
            
    if D2=="D9":
          
       screen.blit(imgD9,(280,60))
              
    if D2=="D10":
            
       screen.blit(imgD10,(280,60))
             
    if D2=="DJ":
            
       screen.blit(imgDJ,(280,60))
             
    if D2=="DQ":
            
       screen.blit(imgDQ,(280,60))
            
    if D2=="DK":
          
       screen.blit(imgDK,(280,60))
             
    if D2=="K1":
           
       screen.blit(imgK1,(280,60))
            
    if D2=="K2":
           
       screen.blit(imgK2,(280,60))
              
    if D2=="K3":
            
       screen.blit(imgK3,(280,60))
               
    if D2=="K4":
            
       screen.blit(imgK4,(280,60))
              
    if D2=="K5":
           
       screen.blit(imgK5,(280,60))
              
    if D2=="K6":
            
       screen.blit(imgK6,(280,60))
              
    if D2=="K7":
          
       screen.blit(imgK7,(280,60))
              
    if D2=="K8":
           
       screen.blit(imgK8,(280,60))
              
    if D2=="K9":
            
       screen.blit(imgK9,(280,60))
              
    if D2=="K10":
           
       screen.blit(imgK10,(280,60))
             
    if D2=="KJ":
           
       screen.blit(imgKJ,(280,60))
              
    if D2=="KQ":
           
       screen.blit(imgKQ,(280,60))
             
    if D2=="KK":
           
       screen.blit(imgKK,(280,60))
             
                     
    if D2=="H1":
           
       screen.blit(imgH1,(280,60))
             
    if D2=="H2":
           
       screen.blit(imgH2,(280,60))
             
    if D2=="H3":
           
       screen.blit(imgH3,(280,60))
             
    if D2=="H4":
            
       screen.blit(imgH4,(280,60))
             
    if D2=="H5":
           
       screen.blit(imgH5,(280,60))
             
    if D2=="H6":
           
       screen.blit(imgH6,(280,60))
             
    if D2=="H7":
           
       screen.blit(imgH7,(280,60))
             
    if D2=="H8":
         
       screen.blit(imgH8,(280,60))
             
    if D2=="H9":
         
       screen.blit(imgH9,(280,60))
             
    if D2=="H10":
            
       screen.blit(imgH10,(280,60))
             
    if D2=="HJ":
            
       screen.blit(imgHJ,(280,60))
             
    if D2=="HQ":
            
       screen.blit(imgHQ,(280,60))
             
    if D2=="HK":
            
       screen.blit(imgHK,(280,60))
            
    if D2=="S1":
            
       screen.blit(imgS1,(280,60))
             
    if D2=="S2":
           
       screen.blit(imgS2,(280,60))
             
    if D2=="S3":
           
       screen.blit(imgS3,(280,60))
            
    if D2=="S4":
           
       screen.blit(imgS4,(280,60))
             
    if D2=="S5":
           
       screen.blit(imgS5,(280,60))
            
    if D2=="S6":
           
       screen.blit(imgS6,(280,60))
             
                    
    if D2=="S7":
           
       screen.blit(imgS7,(280,60))
             
    if D2=="S8":
           
       screen.blit(imgS8,(280,60))
             
    if D2=="S9":
           
       screen.blit(imgS9,(280,60))
             
    if D2=="S10":
            
       screen.blit(imgS10,(280,60))
            
    if D2=="SJ":
            
       screen.blit(imgSJ,(280,60)) 
             
    if D2=="SQ":
           
       screen.blit(imgSQ,(280,60)) 
            
    if D2=="SK":
           
       screen.blit(imgSK,(280,60)) 
def kardP1(P1,screen):

    if P1=="D1":
                   
        screen.blit(imgD1,(170,280))
    if P1=="D2":
                    
        screen.blit(imgD2,(170,280))
    if P1=="D3":
                    
        screen.blit(imgD3,(170,280))
    if P1=="D4":
                   
        screen.blit(imgD4,(170,280))
    if P1=="D5":
                   
        screen.blit(imgD5,(170,280))
    if P1=="D6":
                   
        screen.blit(imgD6,(170,280))
    if P1=="D7":
                   
        screen.blit(imgD7,(170,280))
    if P1=="D8":
                    
        screen.blit(imgD8,(170,280))
    if P1=="D9":
                    
        screen.blit(imgD9,(170,280))  
    if P1=="D10":
                   
        screen.blit(imgD10,(170,280)) 
    if P1=="DJ":
                   
        screen.blit(imgDJ,(170,280)) 
    if P1=="DQ":
                   
        screen.blit(imgDQ,(170,280)) 
    if P1=="DK":
                    
        screen.blit(imgDK,(170,280)) 
    if P1=="K1":
                   
        screen.blit(imgK1,(170,280))
    if P1=="K2":
                    
        screen.blit(imgK2,(170,280))  
    if P1=="K3":
                   
        screen.blit(imgK3,(170,280))   
    if P1=="K4":
                    
        screen.blit(imgK4,(170,280))  
    if P1=="K5":
                    
        screen.blit(imgK5,(170,280))  
    if P1=="K6":
                   
        screen.blit(imgK6,(170,280))  
    if P1=="K7":
                    
        screen.blit(imgK7,(170,280))  
    if P1=="K8":
                   
        screen.blit(imgK8,(170,280))  
    if P1=="K9":
                   
        screen.blit(imgK9,(170,280))  
    if P1=="K10":
                   
        screen.blit(imgK10,(170,280))  
    if P1=="KJ":
                    
        screen.blit(imgKJ,(170,280))  
    if P1=="KQ":
         screen.blit(imgKQ,(170,280)) 
    if P1=="KK" :       
        screen.blit(imgKK,(170,280)) 
                     
    if P1=="H1":
                    
        screen.blit(imgH1,(170,280)) 
    if P1=="H2":
                  
        screen.blit(imgH2,(170,280)) 
    if P1=="H3":
                   
        screen.blit(imgH3,(170,280)) 
    if P1=="H4":
                   
        screen.blit(imgH4,(170,280)) 
    if P1=="H5":
                    
        screen.blit(imgH5,(170,280)) 
    if P1=="H6":
                   
        screen.blit(imgH6,(170,280)) 
    if P1=="H7":
                    
        screen.blit(imgH7,(170,280)) 
    if P1=="H8":
                    
        screen.blit(imgH8,(170,280)) 
    if P1=="H9":
                    
        screen.blit(imgH9,(170,280)) 
    if P1=="H10":
                    
        screen.blit(imgH10,(170,280)) 
    if P1=="HJ":
                   
        screen.blit(imgHJ,(170,280)) 
    if P1=="HQ":
                    
        screen.blit(imgHQ,(170,280)) 
    if P1=="HK":
                    
        screen.blit(imgHK,(170,280))
    if P1=="S1":
                    
        screen.blit(imgS1,(170,280))  
    if P1=="S2":
                   
        screen.blit(imgS2,(170,280)) 
    if P1=="S3":
                   
        screen.blit(imgS3,(170,280)) 
    if P1=="S4":
                    
        screen.blit(imgS4,(170,280)) 
    if P1=="S5":
                    
        screen.blit(imgS5,(170,280))
    if P1=="S6":
                   
        screen.blit(imgS6,(170,280)) 
                    
    if P1=="S7":
                   
        screen.blit(imgS7,(170,280)) 
    if P1=="S8":
                   
        screen.blit(imgS8,(170,280)) 
    if P1=="S9":
                   
        screen.blit(imgS9,(170,280)) 
    if P1=="S10":
                    
        screen.blit(imgS10,(170,280))
    if P1=="SJ":
                   
        screen.blit(imgSJ,(170,280))  
    if P1=="SQ":
                  
        screen.blit(imgSQ,(170,280)) 
    if P1=="SK":
                    
        screen.blit(imgSK,(170,280)) 
def kardP2(P2,screen):   
    if P2=="D1":
        screen.blit(imgD1,(280,280))
    if P2=="D2":
        screen.blit(imgD2,(280,280))
    if P2=="D3":
        screen.blit(imgD3,(280,280))
    if P2=="D4":
        screen.blit(imgD4,(280,280))
    if P2=="D5":
        screen.blit(imgD5,(280,280))
    if P2=="D6":
        screen.blit(imgD6,(280,280))
    if P2=="D7":
        screen.blit(imgD7,(280,280))
    if P2=="D8":
        screen.blit(imgD8,(280,280))
    if P2=="D9":
        screen.blit(imgD9,(280,280))
    if P2=="D10":
        screen.blit(imgD10,(280,280))
    if P2=="DJ":
        screen.blit(imgDJ,(280,280))
    if P2=="DQ":
        screen.blit(imgDQ,(280,280))
    if P2=="DK":
        screen.blit(imgDK,(280,280))
    if P2=="S1":
        screen.blit(imgS1,(280,280))

    if P2=="S2":
        screen.blit(imgS2,(280,280))
    if P2=="S3":
        screen.blit(imgS3,(280,280))
    if P2=="S4":
        screen.blit(imgS4,(280,280))
    if P2=="S5":
        screen.blit(imgS5,(280,280))
    if P2=="S6":
        screen.blit(imgS6,(280,280))

                    
    if P2=="S7":
        screen.blit(imgS7,(280,280))
    if P2=="S8":
        screen.blit(imgS8,(280,280))

    if P2=="S9":
        screen.blit(imgS9,(280,280))
    if P2=="S10":
        screen.blit(imgS10,(280,280))

    if P2=="SJ":
        screen.blit(imgSJ,(280,280))
    if P2=="SQ":
        screen.blit(imgSQ,(280,280))
    if P2=="SK":
        screen.blit(imgSK,(280,280))
    if P2=="H1":
        screen.blit(imgH1,(280,280))
    if P2=="H2":
        screen.blit(imgH2,(280,280))
    if P2=="H3":
        screen.blit(imgH3,(280,280))

    if P2=="H4":
        screen.blit(imgH4,(280,280))
    if P2=="H5":
        screen.blit(imgH5,(280,280))
    if P2=="H6":
        screen.blit(imgH6,(280,280))
    if P2=="H7":
        screen.blit(imgH7,(280,280))
    if P2=="H8":
        screen.blit(imgH8,(280,280))

    if P2=="H9":
        screen.blit(imgH9,(280,280))
    if P2=="H10":
        screen.blit(imgH10,(280,280))
    if P2=="HJ":
        screen.blit(imgHJ,(280,280))
    if P2=="HQ":
        screen.blit(imgHQ,(280,280))
    if P2=="HK":
        screen.blit(imgHK,(280,280))
    if P2=="K1":
        screen.blit(imgK1,(280,280))
    if P2=="K2":
        screen.blit(imgK2,(280,280))
    if P2=="K3":
        screen.blit(imgK3,(280,280))

    if P2=="K4":
        screen.blit(imgK5,(280,280))
    if P2=="K5":
        screen.blit(imgK5,(280,280))
    if P2=="K6":
        screen.blit(imgK6,(280,280))
    if P2=="K7":
        screen.blit(imgK7,(280,280))
    if P2=="K8":
        screen.blit(imgK8,(280,280))
    if P2=="K9":
        screen.blit(imgK9,(280,280))
    if P2=="K10":
        screen.blit(imgK10,(280,280))
    if P2=="KJ":
        screen.blit(imgKJ,(280,280))
    if P2=="KQ":
        screen.blit(imgKQ,(280,280))
    if P2=="KK":
        screen.blit(imgKK,(280,280))
def kardD3(D3,screen):



    if D3=="D1":
                    
           screen.blit(imgD1,(390,60))
    if D3=="D2":
                   
           screen.blit(imgD2,(390,60))
    if D3=="D3":
                    
           screen.blit(imgD3,(390,60))
    if D3=="D4":
                    
           screen.blit(imgD4,(390,60))
    if D3=="D5":
                    
           screen.blit(imgD5,(390,60))
    if D3=="D6":
                    
           screen.blit(imgD6,(390,60))
    if D3=="D7":
                   
           screen.blit(imgD7,(390,60))
    if D3=="D8":
                   
           screen.blit(imgD8,(390,60))
    if D3=="D9":
                    
           screen.blit(imgD9,(390,60))  
    if D3=="D10":
                    
           screen.blit(imgD10,(390,60)) 
    if D3=="DJ":
                    
           screen.blit(imgDJ,(390,60)) 
    if D3=="DQ":
                    
           screen.blit(imgDQ,(390,60)) 
    if D3=="DK":
                   
           screen.blit(imgDK,(390,60)) 
    if D3=="K1":
                   
           screen.blit(imgK1,(390,60))
    if D3=="K2":
                   
           screen.blit(imgK2,(390,60))  
    if D3=="K3":
                    
           screen.blit(imgK3,(390,60))   
    if D3=="K4":
                    
           screen.blit(imgK4,(390,60))  
    if D3=="K5":
                   
           screen.blit(imgK5,(390,60))  
    if D3=="K6":
                   
           screen.blit(imgK6,(390,60))  
    if D3=="K7":
                   
           screen.blit(imgK7,(390,60))  
    if D3=="K8":
                    
           screen.blit(imgK8,(390,60))  
    if D3=="K9":
                   
           screen.blit(imgK9,(390,60))  
    if D3=="K10":
                   
           screen.blit(imgK10,(390,60))  
    if D3=="KJ":
                   
           screen.blit(imgKJ,(390,60))  
    if D3=="KQ":
                   
           screen.blit(imgKQ,(390,60))  
    if D3=="KK":
                    
           screen.blit(imgKK,(390,60)) 
                     
    if D3=="H1":
                   
           screen.blit(imgH1,(390,60)) 
    if D3=="H2":
                   
           screen.blit(imgH2,(390,60)) 
    if D3=="H3":
                   
           screen.blit(imgH3,(390,60)) 
    if D3=="H4":
                    
           screen.blit(imgH4,(390,60)) 
    if D3=="H5":
                    
           screen.blit(imgH5,(390,60)) 
    if D3=="H6":
                   
           screen.blit(imgH6,(390,60)) 
    if D3=="H7":
                   
           screen.blit(imgH7,(390,60)) 
    if D3=="H8":
                    
           screen.blit(imgH8,(390,60)) 
    if D3=="H9":
                    
           screen.blit(imgH9,(390,60)) 
    if D3=="H10":
                   
           screen.blit(imgH10,(390,60)) 
    if D3=="HJ":
                    
           screen.blit(imgHJ,(390,60)) 
    if D3=="HQ":
                    
           screen.blit(imgHQ,(390,60)) 
    if D3=="HK":
                    
           screen.blit(imgHK,(390,60))
    if D3=="S1":
                   
           screen.blit(imgS1,(390,60))  
    if D3=="S2":
                   
           screen.blit(imgS2,(390,60)) 
    if D3=="S3":
                   
           screen.blit(imgS3,(390,60)) 
    if D3=="S4":
                   
           screen.blit(imgS4,(390,60)) 
    if D3=="S5":
                    
           screen.blit(imgS5,(390,60))
    if D3=="S6":
                    
           screen.blit(imgS6,(390,60)) 
                    
    if D3=="S7":
                    
           screen.blit(imgS7,(390,60)) 
    if D3=="S8":
                    
           screen.blit(imgS8,(390,60)) 
    if D3=="S9":
                   
           screen.blit(imgS9,(390,60)) 
    if D3=="S10":
                   
           screen.blit(imgS10,(390,60))
    if D3=="SJ":
                   
           screen.blit(imgSJ,(390,60))  
    if D3=="SQ":
                    
           screen.blit(imgSQ,(390,60)) 
    if D3=="SK":
                  
           screen.blit(imgSK,(390,60)) 
def Game(screen,money):   
    tranp=["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","K1","K2","K3","K4","K5","K6","K7","K8","K9","K10","KJ","KQ","KK","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK"]
    global round
    round += 1
    kakemoney=10
    run2=True
    kard=random.sample(tranp,10)
    Dcount=0
    Pcount=0
    Donearu=False
    D1=kard[0]
    D2=kard[1]
    P1=kard[2]
    P2=kard[3]
    P3=kard[4]
    P4=kard[5]
    P5=kard[6]
    D3=kard[7]
    D4=kard[8]
    D5=kard[9]
    Ponearu=False
    font3 = pygame.font.Font(None, 200)  
    X=False
    font2 = pygame.font.Font(None, 40)  
    
    roundsuu=font3.render("ROUND"+str(round),True,(255,255,255))
    
    
    setumei=font2.render("Press space to decide the bet",True,(255,255,255))
    setumei2=font2.render("Left down Right up",True,(255,255,255))
    
    Dera=False
    run=True
    A=False
    D=False
    B=False
    C=False
    one=False
    two=False
    Donesita=False
    onesita=False
    three=False
    text(screen,money,kakemoney)
    screen.blit(roundsuu,[100,120]) 
    screen.blit(setumei, [300, 450])
    screen.blit(setumei2, [300, 500])
    pygame.display.update()  
    if(round==6):
        run=False
        round=0
        end(screen,money)
    
    

    while run:
        kane=font2.render("Money   "+str(money), True, (255,255,255))
        kake=font2.render("Bet   "+str(kakemoney), True, (255,255,255))
       
       
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:  # キーを押したとき

               if event.key==K_q:
                   pygame.display.update()
               if event.key==K_n:
                   round=0
                   run=False
                   main()

               if event.key==K_ESCAPE:
                 webbrowser.open("http://localhost:5000/")
                 pygame.quit()
                 sys.exit()
               if event.key== K_LEFT and 10<kakemoney and A==False :
                   kakemoney-=10 
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   screen.blit(setumei, [300, 450])
                   screen.blit(setumei2, [300, 500])
                   
                   
                   pygame.display.update() 
                  
               if event.key== K_RIGHT and money>kakemoney and A==False :
                    kakemoney+=10 
                    screen.fill((0,100,0))
                    text(screen,money,kakemoney)
                    screen.blit(setumei, [300, 450])
                    screen.blit(setumei2, [300, 500])

                    pygame.display.update()
               
                    
               if event.key == K_SPACE and A==False:
                   if(D1=="D1" or D1=="H1" or D1=="K1" or D1=="S1"):
                    Dcount+=11
                    onearu=True
                   if(D1=="D2" or D1=="H2" or D1=="K2" or D1=="S2"):
                    Dcount+=2
                   if(D1=="D3" or D1=="H3" or D1=="K3" or D1=="S3"):
                    Dcount+=3
                   if(D1=="D4" or D1=="H4" or D1=="K4" or D1=="S4"):
                     Dcount+=4        
                   if(D1=="D5" or D1=="H5" or D1=="K5" or D1=="S5"):
                    Dcount+=5 
                   if(D1=="D6" or D1=="H6" or D1=="K6" or D1=="S6"):
                    Dcount+=6  
                   if(D1=="D7" or D1=="H7" or D1=="K7" or D1=="S7"):
                     Dcount+=7             
                   if(D1=="D8" or D1=="H8" or D1=="K8" or D1=="S8"):
                    Dcount+=8   
                   if(D1=="D9" or D1=="H9" or D1=="K9" or D1=="S9"):
                    Dcount+=9             
                   if(D1=="D10" or D1=="H10" or D1=="K10" or D1=="S10" or D1=="DJ" or D1=="HJ" or D1=="KJ" or D1=="SJ" or D1=="DQ" or D1=="HQ" or D1=="KQ" or D1=="SQ" or D1=="DK" or D1=="HK" or D1=="KK" or D1=="SK") :
                    Dcount+=10  
                   money = money-kakemoney
                   A=True
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   text2(screen,Pcount,Dcount)
                   if Dera==False:
                   
                    screen.blit(imgback,(280,60))  

                   pygame.display.update() 
                   time.sleep(1)
       
                   if(P1=="D1" or P1=="H1" or P1=="K1" or P1=="S1" ):
                    Pcount+=11
                    Ponearu=True
                   if(P2=="D1" or P2=="H1" or P2=="K1" or P2=="S1"):
                          Pcount+=11
                          Ponearu=True
                   if(P1=="D2" or P1=="H2" or P1=="K2" or P1=="S2"):
                    Pcount+=2   
                   if(P2=="D2" or P2=="H2" or P2=="K2" or P2=="S2"):
                          Pcount+=2 
                   if(P1=="D3" or P1=="H3" or P1=="K3" or P1=="S3"):

                    Pcount+=3    
                   if(P2=="D3" or P2=="H3" or P2=="K3" or P2=="S3"):
                          Pcount+=3
                   if(P1=="D4" or P1=="H4" or P1=="K4" or P1=="S4"):
                    Pcount+=4    
                   if(P2=="D4" or P2=="H4" or P2=="K4" or P2=="S4"):
                          Pcount+=4
                   if(P1=="D5" or P1=="H5" or P1=="K5" or P1=="S5"):
                     Pcount+=5    
                   if(P2=="D5" or P2=="H5" or P2=="K5" or P2=="S5"):
                          Pcount+=5
                   if(P1=="D6" or P1=="H6" or P1=="K6" or P1=="S6"):
                    Pcount+=6    
                   if(P2=="D6" or P2=="H6" or P2=="K6" or P2=="S6"):
                          Pcount+=6
                   if(P1=="D7" or P1=="H7" or P1=="K7" or P1=="S7"):
                    Pcount+=7     
                   if(P2=="D7" or P2=="H7" or P2=="K7" or P2=="S7"):
                          Pcount+=7   
                   if(P1=="D8" or P1=="H8" or P1=="K8" or P1=="S8"):
                     Pcount+=8        
                   if(P2=="D8" or P2=="H8" or P2=="K8" or P2=="S8"):
                          Pcount+=8
                   if(P1=="D9" or P1=="H9" or P1=="K9" or P1=="S9"):
                    Pcount+=9  
                   if(P2=="D9" or P2=="H9" or P2=="K9" or P2=="S9"):
                          Pcount+=9      
                   if(P1=="D10" or P1=="H10" or P1=="K10" or P1=="S10"or P1=="DJ" or P1=="HJ" or P1=="KJ" or P1=="SJ"  or P1=="DQ" or P1=="HQ" or P1=="KQ" or P1=="SQ"  or P1=="DK" or P1=="HK" or P1=="KK" or P1=="SK" ):
                    Pcount+=10
                   if(P2=="D10" or P2=="H10" or P2=="K10" or P2=="S10" or P2=="DJ" or P2=="HJ" or P2=="KJ" or P2=="SJ" or P2=="DQ" or P2=="HQ" or P2=="KQ" or P2=="SQ" or P2=="KK" or P2=="HK" or P2=="DK" or P2=="SK"):
                          Pcount+=10
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   screen.blit(imgback,(280,60)) 
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   text2(screen,Pcount,Dcount)     
                  
                   pygame.display.update()
                   if(Pcount==21):
                       Pblack(screen,money,kakemoney)
                   if Pcount==22:
                       Pcount=Pcount-10
                       screen.fill((0,100,0))
                       text(screen,money,kakemoney)
                       kardD1(D1,screen)
                       screen.blit(imgback,(280,60)) 
                       kardP1(P1,screen)
                       kardP2(P2,screen)
                       text2(screen,Pcount,Dcount)
                   time.sleep(1)
                   HIT=font2.render("H:HIT",True,(255,255,255))
                   screen.blit(HIT,[230,480])
                   STAND=font2.render("S:STAND",True,(255,255,255))
                   screen.blit(STAND,[600,480])
                   DOWN=font2.render("D:DOUBLE DOWN",True,(255,255,255))
                   screen.blit(DOWN,[330,480])
                   D=True
                   pygame.display.update()
               if event.key==K_s and D==True:
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   STAND=font2.render("S:STAND",True,(255,255,255))
                   screen.blit(STAND,[600,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   pygame.display.update()
                   time.sleep(1)
                   Dera=True
                 
               if event.key==K_d and D==True:
                   one=True
                   if(P3=="D1" or P3=="H1" or P3=="K1" or P3=="S1"):
                     Pcount+=11
                     Ponearu=True
                   if(P3=="D2" or P3=="H2" or P3=="K2" or P3=="S2"):
                     Pcount+=2
                   if(P3=="D3" or P3=="H3" or P3=="K3" or P3=="S3"):
                     Pcount+=3
                   if(P3=="D4" or P3=="H4" or P3=="K4" or P3=="S4"):
                     Pcount+=4        
                   if(P3=="D5" or P3=="H5" or P3=="K5" or P3=="S5"):
                     Pcount+=5 
                   if(P3=="D6" or P3=="H6" or P3=="K6" or P3=="S6"):
                     Pcount+=6  
                   if(P3=="D7" or P3=="H7" or P3=="K7" or P3=="S7"):
                     Pcount+=7             
                   if(P3=="D8" or P3=="H8" or P3=="K8" or P3=="S8"):
                     Pcount+=8   
                   if(P3=="D9" or P3=="H9" or P3=="K9" or P3=="S9"):
                     Pcount+=9             
                   if(P3=="D10" or P3=="H10" or P3=="K10" or P3=="S10" or P3=="DJ" or P3=="HJ" or P3=="KJ" or P3=="SJ" or P3=="DQ" or P3=="HQ" or P3=="KQ" or P3=="SQ" or P3=="DK" or P3=="HK" or P3=="KK" or P3=="SK") :
                     Pcount+=10  
                   money=money - kakemoney
                   kakemoney=kakemoney*2
                   if(Pcount>21 and Ponearu==True and onesita==False ):
                       Pcount=Pcount-10
                       onesita=True
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   DOWN=font2.render("D:DOUBLE DOWN",True,(255,255,255))
                   screen.blit(DOWN,[330,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP3(P3,screen)
                   pygame.display.update()
                   time.sleep(1)
                   
                   if(Pcount>21 ):
                       
                       Pbarst(screen,money)
                       pygame.display.update()
                   if(Pcount==21):
                
                       Pblack(screen,money,kakemoney)
                       pygame.display.update()
                   Dera=True
                   pygame.display.update()
               if event.key==K_s and C==True:
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   STAND=font2.render("S:STAND",True,(255,255,255))
                   screen.blit(STAND,[600,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP4(P4,screen)
                   kardP3(P3,screen)
                   pygame.display.update()
                   time.sleep(1)
                   Dera=True
               if event.key==K_h and C==True:
                   C=False
                   three=True
                   if(P5=="D1" or P5=="H1" or P5=="K1" or P5=="S1"):
                     Pcount+=11
                     Ponearu=True
                   if(P5=="D2" or P5=="H2" or P5=="K2" or P5=="S2"):
                     Pcount+=2
                   if(P5=="D3" or P5=="H3" or P5=="K3" or P5=="S3"):
                     Pcount+=3
                   if(P5=="D4" or P5=="H4" or P5=="K4" or P5=="S4"):
                     Pcount+=4        
                   if(P5=="D5" or P5=="H5" or P5=="K5" or P5=="S5"):
                     Pcount+=5 
                   if(P5=="D6" or P5=="H6" or P5=="K6" or P5=="S6"):
                     Pcount+=6  
                   if(P5=="D7" or P5=="H7" or P5=="K7" or P5=="S7"):
                     Pcount+=7             
                   if(P5=="D8" or P5=="H8" or P5=="K8" or P5=="S8"):
                     Pcount+=8   
                   if(P5=="D9" or P5=="H9" or P5=="K9" or P5=="S9"):
                     Pcount+=9             
                   if(P5=="D10" or P5=="H10" or P5=="K10" or P5=="S10" or P5=="DJ" or P5=="HJ" or P5=="KJ" or P5=="SJ" or P5=="DQ" or P5=="HQ" or P5=="KQ" or P5=="SQ" or P5=="DK" or P5=="HK" or P5=="KK" or P5=="SK") :
                     Pcount+=10  
                   if(Pcount>22 and Ponearu==True and onesita==False ):
                       Pcount=Pcount-10
                       onesita=True
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   HIT=font2.render("H:HIT",True,(255,255,255))
                   screen.blit(HIT,[230,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP3(P3,screen)
                   kardP4(P4,screen)
                   kardP5(P5,screen)
                   pygame.display.update()
                   time.sleep(1)
                  
                   if(Pcount>21 ):
                       Pbarst(screen,money)
                   if(Pcount==21):
                       Pblack(screen,money,kakemoney)
                   if Pcount<21:
                       Dera=True
                   pygame.display.update()
               if event.key==K_h and B==True:
                   B=False
                   two=True
                   if(P4=="D1" or P4=="H1" or P4=="K1" or P4=="S1"):
                     Pcount+=11
                     Ponearu=True
                   if(P4=="D2" or P4=="H2" or P4=="K2" or P4=="S2"):
                     Pcount+=2
                   if(P4=="D3" or P4=="H3" or P4=="K3" or P4=="S3"):
                     Pcount+=3
                   if(P4=="D4" or P4=="H4" or P4=="K4" or P4=="S4"):
                     Pcount+=4        
                   if(P4=="D5" or P4=="H5" or P4=="K5" or P4=="S5"):
                     Pcount+=5 
                   if(P4=="D6" or P4=="H6" or P4=="K6" or P4=="S6"):
                     Pcount+=6  
                   if(P4=="D7" or P4=="H7" or P4=="K7" or P4=="S7"):
                     Pcount+=7             
                   if(P4=="D8" or P4=="H8" or P4=="K8" or P4=="S8"):
                     Pcount+=8   
                   if(P4=="D9" or P4=="H9" or P4=="K9" or P4=="S9"):
                     Pcount+=9             
                   if(P4=="D10" or P4=="H10" or P4=="K10" or P4=="S10" or P4=="DJ" or P4=="HJ" or P4=="KJ" or P4=="SJ" or P4=="DQ" or P4=="HQ" or P4=="KQ" or P4=="SQ" or P4=="DK" or P4=="HK" or P4=="KK" or P4=="SK") :
                     Pcount+=10  
                   if(Pcount>22 and Ponearu==True and onesita==False ):
                       Pcount=Pcount-10
                       onesita=True
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   HIT=font2.render("H:HIT",True,(255,255,255))
                   screen.blit(HIT,[230,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP3(P3,screen)
                   kardP4(P4,screen)
                   pygame.display.update()
                   time.sleep(1)
                  
                   if(Pcount>21 ):
                       Pbarst(screen,money)
                   if(Pcount==21):
                       Pblack(screen,money,kakemoney)
                   if Pcount<21:
                       screen.fill((0,100,0))
                       text(screen,money,kakemoney)
                       kardD1(D1,screen)
                       screen.blit(STAND,[600,480])
                       screen.blit(HIT,[230,480])
                       screen.blit(imgback,(280,60)) 
                       text2(screen,Pcount,Dcount)
                       kardP1(P1,screen)
                       kardP2(P2,screen)
                       kardP3(P3,screen)
                       kardP4(P4,screen)
                       pygame.display.update()
                       C=True
                   pygame.display.update()
               if event.key==K_s and B==True:
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   STAND=font2.render("S:STAND",True,(255,255,255))
                   screen.blit(STAND,[600,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP3(P3,screen)
                   pygame.display.update()
                   time.sleep(1)
                   Dera=True
               if event.key==K_h and D==True:
                   D=False
                   one=True
                   if(P3=="D1" or P3=="H1" or P3=="K1" or P3=="S1"):
                     Pcount+=11
                     Ponearu=True
                   if(P3=="D2" or P3=="H2" or P3=="K2" or P3=="S2"):
                     Pcount+=2
                   if(P3=="D3" or P3=="H3" or P3=="K3" or P3=="S3"):
                     Pcount+=3
                   if(P3=="D4" or P3=="H4" or P3=="K4" or P3=="S4"):
                     Pcount+=4        
                   if(P3=="D5" or P3=="H5" or P3=="K5" or P3=="S5"):
                     Pcount+=5 
                   if(P3=="D6" or P3=="H6" or P3=="K6" or P3=="S6"):
                     Pcount+=6  
                   if(P3=="D7" or P3=="H7" or P3=="K7" or P3=="S7"):
                     Pcount+=7             
                   if(P3=="D8" or P3=="H8" or P3=="K8" or P3=="S8"):
                     Pcount+=8   
                   if(P3=="D9" or P3=="H9" or P3=="K9" or P3=="S9"):
                     Pcount+=9             
                   if(P3=="D10" or P3=="H10" or P3=="K10" or P3=="S10" or P3=="DJ" or P3=="HJ" or P3=="KJ" or P3=="SJ" or P3=="DQ" or P3=="HQ" or P3=="KQ" or P3=="SQ" or P3=="DK" or P3=="HK" or P3=="KK" or P3=="SK") :
                     Pcount+=10  
                   if(Pcount>22 and Ponearu==True and onesita==False ):
                       Pcount=Pcount-10
                       onesita=True
                   screen.fill((0,100,0))
                   text(screen,money,kakemoney)
                   kardD1(D1,screen)
                   HIT=font2.render("H:HIT",True,(255,255,255))
                   screen.blit(HIT,[230,480])
                   screen.blit(imgback,(280,60)) 
                   text2(screen,Pcount,Dcount)
                   kardP1(P1,screen)
                   kardP2(P2,screen)
                   kardP3(P3,screen)
                   
                   pygame.display.update()
                   time.sleep(1)
                  
                   if(Pcount>21 ):
                       Pbarst(screen,money)
                   if(Pcount==21):
                       Pblack(screen,money,kakemoney)
                   if Pcount<21:
                       
                       screen.fill((0,100,0))
                       text(screen,money,kakemoney)
                       kardD1(D1,screen)
                       screen.blit(STAND,[600,480])
                       screen.blit(HIT,[230,480])
                       screen.blit(imgback,(280,60)) 
                       text2(screen,Pcount,Dcount)
                       kardP1(P1,screen)
                       kardP2(P2,screen)
                       kardP3(P3,screen)
                       pygame.display.update()
                       B=True
                       
                   
            
               
            if event.type == QUIT:
                webbrowser.open("http://localhost:5000/")  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
        if Dera ==True and X==False:
          X=True
          if(D2=="D1" or D2=="H1" or D2=="K1" or D2=="S1"):
                    Dcount+=11
                    Donearu=True
          if(D2=="D2" or D2=="H2" or D2=="K2" or D2=="S2"):
                    Dcount+=2
          if(D2=="D3" or D2=="H3" or D2=="K3" or D2=="S3"):
                    Dcount+=3
          if(D2=="D4" or D2=="H4" or D2=="K4" or D2=="S4"):
                     Dcount+=4        
          if(D2=="D5" or D2=="H5" or D2=="K5" or D2=="S5"):
                    Dcount+=5 
          if(D2=="D6" or D2=="H6" or D2=="K6" or D2=="S6"):
                    Dcount+=6  
          if(D2=="D7" or D2=="H7" or D2=="K7" or D2=="S7"):
                     Dcount+=7             
          if(D2=="D8" or D2=="H8" or D2=="K8" or D2=="S8"):
                    Dcount+=8   
          if(D2=="D9" or D2=="H9" or D2=="K9" or D2=="S9"):
                    Dcount+=9             
          if(D2=="D10" or D2=="H10" or D2=="K10" or D2=="S10" or D2=="DJ" or D2=="HJ" or D2=="KJ" or D2=="SJ" or D2=="DQ" or D2=="HQ" or D2=="KQ" or D2=="SQ" or D2=="DK" or D2=="HK" or D2=="KK" or D2=="SK") :
                    Dcount+=10  
          screen.fill((0,100,0))
          if Dcount==22:
              Dcount=Dcount-10
              Donesita=True
          text(screen,money,kakemoney)
          kardD2(D2,screen)
          kardD1(D1,screen)
          kardP1(P1,screen)
          kardP2(P2,screen)
          text2(screen,Pcount,Dcount)
          if one==True:
              kardP3(P3,screen)
          if two==True:
              kardP4(P4,screen)
          if three==True:
              kardP5(P5,screen)
          
          pygame.display.update()
          time.sleep(1)
          if Dcount >21:
              Pwin(screen,money,kakemoney)
          if Dcount==Pcount and Pcount>16:
              drow(screen,money,kakemoney)
          if Dcount>Pcount:
                  Ploose(screen,money)
          if Dcount>16:
              if Dcount<Pcount:
                  Pwin(screen,money,kakemoney)
          else:#17より小さい
             if(D3=="D1" or D3=="H1" or D3=="K1" or D3=="S1"):
                    Dcount+=11
                    Donearu=True
             if(D3=="D2" or D3=="H2" or D3=="K2" or D3=="S2"):
                    Dcount+=2
             if(D3=="D3" or D3=="H3" or D3=="K3" or D3=="S3"):
                    Dcount+=3
             if(D3=="D4" or D3=="H4" or D3=="K4" or D3=="S4"):
                     Dcount+=4        
             if(D3=="D5" or D3=="H5" or D3=="K5" or D3=="S5"):
                    Dcount+=5 
             if(D3=="D6" or D3=="H6" or D3=="K6" or D3=="S6"):
                    Dcount+=6  
             if(D3=="D7" or D3=="H7" or D3=="K7" or D3=="S7"):
                     Dcount+=7             
             if(D3=="D8" or D3=="H8" or D3=="K8" or D3=="S8"):
                    Dcount+=8   
             if(D3=="D9" or D3=="H9" or D3=="K9" or D3=="S9"):
                    Dcount+=9             
             if(D3=="D10" or D3=="H10" or D3=="K10" or D3=="S10" or D3=="DJ" or D3=="HJ" or D3=="KJ" or D3=="SJ" or D3=="DQ" or D3=="HQ" or D3=="KQ" or D3=="SQ" or D3=="DK" or D3=="HK" or D3=="KK" or D3=="SK") :
                    Dcount+=10  
             screen.fill((0,100,0))
             if Dcount>21 and Donearu==True and Donesita==False:
                 Dcount=Dcount-10
                 Donesita=True
             text(screen,money,kakemoney)
             kardD2(D2,screen)
             kardD1(D1,screen)
             kardD3(D3,screen)
             kardP1(P1,screen)
             kardP2(P2,screen)
             text2(screen,Pcount,Dcount)
             if one==True:
              kardP3(P3,screen)
             if two==True:
              kardP4(P4,screen)
             if three==True:
               kardP5(P5,screen)
             
              
              
             pygame.display.update()
             time.sleep(1)
             if Dcount>21:
                 Pwin(screen,money,kakemoney)
             if Dcount==Pcount and Pcount>16:
                 drow(screen,money,kakemoney)
             if Dcount>16:
              if Dcount<Pcount:
                  Pwin(screen,money,kakemoney)
              else:
                  Ploose(screen,money)
             
             else:
                 if(D4=="D1" or D4=="H1" or D4=="K1" or D4=="S1"):
                    Dcount+=11
                    Donearu=True
                 if(D4=="D2" or D4=="H2" or D4=="K2" or D4=="S2"):
                    Dcount+=2
                 if(D4=="D3" or D4=="H3" or D4=="K3" or D4=="S3"):
                    Dcount+=3
                 if(D4=="D4" or D4=="H4" or D4=="K4" or D4=="S4"):
                     Dcount+=4        
                 if(D4=="D5" or D4=="H5" or D4=="K5" or D4=="S5"):
                    Dcount+=5 
                 if(D4=="D6" or D4=="H6" or D4=="K6" or D4=="S6"):
                    Dcount+=6  
                 if(D4=="D7" or D4=="H7" or D4=="K7" or D4=="S7"):
                     Dcount+=7             
                 if(D4=="D8" or D4=="H8" or D4=="K8" or D4=="S8"):
                    Dcount+=8   
                 if(D4=="D9" or D4=="H9" or D4=="K9" or D4=="S9"):
                    Dcount+=9             
                 if(D4=="D10" or D4=="H10" or D4=="K10" or D4=="S10" or D4=="DJ" or D4=="HJ" or D4=="KJ" or D4=="SJ" or D4=="DQ" or D4=="HQ" or D4=="KQ" or D4=="SQ" or D4=="DK" or D4=="HK" or D4=="KK" or D4=="SK") :
                    Dcount+=10  
                 screen.fill((0,100,0))
                 if Dcount>21 and Donearu==True and Donesita==False:
                   Dcount=Dcount-10
                   Donesita=True
                 text(screen,money,kakemoney)
                 kardD2(D2,screen)
                 kardD1(D1,screen)
                 kardD3(D3,screen)
                 kardD4(D4,screen)
                 kardP1(P1,screen)
                 kardP2(P2,screen)
                 text2(screen,Pcount,Dcount)
                 if one==True:
                   kardP3(P3,screen)
                 if two==True:
                   kardP4(P4,screen)
                 if three==True:
                   kardP5(P5,screen)
                 
                 pygame.display.update()
                 time.sleep(1)
                 if Dcount >21:
                     Pwin(screen,money,kakemoney)
                 if Dcount==Pcount and Pcount>16:
                      drow(screen,money,kakemoney)
                 if Dcount>16:
                   if Dcount<Pcount:
                     Pwin(screen,money,kakemoney)
                   else:
                     Ploose(screen,money)
                 
                 else:
                     if(D5=="D1" or D5=="H1" or D5=="K1" or D5=="S1"):
                      Dcount+=11
                      Donearu=True
                     if(D5=="D2" or D5=="H2" or D5=="K2" or D5=="S2"):
                       Dcount+=2
                     if(D5=="D3" or D5=="H3" or D5=="K3" or D5=="S3"):
                        Dcount+=3
                     if(D5=="D4" or D5=="H4" or D5=="K4" or D5=="S4"):
                       Dcount+=4        
                     if(D5=="D5" or D5=="H5" or D5=="K5" or D5=="S5"):
                       Dcount+=5 
                     if(D5=="D6" or D5=="H6" or D5=="K6" or D5=="S6"):
                        Dcount+=6  
                     if(D5=="D7" or D5=="H7" or D5=="K7" or D5=="S7"):
                      Dcount+=7             
                     if(D5=="D8" or D5=="H8" or D5=="K8" or D5=="S8"):
                       Dcount+=8   
                     if(D5=="D9" or D5=="H9" or D5=="K9" or D5=="S9"):
                       Dcount+=9             
                     if(D5=="D10" or D5=="H10" or D5=="K10" or D5=="S10" or D5=="DJ" or D5=="HJ" or D5=="KJ" or D5=="SJ" or D5=="DQ" or D5=="HQ" or D5=="KQ" or D5=="SQ" or D5=="DK" or D5=="HK" or D5=="KK" or D5=="SK") :
                      Dcount+=10  
                     screen.fill((0,100,0))
                     if Dcount>21 and Donearu==True and Donesita==False:
                       Dcount=Dcount-10
                       Donesita=True
                     text(screen,money,kakemoney)
                     kardD2(D2,screen)
                     kardD1(D1,screen)
                     kardD3(D3,screen)
                     kardD4(D4,screen)
                     kardD5(D5,screen)
                     kardP1(P1,screen)
                     kardP2(P2,screen)
                     text2(screen,Pcount,Dcount)
                     if one==True:
                      kardP3(P3,screen)
                     if two==True:
                       kardP4(P4,screen)
                     if three==True:
                      kardP5(P5,screen)
                     
                     pygame.display.update()
                     time.sleep(1)
                     if Dcount>21:
                        Pwin(screen,money,kakemoney)
                     if Dcount==Pcount and Pcount>16:
                         drow(screen,money,kakemoney)
                     
                     if Dcount<Pcount:
                          Pwin(screen,money,kakemoney)
                     else:
                          Ploose(screen,money)
                   




          
        
def main():
    
    pygame.init()    
    
    screen = pygame.display.set_mode((800, 600))
    scene =1
 
    money=100
    
    pygame.display.set_caption("GAME")              # タイトルバーに表示する文字
    font1 = pygame.font.Font(None, 80) 
    font = pygame.font.Font(None, 55) 
    font2 = pygame.font.Font(None, 40) 
    run=True
    # 画面を更新
    suu=font2.render(str(scene), True, (255,255,255))
    Strat(screen)
    
    while run:
        
       
        
      
           
         
        # イベント処理
       
          
        

        for event in pygame.event.get():
            
            if event.type == KEYDOWN:  # キーを押したとき
      
               if event.key==K_q:
                   pygame.display.update()
               if event.key==K_n:
                   round=0
                   run=False
                   main()      
            # ESCキーならスクリプトを終了
               if event.key==K_ESCAPE:
                 webbrowser.open("http://localhost:5000/")
                 pygame.quit()
                 sys.exit()
               
               if event.key == K_SPACE and scene==2:
                   
                    screen.fill((0,100,0))
                    pygame.display.update() 
                    scene=3
                   
                    
              
               if event.key ==K_SPACE and scene ==1:
                   screen.fill((0,100,0))
                   pygame.display.update() 
                   Game(screen,money)
                   run=False
              
           
                 

                

            if event.type == QUIT:
                webbrowser.open("http://localhost:5000/")  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
             
               


if __name__ == "__main__":
    main()


