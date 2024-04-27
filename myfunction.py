def hello():
    print("hello mama")
    print("how are you")

def hello1(name):
    print(f"hello {name}")
    print("how are you?")

hello1("Dylan")


def Command(cmd):
    import os
    os.system(cmd)

Command('ls')