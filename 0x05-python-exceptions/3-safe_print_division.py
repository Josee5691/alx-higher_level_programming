def safe_print_division(a, b):
    try:
        result = a / b  # Attempt the division
    except ZeroDivisionError:
        # Handle division by zero
        return None
    except Exception as e:
        # Handle other exceptions
        return None
    finally:
        # Print the result or 'None' if there was an error
        print("Inside result: {}".format(result if result is not None else 'None'))
    
    return result
