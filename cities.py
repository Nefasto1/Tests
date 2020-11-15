def select():
    print   ("\n---------------------------------------------------------------")
    city = input("Welcome, insert the name of the city you're looking for: ").upper();
    
    return city;


def search(city, file):
    found = False;
    info = [];
    
    for line in file:
        value = line.split(",");
        if value[0][1:-1] != "LatD":
            if value[8].upper()[2:-1] == city:
                info = value;
                found = True;
    
    return found, info;

def result(found, info):
    if found:
        print("\nFound it:");
        print("\nCity name: {}" .format(info[8][2:-1]));
        print("State: {}" .format(info[9][0:-1]));
        print("Latitude: {}°{}'{}\"" .format(info[0], info[1], info[2]));
        print("Longitude: {}°{}'{}\"" .format(info[4], info[5], info[6]));
    else:
        print("\nNot found!");

def main():
    file = open("cities.csv", "r");

    city = select();
    found, info = search(city, file);
    result(found, info);

main();