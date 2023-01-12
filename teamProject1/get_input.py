def get_int(prompt = "Please enter an integer", errorMessage = "That was not an Integer. Please enter an integer", min = None, max = None):
    while True:
        try:
            num = int(input(prompt))
            #check if min is set
            try:
                #is min is the default value, this will raise a valueError
                int(min)
                if num < min:
                    #num is too small
                    raise Exception(f"Input must at least {min}")
            except ValueError:
                #min was not set
                pass
            
            #check if max is set
            try:
                #if max is the default value, this will raise a valueError
                int(max)
                if num > max:
                    #num is too big
                    raise Exception(f"Input must at most {max}")
            except ValueError:
                #max was not set
                pass
            #if now errors are raised by this point, the input is valid
            break
        except ValueError:
            #input is not an integer
            print(errorMessage)
        except Exception as e:
            #one of the min or max tests failed
            print(e)
    return num
