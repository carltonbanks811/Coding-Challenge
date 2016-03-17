"""
This is the Player class. It holds who the player has played against [game_record], the 
players skills, win/loss record, and total score.
"""
class Player(object):
    def __init__(self,name,serve_accuracy,serve_spin,return_skill,return_accuracy,return_spin):
        self.name = name
        self.serve_accuracy = serve_accuracy
        self.serve_spin = serve_spin
        self.return_skill = return_skill
        self.return_accuracy = return_accuracy
        self.return_spin = return_spin
        self.game_record = []
        self.total_score = 0
        self.win = 0
        self.lose = 0
    """
    Detect whether player has played opponent before.
    """
    def playbefore(self,player_b_name):
        result = False
        for player_name in self.game_record:
            if(player_name == player_b_name):
                result = True
        return result
    """
    Add 1 to players win/loss record
    """
    def game_over(self,player_b_name,result):
        if(result=="win"):
            self.win +=1
        else:
            self.lose +=1
        self.game_record.append(player_b_name)
