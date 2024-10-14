
global_immutable = ["global_immutable1","global_immutable2"]



def fun():
   #在函数中尝试修改全局的可变变量
   global_immutable[0]="print1 global_immutable1"
   print(f"fun in :{global_immutable} id={id(global_immutable)}")

print("============================ before change ==================")
print(f"fun out :{global_immutable} id={id(global_immutable)}")
print("=============================================================")

fun()
print("===========================after change =======================")
print(f"fun out :{global_immutable} id={id(global_immutable)}")
 
