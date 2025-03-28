import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class DaysCalculator1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入日期 (格式: yyyy-MM-dd 或 yyyy-M-d): ");
        String dateInput = scanner.nextLine();
        
        try {
            LocalDate inputDate;
            try {
                inputDate = LocalDate.parse(dateInput);
            } catch (Exception e) {
                String[] parts = dateInput.split("-");
                if (parts.length == 3) {
                    int year = Integer.parseInt(parts[0]);
                    int month = Integer.parseInt(parts[1]);
                    int day = Integer.parseInt(parts[2]);
                    inputDate = LocalDate.of(year, month, day);
                } else {
                    throw new Exception("日期格式不正确");
                }
            }

            LocalDate now = LocalDate.now();
            if (inputDate.getYear() > now.getYear() + 100) {
                System.out.println("警告：您输入的是一个很远的未来日期");
            }
            calculateDays(inputDate);
        } catch (Exception e) {
            System.out.println("日期格式错误，请使用 yyyy-MM-dd 或 yyyy-M-d 格式，例如: 2023-12-15 或 2023-12-5");
            System.out.println("错误详情: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
    public static void calculateDays(LocalDate date) {
        int year = date.getYear();
        LocalDate startOfYear = LocalDate.of(year, 1, 1);
        LocalDate endOfYear = LocalDate.of(year, 12, 31);
        long daysPassed = ChronoUnit.DAYS.between(startOfYear, date);
        long daysUntilNextYear = ChronoUnit.DAYS.between(date, endOfYear) + 1;
        System.out.println("今年已经过去了 " + daysPassed + " 天");
        System.out.println("距离下一个新年还有 " + daysUntilNextYear + " 天");
    }
} 