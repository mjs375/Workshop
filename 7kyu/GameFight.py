def fight_resolve(defender, attacker): 
    ### Illegal moves– attacking one's own side:
    if defender.isupper() and attacker.isupper():
        return -1
    if defender.islower() and attacker.islower():
        return -1
    ### Each piece and what it can defeat:
    battles = {
        "a": "sap",
        "p": "kap",
        "s": "ksp",
        "k": "ksa",
    }
    ### Iterate the battles, determine outcome:
    for offense, defeated in battles.items():
        if offense == attacker.lower(): # Match attacker's piece
            if defender.lower() in defeated:
                return attacker
            else:
                return defender
                
                
                
                
                
"""
You are making your very own boardgame. The game is played by two opposing players, featuring a 6 x 6 tile system, with the players taking turns to move their pieces (similar to chess). The design is finished, now it's time to actually write and implement the features. Being the good programmer you are, you carefully plan the procedure and break the program down into smaller managable sections. You decide to start coding the logic for resolving "fights" when two pieces engage in combat on a tile.

Your boardgame features four unique pieces:

Swordsman, Cavalry, Archer and Pikeman

Each piece has unique movement and has advantages and weaknesses in combat against one of the other pieces.

Task
You must write a function fightResolve that takes the attacking and defending piece as input parameters, and returns the winning piece. It may be the case that both the attacking and defending piece belong to the same player, after which you must return an error value to indicate an illegal move.

In C++, C and NASM, the pieces will be represented as chars. Values will be case-sensitive to display ownership. Let the following char values represent each piece from their respective player.

Player 1: p= Pikeman, k= Cavalry, a= Archer, s= Swordsman

Player 2: P= Pikeman, K= Cavalry, A= Archer, S= Swordsman

The outcome of the fight between two pieces depends on which piece attacks, the type of the attacking piece and the type of the defending piece. Archers always win against swordsmens, swordsmen always win against pikemen, pikemen always win against cavalry and cavalry always win against archers. If a matchup occurs that was not previously mentioned (for example Archers vs Pikemen) the attacker will always win. This table represents the winner of each possible engagement between an attacker and a defender.

(Attacker→)
(Defender↓)	Archer	Pikeman	Swordsman	Knight
Knight	Defender	Attacker	Attacker	Attacker
Swordsman	Attacker	Defender	Attacker	Attacker
Archer	Attacker	Attacker	Defender	Attacker
Pikeman	Attacker	Attacker	Attacker	Defender

If two pieces from the same player engage in combat, i.e P vs S or k vs a, the function must return -1 to signify and illegal move. Otherwise assume that no other illegal values will be passed.

"""
