import pickle


def upd_file(func):
    """
    decorator for readig from .pickle file
    :param func:
    :return:
    """
    def wrapper(product, data, calories):
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        calories = func(product, data, calories)
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        return calories
    return wrapper