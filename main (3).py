#2.2Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.


class Player:

  def play(self):
    print("The player is playing cricket.")


class Batsman(Player):

  def play(self):
    print("The batsman is batting.")


class Bowler(Player):

  def play(self):
    print("The bowler is bowling.")


if __name__ == "__main__":
  while True:
    print("Choose a player type:")
    print("1. Batsman")
    print("2. Bowler")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
      batsman = Batsman()
      batsman.play()
    elif choice == "2":
      bowler = Bowler()
      bowler.play()
    elif choice == "3":
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please select a valid option.")
