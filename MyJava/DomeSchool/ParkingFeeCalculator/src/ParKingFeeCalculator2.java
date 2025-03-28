import java.util.Scanner;

public class ParKingFeeCalculator2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("停车场累计计费场景（输入0后结算总账并结束）");

        double time;
        do {
            System.out.print("请输入停车时间（分钟）：");
            time = scanner.nextDouble();
            long priceIncreasePeriod;
            if (time > 0 && time <= 30) {
                System.out.println("免费时段 收取费用为：0元");
            }
            else if (time<=60){
                System.out.println("基础时段 收取费用为：6元");
            }
            else if (time<=120){
                System.out.println("基础时段 收取费用为：12元");
            }
            else {
                priceIncreasePeriod = Math.round(((time-120)/60)*10 + 12);
                System.out.println("加价时段 收取费用为：" + (int)priceIncreasePeriod + "元");
            }
        } while (time != 0);
    }
}
