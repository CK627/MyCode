import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

class IDCardProcessor {
    private static final String[] ZODIAC_SIGNS = {"鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"};

    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入身份证号码: ");
        String idCard = scanner.nextLine().toUpperCase();
        if (idCard.length() != 18) {
            System.out.println("身份证号码长度不正确，请输入18位身份证号码");
            return;
        }
        LocalDate birthDate = parseBirthDate(idCard);
        System.out.println("出生日期: " + birthDate.format(DateTimeFormatter.ISO_DATE));
        String zodiac = getZodiac(birthDate.getYear());
        System.out.println("生肖: " + zodiac);
        LocalDate nextBirthday = calculateNextBirthday(birthDate);
        System.out.println("下次生日: " + nextBirthday.format(DateTimeFormatter.ISO_DATE));
        scanner.close();
    }

    private static LocalDate parseBirthDate(String idCard) {
        String birthDateStr = idCard.substring(6, 14);
        return LocalDate.parse(birthDateStr, DateTimeFormatter.ofPattern("yyyyMMdd"));
    }

    private static String getZodiac(int birthYear) {
        return ZODIAC_SIGNS[(birthYear - 4) % 12];
    }

    private static LocalDate calculateNextBirthday(LocalDate birthDate) {
        LocalDate today = LocalDate.now();
        LocalDate thisYearBirthday = birthDate.withYear(today.getYear());
        
        return thisYearBirthday.isBefore(today) || thisYearBirthday.isEqual(today)
                ? thisYearBirthday.plusYears(1)
                : thisYearBirthday;
    }
}

