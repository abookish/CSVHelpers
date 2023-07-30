'''
assumptions: 
1. csv format, all values strings
    first column: dates in a month/day/year format
    second column: money values
    fifth column: descriptions
2. csv located in same dir
'''
if __name__ == "__main__":
    import csv
    import sys
    def formatMoneyString(floatValue, makeAbsolute = True):
        valueToUse = abs(floatValue) if makeAbsolute else floatValue
        return "$" + "%.2f" % round(valueToUse,2)
        

    ##get user input
   
    #month filter ask
    print('Want to filter by month? (y/n): ')
    monthFilter = True if input().upper() == "Y" else False
    print("enter month number: " if monthFilter else "Okay.")
    monthNum = int(input()) if monthFilter else None
    #keywordAsk
    print('Want to search by keyword? (y/n): ')
    wantsSearch = True if input().upper() == "Y" else False
    print("Enter keyword" if wantsSearch else "Okay, here are your totals")
    keyword = input() if wantsSearch else None

    #get csv
    with open('test.csv', newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        monthData = False
        totalSum = 0
        keywordSum = 0 
        keywordCount = 0
        mostExpensiveCost = 0
        mostExpensiveDesc = ''
        #repeated methods
        def incrementMostExpensive():
            global mostExpensiveCost
            global mostExpensiveDesc
            if amount < mostExpensiveCost:
                mostExpensiveCost = amount
                mostExpensiveDesc = description
        def incrementKeywordCounts(keywordToSearch):
            if keywordToSearch.lower() in description.lower():
                    global keywordSum, keywordCount
                    keywordSum += amount
                    keywordCount +=1
        def incrementAllCounts(keywordToSearch):
            global totalSum           
            totalSum += amount 
            incrementMostExpensive()
            if wantsSearch:
                incrementKeywordCounts(keyword)
        #time to count
        for row in reader:
            date, amount, description = row[0], float(row[1]), row[4]
            months = int(date.split("/")[0])
        
            if monthFilter:
                if int(months) == monthNum:
                    monthData = True
                    incrementAllCounts(keyword)
            else:
                incrementAllCounts(keyword)
                
    #output                 
    changeDescription = "loss" if totalSum < 0 else "gain"
    totalString = "End of the month total" if monthFilter else "Total"
    monthString = ' this month' if monthFilter else ''
    if monthFilter and not monthData:
        print("no data for this month")
    else:
        #total data
        if totalSum == 0: print(f"You broke even{monthString}") 
        else: print(f"{totalString}: {formatMoneyString(totalSum, False)} \nYou had a net {changeDescription}{monthString}.")
       #specific purchases
        if wantsSearch:
            if keywordCount == 0:
                print (f"You had no {keyword} purchases{monthString}.")
            else: 
                print(f"You had {keywordCount} {keyword} purchases{monthString}, totalling {formatMoneyString(keywordSum)} with an average cost of {formatMoneyString(keywordSum/keywordCount)}.") 
        print(f"Most expensive purchase{monthString}: " + mostExpensiveDesc, "which cost " + formatMoneyString(mostExpensiveCost))

