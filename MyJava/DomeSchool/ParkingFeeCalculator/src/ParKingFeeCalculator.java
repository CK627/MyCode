import java.util.Scanner;

public class ParKingFeeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("停车场累计计费场景（输入0后结算总账并结束）");
        double TotalBilling = 0; // 计数器，用于结算费用的存储

        while (true) {
            System.out.print("请输入停车时间（分钟）：");
            double time = scanner.nextDouble();
            if (time == 0) {
                break;
            } else if (time <= 30) {
                System.out.println("当前费用：" + 0 + "元");
                TotalBilling += 0;
            } else if (time <= 60) {
                System.out.println("当前费用：" + 6 + "元");
                TotalBilling += 6;
            } else if (time <= 120) {
                System.out.println("当前费用：" + 12 + "元");
                TotalBilling += 12;
            } else {
                int PriceIncreasePeriod = (int) Math.round(((time - 120) / 60) * 10 + 12); // int转化去除小数点
                System.out.println("当前费用：" + PriceIncreasePeriod + "元");
                TotalBilling += PriceIncreasePeriod;
            }
        }
        System.out.println("总费用：" + (int) TotalBilling + "元");
    }
}