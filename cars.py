def select():
    print   ("\n--------------------------------------------------------");
    cylinders = input("Welcome, insert the minimun cylinders: ");
    
    MPG = input("\nInsert the minimun mile Per Gallons: ")

    HP = input("\nInsert the minumun HorsePower: ");
    
    return cylinders, MPG, HP;


def search(cylinders, MPG, HP, file):
    found = True;
    info = [];

    for line in file:
        value = line.split(";");
        if value[0] != "Car":
            if value[1] >= MPG and value[2] >= cylinders and value[4] >= HP:
                info.append(value);
                found = True;

    return found, info;

def result(found, info):
    if found: 
        print("There are {} results:" .format(len(info)));
        i = 1;

        for item in info:
            print("\n-----------Result {}----------\n" .format(i));
            print("Car: {}" .format(item[0]));
            print("Mile per Gallons: {}" .format(item[1]));
            print("Cylinders: {}" .format(item[2]));
            print("HorsePower: {}" .format(item[4]));
            print("Weight: {}" .format(item[5]));
            print("Acceleretion: {}" .format(item[6]));
            print("Origin: {}" .format(item[8]));

            i +=1;
    else:
        print("\nNo result!");

def main():
    file = open("cars.csv", "r");

    cylinders, MPG, HP = select();
    found, info = search(cylinders, MPG, HP, file);
    result(found, info);

main();