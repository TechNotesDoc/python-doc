
class base:
   value="base_public"
   __value1 = "base_private"
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __base_fun_private(self):
      print("base_fun_private")
   def base_fun_public(self):
      print("base_fun_public")

my_base1  = base(1,2)
my_base2  = base(3,4)
print(base.value)
print(my_base1.value)
my_base1.value="changed value "
print(my_base1.value)
print(my_base2.value)
print(base.value)

class child(base):
   value="child_public"
   __value1 = "child_private"
   def __init__(self, a, b):
      self.a = a
      self.b = b
      base.__init__(self,a,b)

   def __child_fun_private(self):
      print("child_fun_private")
   def child_fun_public(self):
      print("child_fun_public")



my_child = child(3,4)





if __name__ == '__main__':
   pass        # 自己运行的时候执行这里
else:
   print('I am from import')   # 别的模块导入该模块的时候执行这里
