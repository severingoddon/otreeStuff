import random
import re

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group, BaseGroup, BasePlayer, Portfolio_A, Portfolio_B

class Decision (Page):
    form_fields = ["Portfolio"]
    form_model = Player

    def vars_for_template(self):
        assetpairs = self.player.updateAssetPair()
        firstSplit = assetpairs[0].split(",") #assetpairs chömed als strings daher, drum tuet mer sie da no ufbereite
        secondSplit = assetpairs[1].split(",")
        firstAssetFirstNumber = re.findall(r'\d+', firstSplit[0]) #mittels regex chasch useme string nur d zahle use extrahiere
        firstAssetSecondNumber = re.findall(r'\d+', firstSplit[1])
        secondAssetFirstNumber = re.findall(r'\d+', secondSplit[0])
        secondAssetSecondNumber = re.findall(r'\d+', secondSplit[1])

        return {'chosen_portfolio': self.player.Portfolio, 'state_1': Constants.states[0],'state_2': Constants.states[1],
                'Asset_1_state_1': firstAssetFirstNumber[0], 'Asset_1_state_2': firstAssetSecondNumber[0],
                'Asset_2_state_1': secondAssetFirstNumber[0], 'Asset_2_state_2': secondAssetSecondNumber[0],
                'correspondinglotteryA': self.player.correspondinglotteryA, 'correspondinglotteryB': self.player.correspondinglotteryB,
                'correspondingasset1': self.player.correspondingasset1, 'correspondingasset2': self.player.correspondingasset2}

    # def vars_for_template(self):
    #     # p1=self.player.p1_Portfolio
    #     Result=p1.Asset_chosen



page_sequence = [Decision]