import random

def run():
    
    f = open("quotes.txt")
    quotes = f.readlines()
    last = 13
    rnd = random.randint(0,last)
    f.close()

    print(quotes[rnd])

if __name__== "__main__":
  run()
