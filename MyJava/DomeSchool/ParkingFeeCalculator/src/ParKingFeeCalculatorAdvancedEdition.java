import java.io.IOException;
import java.util.*;
import java.time.*;
import java.nio.file.*;
import java.time.format.DateTimeFormatter;

public class ParKingFeeCalculatorAdvancedEdition {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("停车场累计计费场景（输入0后结算总账并结束）");
        double TotalBilling = 0;

        // 读取会员用户字典
        HashMap<String, Boolean> members = new HashMap<>();
        List<String> lines = Files.readAllLines(Paths.get("/Users/ck/Documents/MyCode/MyJava/DomeSchool/ParkingFeeCalculator/src/VIPUser.txt"));
            for (String line : lines) {
                String[] parts = line.split(",");
                if (parts.length >= 1) {
                    members.put(parts[0].trim(), true);
                }
            }

        // 时间模式选择
        LocalDate nowDate;
        LocalTime nowTime;
        System.out.print("时间模式（1自动获取/2手动输入）: ");
        int timeMode = Integer.parseInt(scanner.nextLine());
        if (timeMode == 2) {
            System.out.print("请输入日期时间（格式：yyyy-MM-dd HH:mm）: ");
            String inputTime = scanner.nextLine();
            LocalDateTime dateTime = LocalDateTime.parse(inputTime.trim(), DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));
            nowDate = dateTime.toLocalDate();
            nowTime = dateTime.toLocalTime();
        } else {
            nowDate = LocalDate.now();
            nowTime = LocalTime.now();
        }

        // 会员验证
        boolean isMember;
        System.out.print("请输入用户ID: ");
        String memberId = scanner.nextLine().trim();
        isMember = members.containsKey(memberId);
        if (isMember) {
            System.out.println(memberId.trim() + "是会员");
        } else {
            System.out.println(memberId + "不是会员");
        }

        while (true) {
            System.out.print("请输入停车时间（分钟）：");
            String input = scanner.nextLine().trim();
            if (input.isEmpty()) continue;

            double time = Double.parseDouble(input);
            if (time == 0) break;

            if (isMember && time <= 60) {
                System.out.println("当前费用：0元");
                continue;
            }

            double fee = 0;
            if (time > 120) {
                fee = Math.round(((time - 120) / 60) * 10 + 12);
            } else if (time > 60) {
                fee = 12;
            } else if (time > 30) {
                fee = 6;
            }

            boolean isWeekend = nowDate.getDayOfWeek().getValue() > 5;
            boolean isPeak = (nowTime.getHour() >= 5 && nowTime.getHour() < 8) || (nowTime.getHour() >= 17 && nowTime.getHour() < 20);

            if (isMember) {
                if (isWeekend) fee *= 0.8;
            }
            if (isPeak) fee *= 0.9;

            System.out.printf("当前费用：%.0f元\n", fee);
            TotalBilling += fee;
        }
        System.out.printf("总费用：%.0f元", TotalBilling); // 格式化输出
    }
}