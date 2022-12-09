import time
import Zeno_func as func

# =?/Settings/?= #
time_delay_per_scan = 0.2 # ?Seconds

cache = [""] # Cache (Do not touch this)
substring = ["Test1", "Test2"] # Run code if it finds this in clipboard
passString = ["Pasted"] # Do not run any code if "this" found in clipboard
class proc_handle():
    def func_reset():
        proc_handle.func()
    def func():
        while True:
            flag = int(0)
            flag2 = int(0)
            time.sleep(int(time_delay_per_scan))
            self = func.data_handle.read()
            if cache[0] == "":
                cache.append(self)
            # ?/Update-Cache/? #
            if self != cache[0]:
                cache.clear()
                cache.append(self)
                for i in passString:
                    if cache[0] == i:
                        flag=int(1)
                        flag2=int(1)
                if flag == int(1):
                    # Text found in passString #
                    print("Pass.PassString")
                else:
                    for x in range(len(substring)):
                        i = substring[x]
                        if self != None and i in cache[0]:
                            # Text Found Inside of Substring #
                            print(f"Detected.inString : {cache[0]}")
                            flag2=int(1)
                            # Add more of these "elif x == int(1)" for whatever you need to paste per list.
                            if x == int(0):
                                statement=str("Found_0_in_substring_List!")
                                func.data_handle.write(statement)
                                ## / print(statement)
                            elif x == int(1):
                                statement=str("Found_1_in_substring_List!")
                                func.data_handle.write(statement)
                                ## / print(statement)
                    if flag2==int(0):
                        # Text Not Found Inside of Substring #
                        print(f"Pass.NoReason")
                        flag=int(0)

            

class setup_idenf():
    def boot():
        proc_handle.func()

if __name__=="__main__":
    setup_idenf.boot()