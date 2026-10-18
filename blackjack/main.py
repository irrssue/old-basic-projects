import random

def random_card():
    """
    Pick random cards, \nrange([11,2,3,4,5,6,7,8,9,10,10,10,10,]) 
    """
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    calculate the score of both user and computer
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0 ## why do I put sum(cards) == 21 there? because 11(ace) + 10 = 21
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return f"It's a draw, both cards: User{user_card} and Computer{computer_card}" # The "user_card" and "computer_card" were taken form public variable
    elif user_score == 0:
        return f"User win wtih {user_card}, score: {userScore}, \nComputer lose with {computer_card} and score: {computerScore}"
    elif computer_score == 0:
        return f"Computer Win with {computer_card}, score: {computerScore}, \nUser lose with {user_card} and score: {userScore}"
    elif user_score > 21:
        return f"User went over 21 wtih cards: {user_card}, Computer Win with cards {computer_card} and score: {computerScore}"
    elif computer_score > 21:
        return f"Computer went over 21 with cards: {computer_card} and score: {computerScore}, User win with cards {user_card} and score: {userScore}"
    elif user_score > computer_score:
        return f"User win wtih {user_card}, score: {userScore}, \nComputer lose with {computer_card} and score: {computerScore}"
    elif computer_score > user_score:
        return f"Computer Win with {computer_card}, score: {computerScore}, \nUser lose with {user_card} and score: {userScore}"
    

print("""

██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
""")

user_card = []  # <-- This will output something along [2,4]
computer_card = []

playing = True

for _ in range(2):
    user_card.append(random_card())
    computer_card.append(random_card())

## Now we have user_card and computer_card     
## ---------------------------------------

while playing:  ##  This loop is considering playing is True
    userScore = calculate_score(user_card) # <-- so now user_card is equal to calculate_score's cards
    print(f"Your cards: {user_card} and your score: {userScore}")
    computerScore = calculate_score(computer_card)
    print(f"Computer cards: {computer_card[0]}")

    if userScore == 0 or computerScore == 0 or userScore > 21:
        playing = False  #TODO: This line control the While Loop

    else:
        userDeal = input("Type 'y' to get another card, type 'n' to pass: ")
        if userDeal == "y":
            user_card.insert(2,random_card()) # I can also use .append here like .append(random_card())
            print(user_card)
        else:
            playing = False #TODO: This line control the while loop

## The while loop above is only for user to keep drawingcards so we need to create one for computer

## the readon != 0 was added is if the computer score is == 0 the ocmputer has a blackjack and the computer win so the game is ended
while computerScore != 0 and computerScore < 17:
    computer_card.append(random_card())
    computerScore = calculate_score(computer_card)

print(compare(userScore, computerScore))
