import yaml


class YamlSerialization:
    @staticmethod
    def upd_file(func):
        """
        decorator for reading from .yaml file
        :param func:
        :return:
        """

        def wrapper(product, data, calories):
            """

            :param product:
            :param data:
            :param calories:
            :return:calories if need

            >>> from io import StringIO
            >>> with open('data.yaml', 'r') as f:
                    data = yaml.load(f)
            >>> file = open ('data.yaml', 'r')
            >>> st  = file.read()
            >>> file = StringIO(st)
            >>> st2 = file.getvalue(st)
            >>> return st==st2



            """
            with open('data.yaml', 'r') as f:
                data = yaml.load(f)
            calories = func(product, data, calories)
            with open('data.yaml', 'w') as f:
                yaml.dump(data, f)
            return calories

        return wrapper
