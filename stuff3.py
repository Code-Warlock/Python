from time import sleep
def create_list():
    try:
        cgpas = list()
        length = int(input("Enter the no of cgpas to add : "))
        if length >= 1:
            values = input("Enter the cgpas(separate multiple values with a space ) : ").strip()
            values = values.split()
            for each in values:
                try:
                    cgpas.append(float(each))
                    cgpas = cgpas[:int(length)]
                except ValueError:
                    print("Did not add non-integer values to the cgpas list")
                    continue
                except KeyboardInterrupt:
                    print("\nClosing...")
                    sleep(2)
                    print("Program Closed!")
                except Exception as e:
                    raise e

        return cgpas

    except ValueError:
        print("Invalid Integer value!")
    except KeyboardInterrupt:
        print("\nClosing...")
        sleep(2)
        print("Program Closed!")
    except Exception as e:
        raise e
create_list()
