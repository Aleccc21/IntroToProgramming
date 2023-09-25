#Example program that converts miles to kilometers

def main():
    #Display the intro screen
    intro()

    try:
  #Get number of miles
      miles_needed = float(input("Enter the number of miles: "))
  # Convert miles to kilometers
      miles_to_kilometers(miles_needed)
    except:
      print("An execption occured, try again by entering only a number")
      print()
      main()
      
#The intro function displays an intro screen
def intro():
    print('This program converts measurments')
    print('in miles to kilometers. For your')
    print('refrence the formula is:')
    print(' 1 miles = 1.60934 kilometers')
    print()

#The miles_to_kilometers accepts a number of miles and 
#displays the equivelent number of kilometers
def miles_to_kilometers(miles):
  kilometers = miles * 1.60934
  print('That converts to', kilometers, 'kilometers')
  print('Converted from', miles, 'miles')
#call the main function
main()