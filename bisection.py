import math
import decimal


def get_length(interval):
    return decimal.Decimal((interval[1] - interval[0]))


def split_interval(interval):
    left = decimal.Decimal(interval[0])
    right = decimal.Decimal(interval[1])
    interval_length = decimal.Decimal(get_length(interval))
    if not (fun(left) * fun(right)) < 0:
        print ("Error, choosen interval is wrong.")
        return False

    split_point = decimal.Decimal(( left + (interval_length / 2) ))

    if (fun(left) * fun(split_point)) < 0:
        return [left,split_point]
    elif (fun(split_point) * fun(right)) < 0:
        return [split_point, right]
    else:
        print ('Error, none of the intervals is valid.')
        return False


def run_bisection(interval, target_length):
    interval_length = decimal.Decimal(get_length(interval))
    while interval_length > target_length:
        interval = split_interval(interval)
        if not interval:
            print ("Function returned False! (spliting the interval)")
            return False
        interval_length = get_length(interval)
        print ("=========\n New interval size %f" % interval_length)
        print (" New interval [%f : %f]" % (interval[0], interval[1]))

    print ("\n\n|-+-+-+-+-+-+-+-+-+-| \n\n  Result: [%f : %f]" % (interval[0], interval[1]))


# ===== Example functions ======

# Function x^2 - x - 20
def fun2(x):
    return math.pow(x,2) - x - 20
# Function x^3 + 2x^2 + 43
def fun3(x):
    return (math.pow(x,3)) + (2 * math.pow(x,2)) + 43
# Function 10x^5+40x^5+82x^3+91x^2+52x+13
def fun(x):
    return (10*pow(x,5)) + (40*pow(x,5)) + (82*pow(x,3)) + (91*pow(x,2)) + (52*x) + 13

# ===== Config =====
interval = [-50.0, 50.0] # Search interval
length = decimal.Decimal('0.00001') # Error size

# ==== Uruchomienie =====
run_bisection(interval, length)
