#1
lst = [1, 2, 3, 6, 10]

lst1 = tuple(lst)
print(lst1, type(lst1))


#2
tp1 = (1, 2)
tp2 = (3, 4)

tp3 = tp1 + tp2
print(tp3)


#3
def tulpe_reverse(tp1):
    return tp1[::-1]

tp1 = (1, 2, 3, 4)
print(tulpe_reverse(tp1))

#4
def length_tuple(tp1):
    return len(tp1)

tp1 = (1, 2, 3, 4)
print(length_tuple(tp1))


#5
tp1 = (10, 20, 30)
a, b, c = tp1
print(a, b, c)



#6
def dict3(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
print(dict3(dict1, dict2))    


#7
dicts = {'a':1, "b":2}
result = dicts['b']
print(result)


#8
def dicts_key(dict1, key):
    return key in dict1
dict1 = {'a':1, 'b':2}
print(dicts_key(dict1, 'b'))
print(dicts_key(dict1, 'c'))

#9
dict ={'a':1, 'b':2}
for key, value in dict.items():
    print(key, value)


#10
def swap_key_values(dicts):
    return {v: k for k, v in dicts.items()}
dicts = {'a':1, 'b':2}
print(swap_key_values(dicts))

#11
def divided_number(a, b):

    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    
print(divided_number(10, 2))
print(divided_number(10, 0))


#12
def multiple_exceptions(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError) as e:
        return f"An error occured: {e}"
    
print(multiple_exceptions(10, 0))    
print(multiple_exceptions(10, 'a'))

#13
class BigLasCodeIntegerError(Exception):
    pass

def positive_integer(n):
    if not isinstance(n, int) or n <= 0:
        raise BigLasCodeIntegerError("The input is not a positive integer")
    return True

try:
    print(positive_integer(10))
    print(positive_integer(-5))
except BigLasCodeIntegerError as e:
    print(e)    


#14
def access_safe(dict, key, default=None):
    return dict.get(key, default)

dict = {'a':1, 'b':2}    
print(access_safe(dict, 'b'))
print(access_safe(dict, 'c', 'default_value'))


#15
def last_finally():
    try:
        print("Try block")
    except Exception as e:
        print(f"Exception: {e}")    
    finally:
        print("This block alwaysm excutes")    


last_finally()        
