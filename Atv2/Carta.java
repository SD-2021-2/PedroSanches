public class Carta {
    String nomecart;
    String toString(int cart, int naipe){
        switch (cart) {
            case 1:
              nomecart="Ás";
              break;
            case 2:
                nomecart="Dois";
              break;
            case 3:
                nomecart="Três";
              break;
            case 4:
               nomecart="Quatro";
              break;
            case 5:
            nomecart="Cinco";
                break;
            case 6:
            nomecart="Seis";
                break;
            case 7:
            nomecart="Sete";
                break;
            case 8:
            nomecart="Oito";
                break;
            case 9:
            nomecart=("Nove");
                break;
            case 10:
            nomecart=("Dez");
                break;
            case 11:
            nomecart=("Dama");
                break;
            case 12:
            nomecart=("Valete");
                break;
            case 13:
            nomecart=("Reis");
                break;
            default:
            nomecart=("Número inválido");
         }
        switch (naipe) {
            case 1:
                nomecart.concat(" de Ouros");
                break;
            case 2:
                nomecart.concat(" de Paus");
                break;
            case 3:
                nomecart.concat(" de Copas");
                break;
            case 4:
                nomecart.concat(" de Espadas");
                break;
            default:
                nomecart=("Número inválido");
        }
        return nomecart;
    }
}
