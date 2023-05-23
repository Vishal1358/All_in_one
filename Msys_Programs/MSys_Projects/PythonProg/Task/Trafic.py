def traffic_signals(function):
    def message():
        print("hi all")
        function()
        print("follow rules")
    return message

@traffic_signals
def red():
   		print("red : STOP")

@traffic_signals
def yellow():
   		print("yellow : SLOWDOWN")

@traffic_signals
def green():
   		print("green : GO")

red()
yellow()
green()
