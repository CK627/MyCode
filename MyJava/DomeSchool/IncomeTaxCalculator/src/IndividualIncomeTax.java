import java.util.Scanner;

public class IndividualIncomeTax {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入年收入（元）：");
        double annualIncome = scanner.nextDouble();
        double taxableIncome = annualIncome - 60000;
        int grade = 0;
        double tax;
        if (taxableIncome < 0) {
            tax = 0;
        } else if (taxableIncome <= 36000) {
            tax = taxableIncome * 0.03;
            grade = 1;
        } else if (taxableIncome <= 144000) {
            tax = taxableIncome * 0.10 - 2520;
            grade = 2;
        } else if (taxableIncome <= 300000) {
            tax = taxableIncome * 0.20 - 16920;
            grade = 3;
        } else if (taxableIncome <= 420000) {
            tax = taxableIncome * 0.25 - 31920;
            grade = 4;
        } else if (taxableIncome <= 660000) {
            tax = taxableIncome * 0.30 - 52920;
            grade = 5;
        } else if (taxableIncome <= 960000) {
            tax = taxableIncome * 0.35 - 85920;
            grade = 6;
        } else { // 第7级 45%
            tax = taxableIncome * 0.45 - 181920;
            grade = 7;
        }
        System.out.printf("应纳个税："+tax+"元，第"+grade+"级");
    }
}