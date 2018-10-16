'''
Created on Oct 15, 2018

@author: lfko

    let us play a silly game of rock-paper-scissor, shan't we?
'''

# import sys;


def main():
    
    print('What do you want to do?');
    print('    --- (1) start a game');
    print('    --- (2) exit');
    print('    --- (3) show help');
    
    game_input = input();
    print('You have selected ', game_input);

    def dispatch_game_cmd(arg):
        dispatch = {
            1:play_game(),
            2:"iki",
            3:"üs",
        }
        return dispatch.get(arg, "nothing");

    # this will call the selected method automatically
    dispatch_game_cmd(int(game_input));
    # print(dispatch_game_cmd(int(game_input)));
    

def play_game():
    
    weapons = ['rock', 'paper', 'scissor', 'laser'];
    
    print('available weapons: ', weapons);
    wpn_1 = input('First player - choose yours:');
    wpn_2 = input('Second player - choose yours:');

    print('%s versus %s - who wins?' % (wpn_1, wpn_2));

    # evaluate the victory condition
    res, state = eval_victory(wpn_1, wpn_2);
    
    if state == False:
        print(' game is not decided yet - you need to play again!');
        play_game();
    else:  
        print(' final result: ', res);


def eval_victory(wpn_p1, wpn_p2):
    """ evaluate victory (or draw) 
    
        it returns a tuple, containing a string representation of the game result and a boolean for further processing, e.g. "P1 wins", true;
    """
    
    # victory conditions: [0] wins against [1]
    vic_cond = [['rock', 'scissor'], ['scissor', 'paper'], ['paper', 'rock']];
    
    # easy case: both selected the same weapon - this is a draw
    if wpn_p1 == wpn_p2:
        return "Draw!", False;

    game = [wpn_p1, wpn_p2];
    if game in vic_cond:
        print('Winner! ', game[0], ' wins over ', game[1]);
        return "P1WIN", True;
    else:
        # victory was not matched yet, because the specific winning-pair had not been found yet
        # in order to search for it, the elements need to be switched
        game[0], game[1] = game[1], game[0];
        print(game);
        if game in vic_cond:
            print('Winner! ', game[0], ' wins over ', game[1]);
            return "P2WIN", True;

        
if __name__ == '__main__':
    main();
