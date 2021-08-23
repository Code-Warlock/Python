""" Algorithm for Max CGPA"""
from time import sleep
try:
    # Create the empty lists
    cgpas = list()
    # Make the list dynamic by collecting the length
    length = int(input("Enter the no of cgpas to add : "))
    # Make sure the length of the list is greater than or equal to 1
    if length >= 1:
        # Accepting all the values on 1 line...And converting them to float items in the array(list!🤷‍♀️)
        values = input("Enter the cgpas(separate multiple values with a space ) : ").strip()
        values = values.split()
        for each in values:
            try:
                cgpas.append(float(each))
                # Making sure the items in the list do no exceed the initial definition by the user.
                cgpas = cgpas[:int(length)]
                # Well you should know what except blocks do😂
                # No time....
            except ValueError:
                print("Did not add non-integer values to the cgpas list")
                continue
            except KeyboardInterrupt:
                print("\nClosing...")
                sleep(2)
                print("Program Closed!")
            except Exception as e:
                raise e
    # Printing out the values in the cgpas array(list) just for display reasons... That's all
    print(cgpas)
    try:
        # Max Algo and code
        maximum_cgpa = max(cgpas)
        # End of Max CGPA code
        # Second-to-Max Algorithm
        new = cgpas.copy()
        x = maximum_cgpa
        while x in new:
            new.remove(x)
        next_maximum_cgpa = max(new)
       # End of Second-Max CGPA  code
    except Exception as e:
        raise e
    print(f"Maximum CGPA ===> {maximum_cgpa}\n2nd Maximum CGPA ====> {next_maximum_cgpa}")
except ValueError:
    print("Invalid Integer value!")
except KeyboardInterrupt:
    print("\nClosing...")
    sleep(2)
    print("Program Closed!")
except Exception as e:
    raise e
