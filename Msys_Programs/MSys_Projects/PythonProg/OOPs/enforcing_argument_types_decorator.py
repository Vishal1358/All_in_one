def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            newarg = []
            for (a, t) in zip(args, types):
                newarg.append(t(a))
            return f(*newarg, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def devide(a, b):
    print(a/b)

repeat_msg("hello", '5')
devide("1", "4")
