import pprint
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

#from ControlAversion.pages import ActionSupervisor

#from ControlAversion.pages import PayoffEmployee


author = 'Diego Loretan'

doc = """
correlation neglect 
"""
# class Constants(BaseConstants):
#     name_in_url = 'ControlAversion'
#     players_per_group = 5
#     num_rounds = 1
#     endowment = c(120.00)
#     multiplier = 2.00
#     participation_fee = 10


class Constants(BaseConstants):
    name_in_url = 'Part1'
    players_per_group = None
    num_rounds = 10
    asset_1 = [111, 11]
    asset_2 = [222, 22]
    asset_3 = [333, 33]
    asset_4 = [444, 44]
    asset_5 = [555, 55]
    asset_6 = [666, 66]
    asset_7 = [777, 77]
    asset_8 = [888, 88]
    Asset_1={"Win": asset_1[0], "Lose":asset_1[1]}
    Asset_2={"Win": asset_2[0], "Lose":asset_2[1]}
    Asset_3 = {"Win": asset_3[0], "Lose": asset_3[1]}
    Asset_4 = {"Win": asset_4[0], "Lose": asset_4[1]}
    Asset_5 = {"Win": asset_5[0], "Lose": asset_5[1]}
    Asset_6 = {"Win": asset_6[0], "Lose": asset_6[1]}
    Asset_7 = {"Win": asset_7[0], "Lose": asset_7[1]}
    Asset_8 = {"Win": asset_8[0], "Lose": asset_8[1]}


    #Lotteriewahrscheinlichkeiten mit denen gewonnen oder verloren wird
    states=(20,80)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

Assets = (
    str(Constants.Asset_1),str(Constants.Asset_2),str(Constants.Asset_3),str(Constants.Asset_4),str(Constants.Asset_5),str(Constants.Asset_6),str(Constants.Asset_7),str(Constants.Asset_8)
)

lotterieChoice = random.choice(list(Assets))

Lotterie1 =  random.choice(list(Assets))
Lotterie2 = random.choice(list(Assets))
while Lotterie1 == Lotterie2:
    Lotterie2 = random.choice(list(Assets))


print("Lotterie 1 ist", Lotterie1)
print("Lotterie 2 ist", Lotterie2)

#wählt eine der so bestimmten Lotterien und teit sie Porfolio A zu
Lotterie = (Lotterie1,Lotterie2)
Portfolio_Choice= random.choice(list(Lotterie))
Portfolio_A= Portfolio_Choice
print("Portfolio_A is:", Portfolio_A)

#teilt die andere Lotterie Portfolio B zu 
if Portfolio_A==(Lotterie1):
    Portfolio_B=(Lotterie2)
else: 
    Portfolio_B=(Lotterie1)
print("Portfolio_B is:", Portfolio_B)

#Variable, die im Portfolio die dem Payoff entsprechende Lotterie anzeigt
if Portfolio_A==(Lotterie1):
    correspondinglotteryA='Lotterie 1'
    correspondinglotteryB='Lotterie 2'
else:
    correspondinglotteryA='Lotterie 2'
    correspondinglotteryB='Lotterie 1'

#Variable, die Lotterie 1 und Lotterie 2, die richtigen assets zuteilt.

#

correspondingasset1= 'asset_1'
correspondingasset2= 'asset_2'




####################################################################################################################################

class Player(BasePlayer):

    #die funktion suecht neui asset pairs und tuet die denn de Variable Asset_1 und Asset_2 zuewiise. Damit werdeds gspeicheret
    def updateAssetPair(self):
        firstAsset = random.choice(list(Assets))
        secondAsset = random.choice(list(Assets))
        while firstAsset == secondAsset:
            secondAsset = random.choice(list(Assets))
        self.Asset_1 = firstAsset
        self.Asset_2 = secondAsset
        return [firstAsset,secondAsset]

    # da werded d assetpairs inital und random gsetzt
    first_initial_asset = models.CharField(initial=random.choice(list(Assets)))
    second_initial_asset = models.CharField(initial=random.choice(list(Assets)))

    #falls random die zwei gliche gsetzt werded tuet mer namal es neus zweits asset sueche
    while first_initial_asset == second_initial_asset:
        second_initial_asset = random.choice(list(Assets))

    Asset_1 = models.StringField(initial=first_initial_asset)
    Asset_2 = models.StringField(initial=second_initial_asset)
    Lotterie1 = models.StringField(initial=Lotterie1)
    Lotterie2 = models.StringField(initial=Lotterie2)
    Portfolio_A = models.StringField(initial=Portfolio_A)       
    Portfolio_B = models.StringField(initial=Portfolio_B)
    correspondinglotteryA = models.StringField(initial=correspondinglotteryA)
    correspondinglotteryB = models.StringField(initial=correspondinglotteryB)
    correspondingasset1 = models.StringField(initial= correspondingasset1)
    correspondingasset2 = models.StringField(initial=correspondingasset2)

    Portfolio = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'Portfolio A'], 
            [2, 'Portfolio B']
        ],
        label= None
    )
    

#         #Resultat der gewählten Lotterie
# chosen_Portfolio=Player.Portfolio
# print('You chose:' + chosen_Portfolio)

# if chosen_Portfolio==(Portfolio_A):
#     Draw_A = list(Portfolio_A.items())
#     print(Draw_A)
#     result=random.choices(Draw_A, weights=(100,0), k=1)
#     print('The result is:',result)

# else: 
#     Draw_B = list(Portfolio_B.items())
#     print(Draw_B)
#     result=random.choices(Draw_B, weights=(0,100), k=1)
#     print('The result is:',result)



# Lotterie = {"Lotterie 1":Asset_1,"Lotterie 2":(Asset_2)}
# Portfolio_Choice= random.choice(list(Lotterie.items()))
# Portfolio_A= Portfolio_Choice
# # print("Portfolio_A is:", Portfolio_A)

# if Portfolio_A==('Lotterie 2', {'Win': 300, 'Lose': 20}):
#     Portfolio_B=('Lotterie 1', {'Win': 200, 'Lose': 100})
# else: 
#     Portfolio_B=('Lotterie 2', {'Win': 300, 'Lose': 20})
# # # # print("Portfolio_B is:", Portfolio_B)
# # Portfolio_A_try=str(Portfolio_A)
# Portfolio_B_try=str(Portfolio_B)


    

    # def show_result (self):
    #     p1 = self.get_player_by_id(1)
        
    #     if  p1.Portfolio == 1:
    #         p1.Asset_chosen=Portfolio_A
    #         return(p1.Asset_chosen)
    #     else:
    #         p1.Asset_chosen=Portfolio_B
    #         return(p1.Asset_chosen)
        
    # def winorlose(Asset):
    #     result=random.choices(list(Asset.items()), weights=(50,50), k=1)
    #     print(result)
    #     return(result)


  
    
        
        # def set_payoffs (self):
        # p1 = self.get_player_by_id(1)
        # p2 = self.get_player_by_id(2)
        # p3 = self.get_player_by_id(3)
        # p4 = self.get_player_by_id(4)
        # p5 = self.get_player_by_id(5)
        # if p5.Decision3 == 1:
        #     p1.payoff = ((Constants.endowment - p1.Decision13))
        #     self.p1_decision = float(p1.Decision13)
        #     self.p3_decision = p3.Decision2
            
        # if p5.Decision3 == 1:
        #     self.p5_decision = 1
        