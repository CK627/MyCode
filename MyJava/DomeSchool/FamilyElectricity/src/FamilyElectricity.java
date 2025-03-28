public class FamilyElectricity {
    public static void main(String[] args) {
        String[] families = {"赵家", "钱家", "孙家", "李家"};
        double[][] data = {
                {150.0, 180.0, 200.0, 220.0, 190.0, 210.0},
                {130.0, 160.0, 170.0, 185.0, 175.0, 160.0},
                {210.0, 230.0, 240.0, 260.0, 250.0, 280.0},
                {170.0, 200.0, 210.0, 245.0, 205.0, 195.0}
        };
        // 计算家庭总用电量
        double[] TotalHouseholdElectricityConsumption = new double[4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 6; j++) {
                TotalHouseholdElectricityConsumption[i] += data[i][j];
            }
        }
        // 计算月份总用电量
        double[] MonthlyTotalElectricityConsumption = new double[6];
        for (int j = 0; j < 6; j++) {
            for (int i = 0; i < 4; i++) {
                MonthlyTotalElectricityConsumption[j] += data[i][j];
            }
        }
        // 输出结果
        System.out.println("==== 电费统计报告 ====\n");
        // 家庭总用电量
        System.out.println("1. 各家庭总用电量：");
        for (int i = 0; i < 4; i++) {
            System.out.printf("%s -> %d千瓦时%n", families[i], (int) Math.round(TotalHouseholdElectricityConsumption[i]));
        }
        // 月份总用电量
        System.out.println("\n2. 各月总用电量：");
        String[] months = {"1月", "2月", "3月", "4月", "5月", "6月"};
        for (int j = 0; j < 6; j++) {
            System.out.printf("%s：%d千瓦时%n", months[j], (int) Math.round(MonthlyTotalElectricityConsumption[j]));
        }
        // 查找最高用电家庭
        int HighestElectricityConsumptionHousehold = 0;
        for (int i = 1; i < 4; i++) {
            if (TotalHouseholdElectricityConsumption[i] > TotalHouseholdElectricityConsumption[HighestElectricityConsumptionHousehold]) {
                HighestElectricityConsumptionHousehold = i;
            }
        }
        System.out.printf("\n3. 用电最高家庭：\n%s (%.0f 千瓦时)%n",
                families[HighestElectricityConsumptionHousehold], TotalHouseholdElectricityConsumption[HighestElectricityConsumptionHousehold]);
        System.out.println("\n4. 节能提示：");
        java.util.ArrayList<String> EnergySavingTips = new java.util.ArrayList<>();
        for (int i = 0; i < 4; i++) {
            if (TotalHouseholdElectricityConsumption[i] > 1000) {
                EnergySavingTips.add(families[i]);
            }
        }
        if (!EnergySavingTips.isEmpty()) {
            System.out.println(String.join("、", EnergySavingTips));
        }
    }
}