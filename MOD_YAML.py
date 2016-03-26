import yaml


def upd_file(func):
    """
    decorator for readig from .yaml file
    :param func:
    :return:
    """
    def wrapper(product, data, calories):
        with open('data.yaml', 'r') as f:
            data = yaml.load(f)
        calories = func(product, data, calories)
        with open('data.yaml', 'w') as f:
            yaml.dump(data, f)
        return calories
    return wrapper