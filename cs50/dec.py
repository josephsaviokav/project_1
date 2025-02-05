def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print('Done with function')
        return wrapper
@announce
def hello():
    print("Hello world")
#people.sort(key=lamda person:people['name']) where people is a dictionary which cintain name as keys 