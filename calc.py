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
    sys.argv[1] = drink_abv
    sys.argv[2] = drink_volume

  elif len(sys.argv) == 4:
    print("3 args provided, attempting to calulate price...\n")

  else:
    print("unsupported number of arguments provided")
    sys.exit(1)


def get_alc_content(percentage,volume):
  print("unfinished method: will calculate total alcohol content")


def get_price(percentage,volume,price):
  print("unfinished method: will calculate price per unit of alcohol")




def main():
  # main program logic

  # Check if at least 2 args provided
  check_args()

if __name__ == '__main__':
  main()