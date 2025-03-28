import java.util.Scanner;

public class IncomeTaxCalculator {
    private static final double[][] TAX_BRACKETS = {
        {36000, 0.03, 0},
        {144000, 0.10, 2520},
        {300000, 0.20, 16920},
        {420000, 0.25, 31920},
        {660000, 0.30, 52920},
        {960000, 0.35, 85920},
        {Double.MAX_VALUE, 0.45, 181920}
    };
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入年收入（元）：");
        double annualIncome = scanner.nextDouble();
        scanner.close();
        double taxableIncome = annualIncome - 60000;
        if(taxableIncome <= 0) {
            System.out.println("无需纳税");
            return;
        }
        int bracketIndex = 0;
        while(taxableIncome > TAX_BRACKETS[bracketIndex][0]) {
            bracketIndex++;
        }
        double tax = taxableIncome * TAX_BRACKETS[bracketIndex][1] - TAX_BRACKETS[bracketIndex][2];
        int taxLevel = bracketIndex + 1;
        System.out.printf("应纳税额: %.2f 元，对应的级数为：%d级", tax, taxLevel);
    }
}
