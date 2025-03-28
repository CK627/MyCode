import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class FamilyElectricity2 {
    public static void main(String[] args) {
        Map<String, List<Double>> familyData = new LinkedHashMap<String, List<Double>>() {{
            put("赵家", Arrays.asList(150.0,180.0,200.0,220.0,190.0,210.0));
            put("钱家", Arrays.asList(130.0,160.0,170.0,185.0,175.0,160.0));
            put("孙家", Arrays.asList(210.0,230.0,240.0,260.0,250.0,280.0));
            put("李家", Arrays.asList(170.0,200.0,210.0,245.0,205.0,195.0));
        }};
        // 家庭总用电量
        Map<String, Double> familyTotal = new LinkedHashMap<>();
        for (Map.Entry<String, List<Double>> entry : familyData.entrySet()) {
            double sum = 0.0;
            for (Double value : entry.getValue()) {
                sum += value;
            }
            familyTotal.put(entry.getKey(), sum);
        }
        // 月份总用电量
        String[] months = {"1月","2月","3月","4月","5月","6月"};
        Map<String, Double> monthTotalMap = new LinkedHashMap<>();
        for (int i = 0; i < months.length; i++) {
            final int monthIndex = i;
            double total = 0.0;
            for (List<Double> values : familyData.values()) {
                total += values.get(monthIndex);
            }
            monthTotalMap.put(months[i], total);
        }
        // 查找最高用电家庭
        Map.Entry<String, Double> maxEntry = null;
        for (Map.Entry<String, Double> entry : familyTotal.entrySet()) {
            if (maxEntry == null || entry.getValue() > maxEntry.getValue()) {
                maxEntry = entry;
            }
        }
        System.out.println("===== 电费统计报告 =====\n");
        System.out.println("家庭总用电量：");
        for (Map.Entry<String, Double> entry : familyTotal.entrySet()) {
            System.out.printf("%s -> %.0f千瓦时%n", entry.getKey(), entry.getValue());
        }

        System.out.println("\n每月总用电量：");
        for (Map.Entry<String, Double> entry : monthTotalMap.entrySet()) {
            System.out.printf("%s：%.0f千瓦时%n", entry.getKey(), entry.getValue());
        }

        System.out.printf("\n用电最高家庭：\n%s (%.0f 千瓦时)%n",
            maxEntry.getKey(), maxEntry.getValue());

        System.out.println("\n节能提示：");
        List<String> needAdvice = new ArrayList<>();
        for (Map.Entry<String, Double> entry : familyTotal.entrySet()) {
            if (entry.getValue() > 1000) {
                needAdvice.add(entry.getKey());
            }
        }
        if (!needAdvice.isEmpty()) {
            System.out.println(String.join("、", needAdvice));
        }
    }
}