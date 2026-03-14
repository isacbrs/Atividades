import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Numeros de laranjas:");
        int laranjas = entrada.nextInt();
        System.out.println("O pagamento é no Pix? true ou false");
        var pix = entrada.hasNextBoolean();

        double valor = laranjas < 10 ? 2.5 : 2;

        double desconto = pix == true ? .9 : 1;

        double valorFinal = valor * laranjas * desconto;

        System.out.println("VALOR A PAGAR:" + valorFinal);
    }
}