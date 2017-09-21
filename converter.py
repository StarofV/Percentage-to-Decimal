def converter():
  try:
    user_input= float(input('Enter percentage: ').rstrip('%'))
    print(round(user_input/100,2))
  except ValueError:
    print("Please enter the percentage sign correctly.")
    converter()

if __name__ == '__main__':
  converter()
