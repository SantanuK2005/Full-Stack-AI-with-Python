class OutOfIngredientsError(Exception):
    pass

def make_chai(mlik, suger):
    if mlik ==0 or suger ==0:
        raise OutOfIngredientsError("Milk or sugar cannot be zero!")
    print("chai is ready...")

make_chai(1, 0)