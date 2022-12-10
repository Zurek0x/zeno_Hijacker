import Zeno # Import Zeno Script into Code
import multiprocessing # Import multiprocessing to start script as thread
import time # To delay the test script ()

class process_handle():
    def Start_Zeno(): # Run as background process
        Zeno.setup_idenf.start()
    def Run_Code(): # Run as main code to execute
        s=int(1)
        while True:
            time.sleep(0.3) 
            s=s+1
            print(s)
        # Loop is to test running code while process thread is in background

if __name__=="__main__":
    p = multiprocessing.Process(target=process_handle.Start_Zeno) # Define thread to variable
    p.start() # Execute thread through variable (Call Function)
    # =/?/= #
    s = multiprocessing.Process(target=process_handle.Run_Code) # Define thread to variable
    s.start() # Execute thread through variable (Call Function)