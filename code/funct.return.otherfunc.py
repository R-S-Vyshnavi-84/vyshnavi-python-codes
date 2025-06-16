def disp():
         def show():
                 return "show function"
         print("disp function")
         return show
r_sh = disp()
print(r_sh())