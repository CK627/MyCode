public class MyProfile {
        public static void main(String[] args) {
            // 个人信息变量声明
            String name = "毛文俊"; // 名字
            char gender = '男';  // 性别
            String studentId = "2402410217"; // 学号
            String hometown = "浙江省衢州市衢江区";  // 籍贯
            int age = 20; // 年龄
            double height = 1.75; // 身高
            double weight = 70; // 体重

            // 格式化输出个人信息
            System.out.println("========== 个人信息 ==========");
            System.out.printf("%-6s: %s%n", "姓名", name);
            System.out.printf("%-6s: %c%n", "性别", gender);
            System.out.printf("%-6s: %s%n", "学号", studentId);
            System.out.printf("%-6s: %s%n", "籍贯", hometown);
            System.out.printf("%-6s: %d岁%n", "年龄", age);
            System.out.printf("%-6s: %.2f米%n", "身高", height);
            System.out.printf("%-6s: %.1f公斤%n", "体重", weight);
        }
}
