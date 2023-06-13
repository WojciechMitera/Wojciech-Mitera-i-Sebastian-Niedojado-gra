def stworz_plansze():
    plansza = [[' ' for _ in range(3)] for _ in range(3)]
    return plansza

def wyswietl_plansze(plansza):
    for i in range(3):
        print("█████████████")
        for j in range(3):
            print("█", end=" ")
            print(plansza[i][j], end=" ")
        print("█")
    print("█████████████")

def sprawdz_wygranego(plansza):
    for wiersz in plansza:
        if wiersz[0] == wiersz[1] == wiersz[2] != ' ':
            return wiersz[0]

    for kolumna in range(3):
        if plansza[0][kolumna] == plansza[1][kolumna] == plansza[2][kolumna] != ' ':
            return plansza[0][kolumna]

    if plansza[0][0] == plansza[1][1] == plansza[2][2] != ' ':
        return plansza[0][0]
    if plansza[0][2] == plansza[1][1] == plansza[2][0] != ' ':
        return plansza[0][2]

    return None

def czy_plansza_pelna(plansza):
    for wiersz in plansza:
        if ' ' in wiersz:
            return False
    return True

def wykonaj_ruch(plansza, wiersz, kolumna, symbol):
    if plansza[wiersz][kolumna] == ' ':
        plansza[wiersz][kolumna] = symbol
        return True
    else:
        return False

def rozpocznij_gre():
    plansza = stworz_plansze()
    aktualny_symbol = 'X'

    while True:
        wyswietl_plansze(plansza)

        while True:
            try:
                wiersz = int(input('Podaj numer wiersza (0-2): '))
                kolumna = int(input('Podaj numer kolumny (0-2): '))
                if wykonaj_ruch(plansza, wiersz, kolumna, aktualny_symbol):
                    break
                else:
                    print('Nieprawidłowy ruch. Spróbuj jeszcze raz.')
            except ValueError:
                print('Nieprawidłowe dane. Spróbuj jeszcze raz.')

        wygrany = sprawdz_wygranego(plansza)
        if wygrany:
            print(f'Zwycięża {wygrany}!')
            break
        elif czy_plansza_pelna(plansza):
            print('Remis!')
            break

        aktualny_symbol = 'O' if aktualny_symbol == 'X' else 'X'

rozpocznij_gre()
