import os


os.environ['VarHello'] = "874587"

env = os.getenv("VarHello", "Default Value")
print(env)