def UnderConstruction(func):
    def wrapper(self, *args, **kwargs):
        print(f"UNDER CONSTRUCTION > The function \"{func.__name__}()\" is under construction!")
        result = func(self, *args, **kwargs)
        print("UNDER CONSTRUCTION > Please ignore any faulty output.")
        return result
    return wrapper