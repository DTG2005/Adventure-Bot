
class Player:
    def __init__(self, attack, defence, magic, shield, hitChance, blockChance, health = 100):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.canUseMove = True
        self.magic = magic
        self.hitChance = hitChance
        self.blockChance = blockChance
        self.shield = shield
        self.effects = {}
        self.charge = {}
        self.cooldown = {}
        self.turns = 0

    def onTurn(self, turns):
        if self.charge or self.cooldown:
            self.canUseMove = False
        self.turns += 1
        for mov in self.charge:
            self.charge[mov] -= 1
        for effect in self.effects:
            self.effects[effect] -= 1
        for mov in self.cooldown:
            self.cooldown[mov] -= 1
            
        for mov in self.charge:
            if self.charge[mov] == 0:
                mov.inflict(charge=0, Player= self)
                self.charge.pop(mov)

class move:
    def __init__(self, movetype, charge = 0, damage = 0, shield = 0, statusEffects = None, statusEffectsTurn = None, heal = 0, cooldown = 0, blockChanceChange = 0, missChanceChange = 0, effectcancel = []):
        self.damage = damage
        self.effectcancel = effectcancel
        self.shield = shield
        self.statusEffects = statusEffects
        self.statusEffectsTurn = statusEffectsTurn
        self.heal = heal
        self.Player = Player
        self.blockChanceChange = blockChanceChange
        self.missChanceChange = missChanceChange
        self.movetype = movetype
        self.charge = charge
        self.cooldown = cooldown

    def inflict(self, Playerown, Player, charge):
        if Playerown.canUseMove:
            if charge == 0:
                Player.health - self.damage
                if effectcancel:
                    for effect in self.effectcancel:
                        Playerown.effects.pop(effect)
                Playerown.health + self.heal
                if self.movetype == "Helpful":
                    Playerown.effects[self.statusEffects] = self.statusEffectsTurn
                    Playerown.blockChance + self.blockChanceChange
                    Playerown.hitChance - self.missChanceChange
                else:
                    Player.effects[self.statusEffects] = self.statusEffectsTurn
                    Player.blockChance - self.blockChanceChange
                    Player.hitChance + self.missChanceChange
                Player.shield + self.shield
                Player.cooldown[self] = self.cooldown
            else:
                Player.charge[self] = self.charge
        

            


Whirlwind = move(movetype = "Harmful", damage= 2)

Earths_Vengeance = move(movetype = "Harmful", damage=3, missChanceChange=1)

Slashdown = move(movetype="Harmful", damage=3, charge=3)

Stabdown = move(movetype="Harmful", charge=1, damage=2)

Headbutt = move(movetype = "Harmful", damage=1)

Smashdown = move(movetype = "Harmful", charge=2, damage=4, statusEffects="stun", cooldown= 0)

Braceup = move(movetype="Helpful", blockChanceChange= 0.3)

Dodge = move(movetype= "Harmful", missChanceChange= 0.3)

Longshot = move(movetype="Helpful", missChanceChange=0.1)

Protection = move(movetype="Helpful", blockChanceChange=0.1)

Woundcheck = move(movetype="Harmful", damage= 3)

Deep_cut = move("Harmful", charge= 1, damage= 3, statusEffects= "Bleed", statusEffectsTurn= 4)

Iron_fist = move("Harmful", charge= 3, damage= 7, statusEffects= "Stun", statusEffectsTurn=1)

Mashdown = move("Harmful",damage=2, statusEffects= "Stun", statusEffectsTurn=1)

Unbreakable = move("Helpful", blockChanceChange=.35)

Heads_up = move("Helpful", blockChanceChange= .4, cooldown= 1)

Medics_praise = move("Helpful", heal=5, effectcancel=["Burn", "Bleed", "Trauma", "Weakness", "Fatugue"])

Lightning = move("Harmful", damage=4, statusEffects= "Stun", statusEffectsTurn=1)

Strengthening = move("Helpful", blockChanceChange= 0.3)

Flasher = move("Harmful", blockChanceChange= 0.3)

Levitator = move("Harmful", damage= 6)

Sunburn = move("Harmful", damage=5, missChanceChange=1)

Slice = move("Harmful", damage=3, statusEffects= "Bleed", statusEffectsTurn=4),

Pain_Slash = move("Harmful", damage=5, statusEffects = "Trauma")

Finish = move("Harmful", charge= 3, damage= 10, statusEffects= "Stun", statusEffectsTurn= 1)

Smashup = move("Harmful", damage=4, statusEffects= "Weakness", statusEffectsTurn=1),

Backstance = move("Helpful", blockChanceChange= .1)

