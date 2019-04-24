class Data_test2(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data_as_string):
        # 这里第一个参数是cls， 表示调用当前的类名
        year, month, day = map(int, data_as_string.split('-'))
        date1 = cls(year, month, day)
        cls.__out_date__
        # 返回的是一个初始化后的类
        return date1

    def out_date(self):
        print('操', self.year)


r = Data_test2.get_date("2016-8-6")
