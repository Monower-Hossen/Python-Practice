'''2. Write a python program using function to convert Celsius to Fahrenheit. '''

def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit.

  Args:
    celsius: The temperature in Celsius.

  Returns:
    The temperature in Fahrenheit.
  """

  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Get input from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the function
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print("The temperature in Fahrenheit is:", fahrenheit)

