
class Player:
    def __init__(self, attack, defence, magic, shield, hitChance, blockChance, health = 100):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.hitChance = hitChance
        self.blockChance = blockChance
        self.shield = shield
        self.effects = {}
        self.charge = {}
        self.turns = 0

    def onTurn(self, turns):
        self.turns += 1
        for mov in self.charge:
            self.charge[mov] -= 1
        for effect in self.effects:
            self.effects[effect] -= 1
            
        for mov in self.charge:
            if self.charge[mov] == 0:
                mov.inflict(charge=0, Player= self)
                self.charge.pop(mov)

class move:
    def __init__(self, charge = 0, damage = 0, shield = 0, statusEffects = None, statusEffectsTurn = None, heal = 0):
        self.damage = damage
        self.shield = shield
        self.statusEffects = statusEffects
        self.statusEffectsTurn = statusEffectsTurn
        self.heal = heal
        self.Player = Player
        self.charge = charge

    def inflict(self, Player, charge):
        if charge == 0:
            Player.health - self.damage
            Player.health + self.heal
            Player.effects[self.statusEffects] = self.statusEffectsTurn
            Player.shield + self.shield
        else:
            Player.charge[self] = self.charge
        

            


Whirlwind = move(damage= 2)

Earths_Vengeance = move(damage=3, statusEffects= 'Bl', statusEffectsTurn= 1)

Slashdown = move(damage=3, charge=3)
