def select():
    print("\n-------------------------------------------------\n");
    print("Data: \n");
    gg = input("Giorno: ");
    mm = input("Mese: ");
    aa = input("Anno: ");

    data = [gg, mm, aa];

    return data;


def search(data, file):
    found = False;
    info = [];
    
    for line in file:
        dati = line.split(",");
    
        if dati[0] != "data":
            value = dati[0].split(";");
            value = value[0].split("-");

            if value[0] == data[2] and value[1] == data[1] and value[2] == data[0]:
                info = dati;
                found = True;
    
    return found, info;

def result(found, data, info):
    if found:
        print("\n---------------------------------------------\n");
        print("\nDati relativi al {}/{}/{}" .format(data[0], data[1], data[2]));
        print("Ricoverati con Sintomi: {}" .format(info[2]));
        print("Terapia Intensiva: {}" .format(info[3]));
        print("Totale Isolamento Domiciliare: {}" .format(info[5]));
        print("Totale Positivi: {}" .format(info[6]));
        print("Dimessi guariti: {}" .format(info[9]));
        print("Deceduti: {}" .format(info[10]));
        print("Nuovi Positivi: {}" .format(info[8]));
        print("Casi da Sospetto Diagnostico: {}" .format(info[11]));
        print("Casi da Screening: {}" .format(info[12]));
        print("Casi Totali: {}" .format(info[15]));
        print("Totale Casi Testati: {}" .format(info[13]));
        print("Tamponi: {}" .format(info[14]));
    else:
        print("\nDati NON Trovati\n");

def main():
    file = open("covidItalia.csv", "r");

    data = select();
    found, info = search(data, file);
    result(found, data, info);

    file.close();

while True:
    main();