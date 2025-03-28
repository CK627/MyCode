import java.util.Scanner;

public class IncomeTaxCalculator_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入年收入（元）：");
        double annualIncome = scanner.nextDouble();
        double taxableIncome = annualIncome - 60000;
        int taxLevel = 0;
        double taxRate = 0;
        double quickDeduction = 0;
        if (taxableIncome <= 0) {
            System.out.println("无需纳税");
            return;
        } else if (taxableIncome <= 36000) {
            taxLevel = 1;
            taxRate = 0.03;
        } else if (taxableIncome <= 144000) {
            taxLevel = 2;
            taxRate = 0.10;
            quickDeduction = 2520;
        } else if (taxableIncome <= 300000) {
            taxLevel = 3;
            taxRate = 0.20;
            quickDeduction = 16920;
        } else if (taxableIncome <= 420000) {
            taxLevel = 4;
            taxRate = 0.25;
            quickDeduction = 31920;
        } else if (taxableIncome <= 660000) {
            taxLevel = 5;
            taxRate = 0.30;
            quickDeduction = 52920;
        } else if (taxableIncome <= 960000) {
            taxLevel = 6;
            taxRate = 0.35;
            quickDeduction = 85920;
        } else {
            taxLevel = 7;
            taxRate = 0.45;
            quickDeduction = 181920;
        }
        double tax = taxableIncome * taxRate - quickDeduction;
        System.out.printf("应纳税额: %.2f 元，适用"+taxLevel+"级税率", tax);
    }
}
