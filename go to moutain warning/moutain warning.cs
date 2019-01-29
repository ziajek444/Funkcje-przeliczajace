using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace moutain_warning
{
    class moutain_warning
    {
        public double ZagrorzenieCal(double Temperatura, double SilaWiatru, double Cisnienie, double Wilgotnosc, bool debug = false)
        {
            double ZAGROZENIE;
            // warunki
            if (Temperatura < 15.0F)
            {
                System.Console.Write("Za zimno, zagrozenie ponad skale !!\n");
                ZAGROZENIE = 100.0F;
            }
            if (SilaWiatru > 20.0F)
            {
                System.Console.Write("Za mocny wiatr, zagrozenie ponad skale !!\n");
                ZAGROZENIE = 100.0F;
            }
            if (Cisnienie < 700.0F)
            {
                System.Console.Write("Za niskie cisnienie, zagrozenie ponad skale !!\n");
                ZAGROZENIE = 100.0F;
            }
            if (Wilgotnosc < 30.0F)
            {
                System.Console.Write("Za suche powietrze, zagrozenie ponad skale !!\n");
                ZAGROZENIE = 100.0F;
            }
            if (Wilgotnosc > 80.0F)
            {
                System.Console.Write("Powietrze zbyt wilgotne, zagrozenie ponad skale !!\n");
                ZAGROZENIE = 100.0F;
            }

            // wzór -> zagrozenie = ( 50000SW * sqrt(Wilgotnosc) ) / ( Temperatura^2 * (cisnienie/10) )

            SilaWiatru *= 50000;
            Wilgotnosc = Math.Sqrt((WilToDegre(Wilgotnosc)));
            Temperatura *= Temperatura;
            Cisnienie /= 10;

            double debugLicznik = (SilaWiatru * Wilgotnosc);
            double debugMianownik = (Temperatura * Cisnienie);
            ZAGROZENIE = debugLicznik / debugMianownik;

            if (debug)
            {
                System.Console.Write("SilaWiatru: {0}\n", SilaWiatru);
                System.Console.Write("Wilgoc przelcznik: {0}\n", Wilgotnosc);
                System.Console.Write("licznik: {0}\n\n", debugLicznik);

                System.Console.Write("Temperatura: {0}\n", Temperatura);
                System.Console.Write("Cisnienie: {0}\n", Cisnienie);
                System.Console.Write("mianownik: {0}\n", debugMianownik);

                System.Console.Write("ZAGROZENIE w funkcji: {0}\n", ZAGROZENIE);
            }

            return ZAGROZENIE;
        }

        private double stopnieToRad(double stop)
        {
            const double Pi = Math.PI;
            return (stop * Pi) / 180;
        }

        private double WilToDegre(double Wilgotnosc)
        {
            // 0-90 stopni = 0-30 procent wilgotnosci
            // 90-180 stopni = 30-80 procent wilgotnosci
            // 180-270 stopni = 8-100 procent wilgotnosci
            // wiecej niz 100% lub mniej niz 0% wilgotnosci to blad

            double ret = 0;
            float a1 = 1.8F;
            float b1 = 36.0F;
            float a2 = 4.5F;
            float b2 = -180.0F;

            if (Wilgotnosc < 0.0F || Wilgotnosc > 100.0F) { System.Console.Write("\nZle paramtery wejsciowe wilgoci\n(dopuszczlane 0-100)\n"); return -1; }
            else
            {
                if (Wilgotnosc < 30.0F) ret = Wilgotnosc * 3;
                else if (Wilgotnosc < 80.0F) ret = (Wilgotnosc * a1) + b1;
                else ret = (Wilgotnosc * a2) + b2;
            }

            return Math.Abs(Math.Sin(stopnieToRad(ret)));
        }

        static void Main()
        {
            //moutain_warning mw = new moutain_warning();

            double Temperatura; // Mniej niż 15 -> ŹLE
            double SilaWiatru; // Wiecej niz 20m/s -> ŹLE
                               // kierunek wiatru nie ma znaczenia dla zagraożenia
            double Cisnienie; // Mniej niz 700 Hpa -> ŹLE
            double Wilgotnosc; // Mniej niz 30% ŹLE AND Więcej niż 80% -> ŹLE

            double Zagr = 0;

            //Zagr = ZagrorzenieCal(Temperatura, SilaWiatru, Cisnienie, Wilgotnosc);
            System.Console.Write("SilaWiatru testy\n");
            for (SilaWiatru = 0.0; SilaWiatru < 13.0; SilaWiatru++)
            {
                Zagr = new moutain_warning().ZagrorzenieCal(26.0, SilaWiatru, 1000.0, 50.0);
                System.Console.Write("[{0}] Zagr: {1}\n", SilaWiatru, Zagr);
            }
            System.Console.Write("Temperatura testy\n");
            for (Temperatura = 15.0; Temperatura < 27.0; Temperatura++)
            {
                Zagr = new moutain_warning().ZagrorzenieCal(Temperatura, 5.0, 1000.0, 50.0);
                System.Console.Write("[{0}] Zagr: {1}\n", Temperatura, Zagr);
            }
            System.Console.Write("Cisnienie testy\n");
            for (Cisnienie = 800.0; Cisnienie < 1300.0; Cisnienie += 50)
            {
                Zagr = new moutain_warning().ZagrorzenieCal(20.0, 5.0, Cisnienie, 50.0);
                System.Console.Write("[{0}] Zagr: {1}\n", Cisnienie, Zagr);
            }
            System.Console.Write("Wilgotnosc testy\n");
            for (Wilgotnosc = 1.0; Wilgotnosc < 100.0; Wilgotnosc += 11)
            {
                Zagr = new moutain_warning().ZagrorzenieCal(20.0, 5.0, 1000.0, Wilgotnosc);
                System.Console.Write("[{0}] Zagr: {1}\n", Wilgotnosc, Zagr);
            }

            System.Console.Write("Skrajnie zle warunki 1\n");
            Zagr = new moutain_warning().ZagrorzenieCal(15.0, 9.9, 800.0, 79.9, false);
            System.Console.Write("Zagr: {0}\n", Zagr);

            System.Console.Write("Skrajnie zle warunki 2\n");
            Zagr = new moutain_warning().ZagrorzenieCal(30.0, 9.9, 800.0, 31.9, false);
            System.Console.Write("Zagr: {0}\n", Zagr);

            System.Console.Write("Idealne warunki wilgoc 45%\n");
            Zagr = new moutain_warning().ZagrorzenieCal(24.0, 1.0, 1000.0, 45.0, false);
            System.Console.Write("Zagr: {0}\n", Zagr);

            System.Console.Write("Idealne warunki wilgoc 60%\n");
            Zagr = new moutain_warning().ZagrorzenieCal(24.0, 1.0, 1000.0, 60.0, false);
            System.Console.Write("Zagr: {0}\n", Zagr);

            System.Console.Write("Idealne warunki wilgoc 75%\n");
            Zagr = new moutain_warning().ZagrorzenieCal(24.0, 1.0, 1000.0, 75.0, false);
            System.Console.Write("Zagr: {0}\n", Zagr);

            System.Console.ReadKey();

            // mniej niz 1 to male zagrozenie
            // wiecej niz jeden to duze zagrozenie
        }
    }

}
