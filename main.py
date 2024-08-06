from mastermind import MasterMind

if __name__ == "__main__":
    length = 4
    colors = ["green", "red", "yellow", "blue"]
    master = MasterMind(colors, length)
    master.play()
