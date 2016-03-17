from controller import Controller
from player import Player
import csv
"""
This is the Game class. It holds the list of opponents, number of players,
the game controller, a record of the games played and whether or not the game
has gone into overtime
"""
class Game(object):
    def __init__(self,file_name):
        self.playerlist = self.readfile(file_name)
        self.player_num  = len(self.playerlist)
        self.game_controller = Controller(self)
        self.all_games = []
        self.overtime = False;

    def start(self):
        print "------------------------- START -------------------------------"
        self.game_controller.play(0)

    """
    This function reads the CSV and compiles a list of players
    with all of their relevant data.
    """
    def readfile(self,file_name):
        my_list =[]
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(f)
            for row in reader:
                my_list.append(Player(row[0], row[1], row[2], row[3], row[4], row[5]))
        return my_list
        # read file code here
        # create palyers
