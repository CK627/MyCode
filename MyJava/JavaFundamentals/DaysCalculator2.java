import java.util.Scanner;

public class DaysCalculator2 {
    
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入日期 (格式: yyyy-MM-dd 或 yyyy-M-d): ");
        String dateInput = scanner.nextLine();
        try {
            String[] parts = dateInput.split("-");
            if (parts.length != 3) {
                throw new Exception("日期格式不正确，请使用 yyyy-M-d 格式");
            }
            
            int year = Integer.parseInt(parts[0]);
            int month = Integer.parseInt(parts[1]);
            int day = Integer.parseInt(parts[2]);
            
            if (isValidDate(year, month, day)) {
                calculateDays(year, month, day);
            } else {
                System.out.println("输入的日期无效，请检查日期是否正确");
            }
        } catch (NumberFormatException e) {
            System.out.println("日期格式错误：年、月、日必须是数字");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        scanner.close();
    }
    
    public static boolean isValidDate(int year, int month, int day) {
        if (year < 1 || month < 1 || month > 12 || day < 1) {
            return false;
        }
        int[] daysInMonth = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (isLeapYear(year)) {
            daysInMonth[2] = 29;
        }
        return day <= daysInMonth[month];
    }
    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
    public static int getDayOfYear(int year, int month, int day) {
        int[] daysBeforeMonth = {0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        int dayOfYear = daysBeforeMonth[month] + day;
        if (month > 2 && isLeapYear(year)) {
            dayOfYear++;
        }
        return dayOfYear;
    }
    
    public static void calculateDays(int year, int month, int day) {
        int daysPassed = getDayOfYear(year, month, day) - 1;
        int daysInYear = isLeapYear(year) ? 366 : 365;
        int daysUntilNextYear = daysInYear - getDayOfYear(year, month, day) + 1;
        
        System.out.println("今年已经过去了 " + daysPassed + " 天");
        System.out.println("距离下一个新年还有 " + daysUntilNextYear + " 天");
    }
} 