# global scope
global_var= 'I am a global scope'
def access_global_var():
    print(global_var)
access_global_var()

# local scope
def function_with_local_var():
    local_var = "I am a local variable"
    print(local_var)
function_with_local_var()