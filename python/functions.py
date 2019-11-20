#1

def double_it(number):
    return number * 2

print(double_it(5))
print(double_it(4.5))
print(double_it('hi'))

#2

def calc_hypo(a, b):
    if type(a) not in (int,float) or type(b) not in (int,float): 
        return 'Bad argument'
    if a <= 0 or b <= 0 :
        return 'Bad argument'
    hypo = (a**2 + b**2)**0.5
    return hypo

print(calc_hypo(3, 4))
print(calc_hypo('hi', 4))
print(calc_hypo(3, 'hi'))
print(calc_hypo(-3, 4))

