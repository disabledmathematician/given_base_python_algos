import numpy as np
import scipy.stats as ss
import pandas as pd



""" Charles Thomas Wallace Truscott Watters Time Series and Binary Classifiers for Daily Activities and eventually Occupational Therapy. Began Oct 5 2023. Can't wait to use datetime objects """
def CharlesDailyPerformance():
	day = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
	hour = ["7 p.m.", "7:45 p.m.", "9:15 p.m.", "11:30 p.m.", "1 a.m.", "5 a.m.", "7:40 a.m.", "8:20 a.m.", "9:42 a.m", "11 a.m.", "5:21 p.m.", "5:41 p.m", "6:02 p.m.", "8:20 p.m.", "4:30 a.m.", "5:00 p.m", "5:30 p.m.", "6:00 p.m.", "7:17 p.m","9:21 p.m.", "10:15 p.m."]
	woke_bin = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
	teeth_bin = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
	combedhair_bin = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
	steamwashface = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]
	eatenmeal_bin = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0]
	soapinshower_bin = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
	coffee_sugar_bin = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0]
	went_to_sleep_bin = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
	what_meal = ["Chocolate Biscuits", None, "Diced Peaches in tub", "Soy Sauce and Fried Rice with Mushrooms and Chicken", None, None, None, "Instant Noodles (Chicken) and Toasted Cheese Sandwich on Sourdough Rye Bread", None, "Diced Peaches in tub and Passionfruit Juice", None, None, None, "Pork Spare Ribs and Rice", None, "Diced Peaches in Tub and Passionfruit Juice", None, "Two 28g bags of potato chips", "Cup of Earl Grey and Glass of Water", None, None]
	dried_clothes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	collected_clothes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	handwashed_clothes = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	performance = pd.DataFrame({"Day": day, "Hour": hour, "Woke up": woke_bin, "3 minutes toothpaste rinse": teeth_bin,"Combed hair": combedhair_bin, "Steamed and Washed Face": steamwashface, "Eaten meal": eatenmeal_bin, "Whole body soap wash five minutes in shower": soapinshower_bin, "Drank a cup of coffee with raw sugar": coffee_sugar_bin, "What meal?": what_meal, "Handwashed clothes in grated coal tar soap": handwashed_clothes, "Set clothes in the sun to dry": dried_clothes, "Collected sun-dried and pressed clothes": collected_clothes})
	print(performance)
	performance.to_csv('CharlesTruscottOccupationalPerformance.csv')
	for k in performance:
		print(performance[k])
		tL = []
		for n in performance[k]:
			if type(n) != type(str()) and type(n) != type(None):
				tL.append(n)
		if len(tL) != 0:
			print("Sum: {} Average: {} Variance: {} Standard Deviation: {}, Coefficient of Variation: {}".format(sum(tL), sum(tL) / len(tL), np.var(tL), np.std(tL), np.std(tL) / np.mean(tL)))
if __name__ == """__main__""": CharlesDailyPerformance()