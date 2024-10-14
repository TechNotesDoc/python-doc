
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


class child(base):
   value="child_public"
   __value1 = "child_private"
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __child_fun_private(self):
      print("child_fun_private")
   def child_fun_public(self):
      print("child_fun_public")


      
if __name__ == '__main__':
   print('python2 run')        # 自己运行的时候执行这里
else:
   print('I am from import')   # 别的模块导入该模块的时候执行这里
