def get_int(prompt = "Please enter an integer", errorMessage = "That was not an Integer. Please enter an integer", min = None, max = None):
    while True:
        try:
            num = int(input(prompt))
            #check if min is set
            if min != None:
                if num < min:
                    #num is too small
                    raise ValueError(f"Input must at least {min}")
            
            
            #check if max is set
            if max != None:
                if num > max:
                    #num is too big
                    raise Exception(f"Input must at most {max}")
           
            break
        except ValueError:
            #input is not an integer
            print(errorMessage)
        except Exception as e:
            #one of the min or max tests failed
            print(e)
    return num
