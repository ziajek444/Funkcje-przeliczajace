
#include <iostream>
#include <math.h>

using namespace std;

double stopnieToRad(double stop){
    const double Pi = 3.14;
    return (stop * Pi)/180;
}

double WilToDegre(double Wilgotnosc)
{
    // 0-90 stopni = 0-30 procent wilgotnosci
    // 90-180 stopni = 30-80 procent wilgotnosci
    // 180-270 stopni = 8-100 procent wilgotnosci
    // wiecej niz 100% lub mniej niz 0% wilgotnosci to blad

    double ret = 0;
    float a1 = 1.8;
    float b1 = 36;
    float a2 = 4.5;
    float b2 = -180;

    if(Wilgotnosc < 0.0 || Wilgotnosc > 100.0) { printf("\nZle paramtery wejsciowe wilgoci\n(dopuszczlane 0-100)\n"); return -1; }
    else
    {
        if(Wilgotnosc < 30.0) ret = Wilgotnosc * 3;
        else if (Wilgotnosc < 80.0) ret = (Wilgotnosc*a1) + b1;
        else ret = (Wilgotnosc*a2) + b2;
    }

    return abs(sin(stopnieToRad(ret)));
}

double ZagrorzenieCal(double Temperatura, double SilaWiatru, double Cisnienie, double Wilgotnosc, bool debug = 0)
{
    double ZAGROZENIE;
    // warunki
    if(Temperatura < 15.0) {
            printf("Za zimno, zagrozenie ponad skale !!\n");
            return 100.0;
    }
    if(SilaWiatru > 20.0) {
            printf("Za mocny wiatr, zagrozenie ponad skale !!\n");
            return 100.0;
    }
    if(Cisnienie < 700.0) {
            printf("Za niskie cisnienie, zagrozenie ponad skale !!\n");
            return 100.0;
    }
    if(Wilgotnosc < 30.0) {
            printf("Za suche powietrze, zagrozenie ponad skale !!\n");
            return 100.0;
    }
    if(Wilgotnosc > 80.0) {
            printf("Powietrze zbyt wilgotne, zagrozenie ponad skale !!\n");
            return 100.0;
    }

    // wzór -> zagrozenie = ( 50000SW * sqrt(Wilgotnosc) ) / ( Temperatura^2 * (cisnienie/10) )

    SilaWiatru *= 50000;
    Wilgotnosc = sqrt((WilToDegre(Wilgotnosc)));
    Temperatura *= Temperatura;
    Cisnienie /= 10;

    double debugLicznik = (SilaWiatru*Wilgotnosc);
    double debugMianownik = (Temperatura*Cisnienie);
    ZAGROZENIE = debugLicznik/debugMianownik;

    if(debug)
    {
        cout<<"SilaWiatru: "<<SilaWiatru<<endl;
        cout<<"Wilgoc przelcznik: "<<Wilgotnosc<<endl;
        cout<<"licznik: "<<debugLicznik<<endl;

        cout<<endl;

        cout<<"Temperatura: "<<Temperatura<<endl;
        cout<<"Cisnienie: "<<Cisnienie<<endl;
        cout<<"mianownik: "<<debugMianownik<<endl;

        cout<<endl;

        cout<<"ZAGROZENIE w funkcji: "<<ZAGROZENIE<<endl;
    }

    return ZAGROZENIE;
}

int main()
{
    double Temperatura; // Mniej niż 15 -> ŹLE
    double SilaWiatru; // Wiecej niz 20m/s -> ŹLE
    // kierunek wiatru nie ma znaczenia dla zagraożenia
    double Cisnienie; // Mniej niz 700 Hpa -> ŹLE
    double Wilgotnosc; // Mniej niz 30% ŹLE AND Więcej niż 80% -> ŹLE

    double Zagr = 0;

    //Zagr = ZagrorzenieCal(Temperatura, SilaWiatru, Cisnienie, Wilgotnosc);
    cout<<"SilaWiatru testy\n";
    for(SilaWiatru = 0.0; SilaWiatru<13.0; SilaWiatru++) {
        Zagr = ZagrorzenieCal(26.0, SilaWiatru, 1000.0, 50.0);
        printf("[%.1f] Zagr: %F\n",SilaWiatru,Zagr);
    }
    cout<<"Temperatura testy\n";
    for(Temperatura = 15.0; Temperatura<27.0; Temperatura++) {
        Zagr = ZagrorzenieCal(Temperatura, 5.0, 1000.0, 50.0);
        printf("[%.1f] Zagr: %F\n",Temperatura,Zagr);
    }
    cout<<"Cisnienie testy\n";
    for(Cisnienie = 800.0; Cisnienie<1300.0; Cisnienie+=50) {
        Zagr = ZagrorzenieCal(20.0, 5.0, Cisnienie, 50.0);
        printf("[%.1f] Zagr: %F\n",Cisnienie,Zagr);
    }
    cout<<"Wilgotnosc testy\n";
    for(Wilgotnosc = 1.0; Wilgotnosc<100.0; Wilgotnosc+=11) {
        Zagr = ZagrorzenieCal(20.0, 5.0, 1000.0, Wilgotnosc);
        printf("[%.1f] Zagr: %F\n",Wilgotnosc,Zagr);
    }

    cout<<"Skrajnie zle warunki 1\n";
    Zagr = ZagrorzenieCal(15.0, 9.9, 800.0, 79.9,0);
    printf("Zagr: %F\n",Zagr);

    cout<<"Skrajnie zle warunki 2\n";
    Zagr = ZagrorzenieCal(30.0, 9.9, 800.0, 31.9,0);
    printf("Zagr: %F\n",Zagr);

    cout<<"Idealne warunki wilgoc 45%\n";
    Zagr = ZagrorzenieCal(24.0, 1.0, 1000.0, 45.0,0);
    printf("Zagr: %F\n",Zagr);

    cout<<"Idealne warunki wilgoc 60%\n";
    Zagr = ZagrorzenieCal(24.0, 1.0, 1000.0, 60.0,0);
    printf("Zagr: %F\n",Zagr);

    cout<<"Idealne warunki wilgoc 75%\n";
    Zagr = ZagrorzenieCal(24.0, 1.0, 1000.0, 75.0,0);
    printf("Zagr: %F\n",Zagr);

    // Jezeli zagrozenie jest wieksze od 1 to ni chuja w gory
    // jezeli jest mniejsze lub rónw 1 to ok :d

    return 0;
}
