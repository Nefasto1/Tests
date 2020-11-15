def select():
    print   ("\n---------------------------------------------------------------");
    period = input("Welcome, insert the period: ");
    
    a = input("\nIs a birth? (Yes/No): ").upper();
    while a != "YES" and a != "NO":
        print("\n\nInsert a valid answer!!!");
        a = input("\nIs a birth? (Yes/No): ").upper();
    if a == "YES":
        state = "Births";
    else:
        state = "Deaths";
    
    min = input("\nInsert the minor value: ");
    
    return period, state, min;


def search(period, state, min, file):
    found = True;
    info = [];

    for line in file:
        value = line.split(",");
        if value[0] != "Period":
            
            if value[0] == period and value[1] == state and value[3] >= min:
                info.append(value);
                found = True;

    return found, info;

def result(found, info):
    if found: 
        print("There are {} results:" .format(len(info)));
        i = 1;

        for item in info:
            print("\n-----------Result {}----------\n" .format(i));
            print("Period: {}" .format(item[0]));
            print("Type: {}" .format(item[1]));
            print("Region: {}" .format(item[2]));
            print("Count: {}" .format(item[3]));

            i +=1;
    else:
        print("\nNo result!");

def main():
    file = open("birthDeath.csv", "r");

    period, state, min = select();
    found, info = search(period, state, min, file);
    result(found, info);

main();