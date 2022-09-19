from game.die import Die

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
        
        # if player chooses to quit rolling, show final score
        if not self.is_playing:
            print(f"Final score is {self.total_score}\n")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        # added to correct inaccurate score additions
        self.score = 0

        # original code from incomplete-dice
        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
        
        # changed - instead of just adding score from this round, check to see 
        # if zero, if so, zero total so player knows they busted
        if self.score > 0:
            self.total_score += self.score
        else:
            self.total_score = 0

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        
        # changed so game would end if current round score is zero and show 
        # final score
        self.is_playing = (self.score > 0) 

        # added to let player know the roll failed to give any points, score is 
        # zero, game over
        if not self.is_playing:
            print("Fail. Score is zero.\n")