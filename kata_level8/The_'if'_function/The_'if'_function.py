def _if(bool_val, func1, func2):
    if bool_val:
        func1()
    else:
        func2()

def truthy():
    print("True")

def falsey():
    print("False")
