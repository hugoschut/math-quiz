# Leaderboards
# made by Hugo Schutte
# 17 May 2024

# Leaderboard to manage the scores
class Leaderboard:
  def __init__(self):
    # Initialise an empty list to store tuples of name and score
    self.scores = []

  def add_score(self, name, score):
    # Add the (name, score) tuple to the list
    self.scores.append((name, score))
    # Sort the list in place by score in descending order
    self.scores.sort(key=lambda x: x[1], reverse=True)

  def display(self):
    # Print the leaderboard title
    print("Leaderboard:")
    # Enumerate through the sorted list and print each entry
    for rank, (name, score) in enumerate(self.scores, start=1):
      print(f"{rank}. {name}: {score}")


def main():
  # Create an instance of the Leaderboard class
  leaderboard = Leaderboard()

  # Infinite loop to continually ask for user input
  while True:
    # Prompt the user for a name
    name = input("Enter name (or 'quit' to exit): ")
    # Check if the user wants to quit the program
    if name.lower() == 'quit':
      break
    # Prompt the user for a score
    try:
      score = int(input("Enter score: "))
    except ValueError:
      # Handle the case where the input is not an integer
      print("Invalid score, please enter an integer.")
      continue
    # Add the name and score to the leaderboard
    leaderboard.add_score(name, score)
    # Display the updated leaderboard
    leaderboard.display()


# Ensure the main function runs only when this script is executed directly
if __name__ == "__main__":
  main()