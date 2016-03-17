from random import randint
from player import Player
"""

This is where the meat of the gameplay takes place. Returns, spins, and games played.

"""
class Controller(object):
    def __init__(self,game):
        self.game = game
        self.total_game_num = self.total_games_calc(game)


    def add_up_total(self,current_num,total):
        if(current_num==0):
            return total
        else:
            total=total+current_num
            current_num -=1
            return self.add_up_total(current_num,total)

    def total_games_calc(self,game):
        player_num = len(game.playerlist)
        return self.add_up_total(player_num-1,0)


    def find_winner(self,player_list):
        highest_score_player = player_list[0].name
        highest_score = player_list[0].win
        current_best_player = player_list[0]
        for player in player_list[1:]:
            if highest_score < player.win:
                highest_score=player.win
                highest_score_player = player.name
                current_best_player = player
            elif highest_score == player.win:
                print "here comes the tie-breaker"
                print "%s and %s have the same wins" % (current_best_player.name,player.name)
                if current_best_player.total_score < player.total_score:

                    highest_score=player.win
                    highest_score_player = player.name
                    current_best_player = player
                elif current_best_player.total_score == player.total_score:
                    print "%s and %s have the same total score" % (current_best_player.name,player.name)
                    winner = self.check_old_game(current_best_player,player)
                    highest_score= winner.win
                    highest_score_player = winner.name
                    current_best_player = winner

        return [highest_score_player,highest_score]

    def check_old_game(self,player_A,player_B):
        for game in self.game.all_games:
            if (player_A.name in game) and (player_B.name in game):
                if player_A.name ==  game[0]:
                    winner = player_A
                else:
                    winner = player_B
                return winner

    def play(self,game_played):

        if(game_played==self.total_game_num):
            result = self.find_winner(self.game.playerlist)
            winner_name = result[0]
            winner_wins = result[1]
            print "winner is: %s, with  %d wins ." % (winner_name, winner_wins)
            print "-------------------------TOURNAMENT END-------------------------------"
            print "-------------------------THE WINNER IS-------------------------------"
            if(winner_name == "Mark"):
                print "___  ___  ___  ______  _   __"
                print "|  \/  | / _ \ | ___ \| | / /"
                print "| .  . |/ /_\ \| |_/ /| |/ / "
                print "| |\/| ||  _  ||    / |    \ "
                print "| |  | || | | || |\ \ | |\  \ "
                print "\_|  |_/\_| |_/\_| \_|\_| \_/"
            elif(winner_name == "Dr. Claw"):
                print " ____  ____               ___  __     __   _  _ "
                print "(    \(  _ \             / __)(  )   / _\ / )( \ "
                print " ) D ( )   /  _         ( (__ / (_/\/    \\ /\ / "
                print "(____/(__\_) (_)         \___)\____/\_/\_/(_/\_)"
            elif(winner_name == "O-Ren Ishii"):
                print "  ____         ___                    ____        __    _    _  "
                print " / __ \ ____  / _ \ ___   ___        /  _/  ___  / /   (_)  (_)"
                print "/ /_/ //___/ / , _// -_) / _ \      _/ /   (_-< / _ \ / /  / / "
                print "\____/      /_/|_| \__/ /_//_/     /___/  /___//_//_//_/  /_/  "
            return
        self.game.overtime = False
        players = self.pick_players(self.game)
        player_A = players[0]
        player_B = players[1]
        print ""
        print "                    < %s > VS < %s >                               " % (player_A.name, player_B.name)
        print ""
        print "------------------------- GAME START -------------------------------"
        winner_name = self.start_round(player_A,player_B,0,0)
        game_played+=1
        self.play(game_played)


    def pick_players(self,game):
        random_A = game.playerlist[randint(0,game.player_num-1)]
        #list_random_pick_list = [];
        if(len(random_A.game_record) < game.player_num-1):
            random_B = game.playerlist[randint(0,game.player_num-1)]

            while((random_B.name == random_A.name) or random_A.playbefore(random_B.name)):
                random_B = game.playerlist[randint(0,game.player_num-1)]
            #print "Player A is %s, Player B is  %s." % (random_A.name, random_B.name)
            return [random_A,random_B]
        else:
            return self.pick_players(game)

    """
    Finds the winner based on how many wins each player has.
    If a tie-breaker occurs it first compares the total scores of each player in question,
    then if both players have the same score it
    goes back to the game played against the two players
    who are tied and decides the winner based on who won that game and the winner of
    that game wins the tournament.
    """
    def start_round(self,player_A,player_B,player_A_score,player_B_score):
        if 10 <= max(player_A_score,player_B_score):
            self.game.overtime = True
        if self.game.overtime:
            if (abs(player_A_score-player_B_score) == 1):
                if(player_A_score > player_B_score):
                    print "The current score is: %s: %d vs %s: %d ." % (player_A.name,player_A_score,player_B.name,player_B_score)
                    return self.serve_and_play(player_B,player_A,player_B_score,player_A_score)
                elif (player_A_score < player_B_score):
                    print "The current score is: %s: %d vs %s: %d ." % (player_A.name,player_A_score,player_B.name,player_B_score)
                    return self.serve_and_play(player_A,player_B,player_A_score,player_B_score)
        if(player_A_score>=11 and (player_A_score>(player_B_score+1))):
            print "Player:  %s: wins the game against %s. The score is %d : %d" %  (player_A.name,player_B.name,player_A_score,player_B_score)
            print "-------------------------GAME END-------------------------------"
            player_A.game_over(player_B.name,"win")
            player_B.game_over(player_A.name,"lose")
            self.game.all_games.append([player_A.name,player_B.name])
            return player_A.name
        if(player_B_score>=11 and (player_B_score>(player_A_score+1))):
            print "Player:  %s: wins the game against %s. The score is %d : %d" %  (player_B.name,player_A.name,player_B_score,player_A_score)
            print "-------------------------GAME END-------------------------------"
            player_B.game_over(player_A.name,"win")
            player_A.game_over(player_B.name,"lose")
            self.game.all_games.append([player_B.name,player_A.name])
            return player_B.name
        print "The current score is: %s: %d vs %s: %d ." % (player_A.name,player_A_score,player_B.name,player_B_score)
        return self.serve_and_play(player_A,player_B,player_A_score,player_B_score)
    """
    Serve and switch after two serves
    """
    def serve_and_play(self,player_A,player_B,player_A_score,player_B_score):
        if(self.serve(player_A,player_B)):
            scored_player_name = self.return_ball(player_A,player_B,True)
            if(scored_player_name == player_A.name):
                player_A_score+=1
                player_A.total_score +=1
            else:
                player_B_score+=1
                player_B.total_score +=1
            total_score = player_A_score+player_B_score
            if(total_score!= 0 and total_score % 2 == 0):
                return self.start_round(player_B,player_A,player_B_score,player_A_score)
            else:
                return self.start_round(player_A,player_B,player_A_score,player_B_score)
        else:
            player_B_score+=1
            player_B.total_score +=1
            total_score = player_A_score+player_B_score
            if(total_score!= 0 and total_score % 2 == 0):
                return self.start_round(player_B,player_A,player_B_score,player_A_score)
            else:
                return self.start_round(player_A,player_B,player_A_score,player_B_score)
    """
    function to serve to other player and based on accuracy detect whether
    player is in-bounds or out of bounds
    """
    def serve(self,player_A,player_B):
        serve_pos = randint(0,99)
        #print "Player %s is serving ." % player_A.name
        if(serve_pos < int(player_A.serve_accuracy)):
            print "%s serves to %s ... in-bounds" % (player_A.name, player_B.name)
            return True
        else:

            print "%s serves to %s ... out of bounds" % (player_A.name, player_B.name)
            return False
    """
    Detect whether player returns serve/volley and calculate spin into chance to return
    the hit
    """
    def return_ball(self,player_A,player_B,first):
        return_pos = randint(0,99)
        reskillB = int(player_B.return_skill)
        spin = int(player_A.return_spin)
        if(first):
            spin = int(player_A.serve_spin)
        reskillB = reskillB - spin
        #print "Player %s's return skill is %d" % (player_B.name, reskillB)
        if(return_pos < reskillB):
            return_in_pos = randint(0,99)
            if(return_in_pos < int(player_B.return_accuracy)):
                #print "return_in_pos is %d " % return_in_pos
                print "%s returns to %s ... in bounds" % (player_B.name, player_A.name)
                self.return_ball(player_B,player_A,False)

            else:
                print "%s returns to %s ... out of bounds" % (player_B.name, player_A.name)
                return player_A.name
        else:
            print "%s fails to return" % player_B.name
            return player_A.name
