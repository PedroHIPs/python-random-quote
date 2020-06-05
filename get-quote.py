import random;

def initial():
  #print("Keep it logically awesome.")

  i = int(1)
  f = open("quotes.txt", "a")
  f.write("Now the file has more quotes!")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  
  rnd = random.randint(0, last);
  Newrnd = random.randint(0, last);

  print(quotes[rnd],quotes[Newrnd])


if __name__== "__main__":
  initial()
