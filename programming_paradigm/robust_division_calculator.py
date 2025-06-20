def safe_divide(numerator, denominator):
  try:
    numerator = float(numerator)
    denominator = float(denominator)
    result = numerator / denominator
    return result
  
  except ValueError:
    return "Error: Both inputs must be numeric."
  
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."

