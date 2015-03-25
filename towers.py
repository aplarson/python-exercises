class Towers:
    def __init__(self):
        self.stacks = [[3, 2, 1], [], []]
    def won(self):
        return len(self.stacks[1]) == 3 or len(self.stacks[2]) == 3
    def move(self, source, dest):
        if self.stacks[dest] and self.stacks[source][-1] > self.stacks[dest][-1]:
            return False
        else:
            self.stacks[dest].append(self.stacks[source].pop())
            return True
    def get_move(self):
        print("Enter a tower to move from")
        source = int(input())
        print("Enter a tower to move to")
        dest = int(input())
        return [source, dest]
    def play(self):
        while(not self.won()):
            print(self.stacks)
            next_move = self.get_move()
            self.move(next_move[0], next_move[1])
        print("You win!")

Towers().play()
