from tkinter import *



#Cette classe Gerera toute les propriéte des cases du Damier 
class Case:
    
    def __init__(self, x1, y1, x2, y2, ColorCase, ColorPion, Pion ):
        
        self.x1= x1
        self.x2= x2
        
        self.y1 = y1
        self.y2 = y2
        
        self.ColorCase = ColorCase
        self.ColorPion = ColorPion
        
        self.Pion = Pion
    
    """
        Cette methode sert à verifier si la case et vide ou non 
    """
    def __eq__(self, other):
          return (self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2)    

    """
        Cette methode sert à recuperer les Coordonnées de la case
    """
    def GetCoordCase(self):
        return [self.x1,self.y1,self.x2,self.y2]
    
    """
        Cette methode sert à recuperer les Coordonnées du Pion
    """
    def GetCoordPion(self):
        return [self.x1+10,self.y1+10,self.x2-10,self.y2-10]
    
    """
        Cette methode sert à Definir un Pion
    """    
    def SetPion(self, Val):
        self.Pion = Val
    
    """
        Cette methode sert à Definir un la couleur Pion
    """        
    def SetColorPion(self, Val):
        self.ColorPion = Val
    
    """
        Cette methode sert à creer une case
    """                
    def CreerCase(self):
        Can.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill=self.ColorCase)    
    
    """
    Cette methode sert à placer le Pion dans une case
    """
    def PlacerPion(self):
        if self.Pion:
           Can.create_oval(self.x1+10,self.y1+10,self.x2-10,self.y2-10, fill=self.ColorPion)
    
    """
        Cette methode sert à positionner le Pion
    """
    def gauche(self):
        for case in tout_les_cases:
            if case.x1 == self.x1-40 and case.x2 == self.x2-40 and case.y1 == self.y1:
                return case
        return caseNeutre    

    def droite(self):
        for case in tout_les_cases:
            if case.x1 == self.x1+40 and case.x2 == self.x2+40 and case.y1 == self.y1:
                return case 
        return caseNeutre      

    def haut(self):
        for case in tout_les_cases:
            if case.y1 == self.y1-40 and case.y2 == self.y2-40 and case.x1 == self.x1:
                return case  
        return caseNeutre        

    def bas(self):
        for case in tout_les_cases:
            if case.y1 == self.y1+40 and case.y2 == self.y2+40 and case.x1 == self.x1:
                return case  
        return caseNeutre
    def PeutBougerVers(self,dest):
    
        #recupere la case de destination 
        CaseDest=Trouver_Case(dest)
    
        #si le case de destination n'est pas retrouver alors on returne 0
        if not CaseDest:
            return 0
        
        else:
            
            #cette condition permet de verifier si il y'a pas un Pion
            #ou une case qui bloque le deplacement
            #elle permet aussi de doubler un Pion de la meme couleurs 
            if CaseDest.Pion or (
                not CaseDest.__eq__(self.gauche()) and not CaseDest.__eq__(self.gauche().gauche())
                and not CaseDest.__eq__(self.droite()) and not CaseDest.__eq__(self.droite().droite())
                and not CaseDest.__eq__(self.haut()) and not CaseDest.__eq__(self.haut().haut())
                and not CaseDest.__eq__(self.bas()) and not CaseDest.__eq__(self.bas().bas())) or (
                CaseDest.__eq__(self.gauche().gauche()) and (
                not self.gauche().Pion or self.gauche().ColorPion == self.ColorPion)) or (
                CaseDest.__eq__(self.droite().droite()) and (
                not self.droite().Pion or self.droite().ColorPion == self.ColorPion)) or (
                CaseDest.__eq__(self.haut().haut()) and (
                not self.haut().Pion or self.haut().ColorPion == self.ColorPion)) or (
                CaseDest.__eq__(self.bas().bas()) and (
                not self.bas().Pion or self.bas().ColorPion == self.ColorPion)):
                return 0
             
        return 1
"""
    Cette fonction sert a afficher le damier
"""
def Dam():
  
    #Recupere les variable X et Y 
    global x1,x2,y1,y2
    ite,i,ColorCase = 0,1,'Black'

    #Cette boucle permettra d'afficher toute les case 
    while x1<500 and y1<350:
    
        #Ces conditions permet de definir les Pions aux joueurs et les case vide
        if i <= 27:
            ColorPion = '#9feb87'
            tout_les_cases.append(Case(x1,y1,x2,y2,ColorCase,ColorPion,1))
        
        elif i > 54:
            ColorPion = '#ffde01'
            tout_les_cases.append(Case(x1,y1,x2,y2,ColorCase,ColorPion,1))
        
        else: tout_les_cases.append(Case(x1,y1,x2,y2,ColorCase,'',0))        

        #Ces lignes de commandes permet de creer les case D'une ligne 
        tout_les_cases[-1].CreerCase()
        i,ite,x1,x2=i+1,ite+1,x1+40,x2+40
        
        #Cette Condition permet de rajouter une nouvelle ligne
        if ite == 9:
            y1,y2=y1+40,y2+40
            ite,x1,x2=0,5,45
        
        #Ces conditions permet de colorier la case
        if i%2 == 0:
            ColorCase='white'
        else: ColorCase='black'

    #Cette boucle sert à rajouter les Pions dans les cases
    for case in tout_les_cases:
       case.PlacerPion()
    
    ButtonDam.destroy()
    Score.pack()
    ButtonQuit.pack()
    
    
    

#Cette methode sert a recuperer l'emplacement de la case pointer par la souris
def Trouver_Case(Coord):
  for case in tout_les_cases:
      if case.x1 == Coord[0] and case.y1 == Coord[1] and case.x2 == Coord[2] and case.y2 == Coord[3]:
        return case     
  return 0    


def Clique(event):
    global CaseDepart,PionClique,session
    x,y=event.x,event.y
    PionClique = 0
    CaseDepart = 0
    
    #Recupere l'emplacement du clique    
    clique = Can.find_overlapping(x, y, x, y)
    
    #Cette condition Verifie si on à recuperer toute les emplacement 
    if len(clique)>1 :
        
        #Recupere les coordonees et la case avec la fonction coord et Trouver_Case
        Coord = Can.coords(clique[0])
        CaseDepart= Trouver_Case(Coord)
        
        #cette condition permet de recuperer le Pion
        if CaseDepart.ColorPion == session:
            PionClique = 0
        else:  
            PionClique = clique[1]
            print(PionClique)

def Bouger(event):
    global CaseDepart,PionClique
    x,y=event.x,event.y 
    
    #cette condition permet le deplacement d'un Pion
    if CaseDepart and PionClique:
        Coord=Can.coords(PionClique)
        deplacement  = [[x-10, y-10, x+10, y+10]]
        Can.coords(PionClique, deplacement[0])

def Arret(event):
    global CaseDepart,PionClique,session, ScoreV, ScoreJ
    x,y=event.x,event.y 
    
    collision = Can.find_overlapping(x-10,y-10,x+10,y+10)
    Coord = Can.coords(collision[0])
    
    #Cette condition permet de definir ou est arrete le Pion
    if CaseDepart and PionClique:
        
        #Cette condition sert a retourner le Pion si il peut pas allez a sa destination
        if not CaseDepart.PeutBougerVers(Coord):
            Can.coords(PionClique, CaseDepart.GetCoordCase())
        else:
            CaseDest = Trouver_Case(Coord)
            
            #si la case de depart est différent de la case d'arriver
            if not CaseDepart.__eq__(CaseDest):
                
                #on met les info de la case de depart à la case d'arriver
                session=CaseDepart.ColorPion
                CaseDest.SetPion(1)
                CaseDest.SetColorPion(CaseDepart.ColorPion)
                
                #place le Pion a la case du destinataire
                Can.coords(PionClique, CaseDest.GetCoordPion())
                
                #renitialise la case de depart
                CaseDepart.SetPion(0)
                CaseDepart.SetColorPion('')
                
                CaseSupprimer=0

                #Ces condition permet de recuperer la case a cote 
                #de la case de depart pour verifier si il y'a pas 
                #de Pion adverse a supprimer 
                if CaseDest.__eq__(CaseDepart.gauche().gauche()):
                  CaseSupprimer = CaseDepart.gauche()
                
                elif CaseDest.__eq__(CaseDepart.droite().droite()):
                    CaseSupprimer = CaseDepart.droite()     
                
                elif CaseDest.__eq__(CaseDepart.haut().haut()):
                    CaseSupprimer = CaseDepart.haut()    
                
                elif CaseDest.__eq__(CaseDepart.bas().bas()):
                    CaseSupprimer = CaseDepart.bas()
                
                #cette fonction permet de verifier qui d'afficher les point remporter ou le vainqueurs
                #il supprime aussi le Pion manger
                if CaseSupprimer:
                        
                        if CaseSupprimer.ColorPion == '#9feb87':
                            ScoreJ += 1
                        
                        else: 
                            ScoreV+=1  
                        
                        Score.configure(text='V : {}  vs  J : {}'.format(ScoreV,ScoreJ)) 
                        
                        if ScoreJ >= 27:
                            Score.configure(text='Victoire J : {}'.format(ScoreJ)) 
                        
                        elif ScoreV >= 27:
                            Score.configure(text='Victoire V : {}'.format(ScoreV))   
                        
                        c = CaseSupprimer.GetCoordPion()
                        PionSupprimer = Can.find_overlapping(c[0],c[1],c[2],c[3])
                        Can.delete(PionSupprimer[1])
                        CaseSupprimer.SetPion(0)
                    
                    
def screen():
    screen_y = int(App.winfo_screenheight())
    screen_x = int(App.winfo_screenwidth())
    window_x = 550
    window_y = 500

    pos_y = (screen_y // 2 ) - (window_y // 2)
    pos_x = (screen_x // 2 ) - (window_x // 2)

    geo ="{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)
    
    return geo

#Ces variable sert à initialisation du projet

x1,y1,x2,y2 = 5,5,45,45
tout_les_cases = []
caseNeutre = Case(0,0,0,0,'','',0)
ScoreV, ScoreJ, session = 0,0,''


#Cette partie concerne l'affichage graphique
        
App=Tk()

App.title('jeu de la dame')
Font= 'arial 13 bold'
App.geometry(screen())
App.configure(background= 'grey',cursor="hand2")
App.resizable(False,False)

Can = Canvas(App, width=400, height=400, bg='#474546', bd=0)
Can.pack()

Can.bind("<ButtonPress-1>", Clique)
Can.bind("<B1-Motion>", Bouger)
Can.bind("<ButtonRelease-1>", Arret)

Score = Label(App, text=' v=0 vs j=0',font=Font,fg='white', bg='#11030c' )
ButtonQuit = Button(App, text='Quitter', font=Font, command=App.destroy)

ButtonDam = Button(App, text='Depart', command=Dam, font=Font, fg='white', bg='#11030c')
ButtonDam.pack()

App.mainloop()