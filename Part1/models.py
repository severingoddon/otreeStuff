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
    asset_9 = [999,99]
    asset_10 = [1000,100]
    asset_11 = [1111, 111]
    asset_12 = [2222, 222]
    assets = [
        [111, 11],
        [222, 22],
        [333, 33],
        [444, 44],
        [555, 55],
        [666, 66],
        [777, 77],
        [888, 88],
        [999, 99],
        [1000, 100],
        [1111, 111],
        [2222, 222],
        [3333, 333],
        [4444, 444],
        [5555, 555],
        [6666, 666],
        [7777, 777],
        [8888, 888],
        [9999, 999],
        [10000, 1000],
    ]
    Asset_1={"Win": assets[0][0], "Lose":assets[0][1]}
    Asset_2={"Win": assets[1][0], "Lose":assets[1][1]}
    Asset_3 = {"Win": assets[2][0], "Lose": assets[2][1]}
    Asset_4 = {"Win": assets[3][0], "Lose": assets[3][1]}
    Asset_5 = {"Win": assets[4][0], "Lose": assets[4][1]}
    Asset_6 = {"Win": assets[5][0], "Lose": assets[5][1]}
    Asset_7 = {"Win": assets[6][0], "Lose": assets[6][1]}
    Asset_8 = {"Win": assets[7][0], "Lose": assets[7][1]}
    Asset_9 = {"Win": assets[8][0], "Lose": assets[8][1]}
    Asset_10 = {"Win": assets[9][0], "Lose": assets[9][1]}
    Asset_11 = {"Win": assets[10][0], "Lose": assets[10][1]}
    Asset_12 = {"Win": assets[11][0], "Lose": assets[11][1]}
    Asset_13 = {"Win": assets[12][0], "Lose": assets[12][1]}
    Asset_14 = {"Win": assets[13][0], "Lose": assets[13][1]}
    Asset_15 = {"Win": assets[14][0], "Lose": assets[14][1]}
    Asset_16 = {"Win": assets[15][0], "Lose": assets[15][1]}
    Asset_17 = {"Win": assets[16][0], "Lose": assets[16][1]}
    Asset_18 = {"Win": assets[17][0], "Lose": assets[17][1]}
    Asset_19 = {"Win": assets[18][0], "Lose": assets[18][1]}
    Asset_20 = {"Win": assets[19][0], "Lose": assets[19][1]}


    Assets = (
        (str(Asset_1), str(Asset_2)),
        (str(Asset_3), str(Asset_4)),
        (str(Asset_5), str(Asset_6)),
        (str(Asset_7), str(Asset_8)),
        (str(Asset_9), str(Asset_10)),
        (str(Asset_11), str(Asset_12)),
        (str(Asset_13), str(Asset_14)),
        (str(Asset_15), str(Asset_16)),
        (str(Asset_17), str(Asset_18)),
        (str(Asset_19), str(Asset_20)),
    )

    #Lotteriewahrscheinlichkeiten mit denen gewonnen oder verloren wird
    states=(20,80)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


chosenAssetPairs = []

def resetChosenAssetPairs():
    print("resetted")
    global chosenAssetPairs
    chosenAssetPairs = []

lotterieChoice = random.choice(list(Constants.Assets))

Lotterie1 =  random.choice(lotterieChoice[0])
Lotterie2 = random.choice(lotterieChoice[1])

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
roundcount = 0
####################################################################################################################################

class Player(BasePlayer):
    #die funktion suecht neui asset pairs und tuet die denn de Variable Asset_1 und Asset_2 zuewiise. Damit werdeds gspeicheret
    def updateAssetPair(self):
        global roundcount
        if roundcount >= Constants.num_rounds-1:
            resetChosenAssetPairs()
            roundcount = 0
        else:
            roundcount +=1
        assetPair = random.choice(list(Constants.Assets))
        while chosenAssetPairs.__contains__(assetPair):
            assetPair = random.choice(list(Constants.Assets))
        chosenAssetPairs.append(assetPair)
        firstAsset = assetPair[0]
        secondAsset = assetPair[1]
        self.Asset_1 = firstAsset
        self.Asset_2 = secondAsset
        return [firstAsset,secondAsset]


    first_initial_asset = models.CharField(initial=None)
    second_initial_asset = models.CharField(initial=None)

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
        