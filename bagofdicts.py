import csv
def main():
    try:
        dictionary = bag_of_dicts(input("Enter .csv address: "))
        print(dictionary)
    except:
        print("File Did Not Open")
    
def bag_of_dicts(filename):
    bag = {}
    for dicts in csv.reader(open(filename)):
        key = int(dicts[0])
        length = dicts[1]
        width = dicts[2]
        # additional dicts if .csv requires 
        bag[key] = {"length" : length, "width" : width}
    return bag    
main()