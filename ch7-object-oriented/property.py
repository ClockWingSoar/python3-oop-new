class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        # 格式的规范
        return self.__name.upper()

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        # 做一些合法性的检查
        self.__name = name
   # @name.setter 注意这里一定要写属性对应的名字，如果写错，比如这里age写成name，则调用age的时候会
   #返回name的结果
   #类似如下，正常 @age.setter应该是
   # PS C:\Users\214228672\Downloads\udemy\python3-oop-new\python3-soveran> & C:/Users/214228672/AppData/Local/Programs/Python/Python311/python.exe c:/Users/214228672/Downloads/udemy/python3-oop-new/python3-soveran/ch7-object-oriented/property.py
# JACK
# 20
# TEST
# 22
#如果是  @name.setter
# PS C:\Users\214228672\Downloads\udemy\python3-oop-new\python3-soveran> & C:/Users/214228672/AppData/Local/Programs/Python/Python311/python.exe c:/Users/214228672/Downloads/udemy/python3-oop-new/python3-soveran/ch7-object-oriented/property.py
# JACK
# JACK
# TEST
# TEST
    @age.setter
    def age(self,age):
        self.__age = age
    def set_age(self, age):
        self.__age = age


someone = People(name='Jack', age=20)
print(someone.name)
print(someone.age)
someone.name = 'Test'
print(someone.name)
someone.age = '22'
print(someone.age)
