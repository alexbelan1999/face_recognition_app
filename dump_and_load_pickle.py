import pickle


def dump(object: list, name: str, number: int):
    path = ""
    if number == 0:
        path = "./pickle/encodings/" + name + ".pickle"

    if number == 1:
        path = "./pickle/names/" + name + ".pickle"

    with open(path, 'wb') as f1:
        pickle.dump(object, f1)
    pass


def load(name: str, number: int):
    path = ""
    if number == 0:
        path = "./pickle/encodings/" + name + ".pickle"

    if number == 1:
        path = "./pickle/names/" + name + ".pickle"
    with open(path, 'rb') as f:
        object = pickle.load(f)
    return object
