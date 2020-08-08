import random

def run():
    
    f = open("quotes.txt")
    quotes = f.readlines()
    last = len(quotes)
    rnd = random.sample(range(0,last),2)  #generates multiple quotes randomly
    f.close()

    print(quotes[rnd[0]],end='')
    print(quotes[rnd[1]])

if __name__== "__main__":
  run()
