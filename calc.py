#!/usr/bin/env python3
import sys


# Help Text
def print_help():
  print("\tProgram Usage:")
  print("\tGet total alcohol content:")
  print("\t#",sys.argv[0],"[ABV%] [DRINK VOLUME]\n")
  print("\tGet price per unit of alcohol in drink:")
  print("\t#",sys.argv[0],"[ABV%] [DRINK VOLUME] [PRICE]\n")


# Verify arguments are provided properly
def check_args():
  if len(sys.argv) < 3:
    print("Too few arguments provided...\n\n")
    print_help()
    sys.exit(1)
  elif len(sys.argv) == 3:
    print("2 args provided, attempting to calulate alcohol content...\n")
    return(3)
  elif len(sys.argv) == 4:
    print("3 args provided, attempting to calulate price...\n")
    return(4)
  else:
    print("unsupported number of arguments provided")
    sys.exit(1)



def get_alc_content(percentage,volume):
  print("%s%% * %s" % (percentage,volume))
  percentage = percentage/100
  total = percentage*volume
  # print("total alcohol in drink is: %s" % (total))
  return(total)

def get_price(percentage,volume,price):
  total = get_alc_content(percentage,volume)
  cost = total/price
  print("Price per unit:\t", '${:,.2f}'.format(cost))


def main():
  # main program logic
  # Check if at least 2 args provided
  ret = check_args()
  if ret == 3:
    abv = float(sys.argv[1]) * 1
    volume = int(sys.argv[2])
    amount = get_alc_content(abv,volume)
    print("Total alcohol in beverage: ", amount)
  if ret == 4:
    abv = float(sys.argv[1]) * 1
    volume = int(sys.argv[2])
    price = float(sys.argv[3])
    get_price(abv,volume,price)


if __name__ == '__main__':
  main()