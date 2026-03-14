import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        System.out.println("Escolha: " + System.lineSeparator() //o /n também iria funcionar(mas só para windows, oque não é uma boa prática para Dev JAVA)
                + "1- Pesquisar usuário" + System.lineSeparator()
                + "2- Cadastrar usuário" + System.lineSeparator()
                + "3- Abrir pedido" + System.lineSeparator()
                + "4- Fechar pedido.");
        int opcao = leitor.nextInt();

        if (opcao == 1) {
            System.out.println(opcao + " - Pesquisar usuário");
        } else if (opcao == 2){
            System.out.println(opcao + " - Cadastrar usuário");
        }else if (opcao == 3) {
            System.out.println(opcao + " - Abrir pedido");
        }else if (opcao == 4) {
            System.out.println(opcao + " - Fechar pedido");
        };

                                    //OU
        switch (opcao){
            case 1 : System.out.println(opcao + " - Pesquisar usuário");
            break;
            case 2 : System.out.println(opcao + " - Cadastrar usuário");
            break;
            case 3 : System.out.println(opcao + " - Abrir pedido");
            break;
            case 4 : System.out.println(opcao + " - Fechar pedido");
            break;
            default: System.out.println("Opção invalida");
        }
    }
}