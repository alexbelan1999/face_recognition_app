import pickle


def dump(object: list, name: str):
    path = "../pickle/" + name + ".pickle"
    with open(path, 'wb') as f1:
        pickle.dump(object, f1)
    pass


def load(name: str):
    path = "../pickle/" + name + ".pickle"
    with open(path, 'rb') as f:
        object = pickle.load(f)
    return object
