class Game:
    
    def __init__(self, battle_number, alive_number, winner, loser):
        self.battle_number = battle_number
        self.alive_number = alive_number
        self.winner = winner
        self.loser = loser

    def get_game_description(self):
        template = ("#PokemonBattle nº {:03d}!\n"
            + "#{winner} Vs #{loser}!\n"
            + "Fight!\n{winner} wins!\n"
            + "{left} left.\n"
            + "Who would beat them all?\n"
            + "#PokemonWarBot #Pokemon")
        description = template.format(
            self.battle_number, 
            winner=self.winner.name, 
            loser=self.loser.name, 
            left=self.alive_number)
        return description