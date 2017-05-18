package generateFeature;

import generateFeature.feature_function;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;


//��ù�����������
public class getBuysFeature {
	public static void main(String args[]) throws IOException {
		getBuysFeature getBFeature = new getBuysFeature();
		// //��ù�����������
		getBFeature
				.getBuysFeature_function(
						"E:\\Data\\feature\\yoochoose-buys-click-feature-maxBuysFrequentness-monthLen.csv",
						10);

	}

	// @SuppressWarnings("unchecked")
	@SuppressWarnings("unchecked")
	private void getBuysFeature_function(String fileOut, int buyThreshold)
			throws IOException {
		int minPrice, maxPrice;
		@SuppressWarnings("unused")
		int time = 0;
		@SuppressWarnings("unused")
		int weekTime;
		String beginTime = "-1", endTime = "-1";
		String sessionId = "-1";
		String file_buys_line = null;
		int clickNumber = 0;
		int popularOrNot = 0;
		long b = System.currentTimeMillis();
		String data[];
		// itemPrice�ܹ�ͳ��buy�е���Ŀ����۸�
		HashMap<String, Integer> itemPrice = new HashMap<>();
		// �õ�buy�ļ���popularItem���ֵ�
		HashMap<String, Integer> popularItem = new HashMap<>();
		// buysFrequentnessFile�洢����buy�е���Ŀ:����������ֵ�
		HashMap<String, Integer> buysFrequentness = new HashMap<>();
		HashMap<String, String> buyMaxMonth = new HashMap<>();
		HashMap<String, Integer> buyMonthLen = new HashMap<>();
		// clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������
		HashMap<String, Integer> clickInfo = new HashMap<>();
		// categoryInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ����������ִ���
		HashMap<String, Integer> categoryInfo = new HashMap<>();
		// category�����������Ŀ�������
		HashMap<String, String> category = new HashMap<>();

		FileReader fr = new FileReader(
				"E:\\Data\\yoochoose-clicks-hasBuyData.dat");
		BufferedReader br_clickhasBuy = new BufferedReader(fr);

		FileWriter fw = new FileWriter(fileOut);
		BufferedWriter bw = new BufferedWriter(fw);

		// category.dat�����������Ŀ�������
		FileReader fr_category = new FileReader(
				"E:\\Data\\yoochoose-category.dat");
		BufferedReader br_category = new BufferedReader(fr_category);

		bw.write("clickNumber,popularOrNot,repeatClick,priceGrade,categoryValue,buysFrequentness,month,category\n");
		/*
		 * itemPrice = (HashMap<String, Integer>)
		 * feature_function.getItemPrice().get(0); minPrice = (int)
		 * feature_function.getItemPrice().get(1); maxPrice = (int)
		 * feature_function.getItemPrice().get(2);
		 */
		itemPrice = (HashMap<String, Integer>) feature_function.getItemPrice()
				.get(0);
		minPrice = (int) feature_function.getItemPrice().get(1);
		maxPrice = (int) feature_function.getItemPrice().get(2);

		popularItem = (HashMap<String, Integer>) feature_function
				.getPopularItem();
		buysFrequentness = (HashMap<String, Integer>) new feature_function()
				.getBuysFrequentness("E:\\Data\\yoochoose-buys-analyse-sorted.dat");

		buyMaxMonth = (HashMap<String, String>) feature_function
				.getDicFromFile("E:\\Data\\yoochoose-buyMaxMonth.dat");
		buyMonthLen = (HashMap<String, Integer>) feature_function
				.getDicFromFile_Integer("E:\\Data\\yoochoose-buyMonthLen.dat");
		category = (HashMap<String, String>) feature_function
				.getDicFromFile("E:\\Data\\yoochoose-category.dat");
		while ((file_buys_line = br_clickhasBuy.readLine()) != null) {
			int loop = 0;
			data = file_buys_line.split(",");
			if (!sessionId.equals(data[0])) {
				if (sessionId.equals("-1")) {
					beginTime = data[1];
					endTime = data[1];
					sessionId = data[0];
				} else {
					if (clickNumber == 1) {
						time = 0;
					} else
						time = new feature_function().calculateTime(beginTime,
								endTime);// ����ʱ�����ķ�����
					weekTime = new feature_function()
							.calculateWeekTime(endTime);
					String categoryValue = new feature_function()
							.getCategoryValue(categoryInfo);
					categoryInfo.clear();//////////////////////////////////////////////ÿ���Ựӳ��������
					
					String returnString = new feature_function().repeatOrNot(clickInfo, itemPrice, minPrice, maxPrice,buysFrequentness);
					int repeat = Integer.valueOf(returnString.split(";")[0]);
					int priceGrade = Integer
							.valueOf(returnString.split(";")[1]);
					int maxBuysFrequentness = Integer.valueOf(returnString
							.split(";")[2]);
					String month = data[1].split("-")[1];
					int monthRight = -1;
					if (buyMaxMonth.containsKey(data[2])) { // ���buyҲ����clickhasbuy�е���Ŀ
						if (buyMaxMonth.get(data[2]).equals(month)) {
							monthRight = 1; // ������Ʒ��������
						} else {
							monthRight = 0;
						}
					}
					month = String.valueOf(monthRight) + "M";
					int monthLen = -1;
					if (buyMonthLen.containsKey(data[2])) {
						monthLen = buyMonthLen.get(data[2]); // ������Ŀ�����Խ���·ݸ�ֵ��monthLen
					}
					bw.write(String.valueOf(clickNumber) + ","
							+ String.valueOf(popularOrNot) + ","
							+ String.valueOf(repeat) + ","
							+ String.valueOf(priceGrade) + "," + categoryValue
							+ "," + String.valueOf(maxBuysFrequentness) + ","
							+ month + "," + String.valueOf(monthLen) + ",yes"
							+ "\n");
					beginTime = data[1];
					sessionId = data[0];
				}
				clickNumber = 0;
				popularOrNot = 0;
				int maxBuysFrequentness=0;
				clickInfo.clear();   //����û�뵽!!!
				
			} else { // ��sessionId== data[0]:
				endTime = data[1];
				if (popularItem.containsKey(data[2]))
					popularOrNot = 1;
			}
			if (clickInfo.containsKey(data[2])) { // clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������
				int j = (int) clickInfo.get(data[2]);
				clickInfo.put(data[2], ++j);
			} else
				clickInfo.put(data[2], 1);
			clickNumber = 1 + clickNumber;
			String categoryId = data[3].trim() + "C";
			if (categoryId.length() > 4)
				categoryId = "-1C";
			if (!categoryId.equals("0C")) {
				if (categoryInfo.containsKey(categoryId)) {
					int k = categoryInfo.get(categoryId);
					categoryInfo.put(categoryId, ++k);
				} else
					categoryInfo.put(categoryId, 1);
			} else if (category.containsKey(data[2])) {
				if (categoryInfo.containsKey(category.get(data[2]))) {
					int m = categoryInfo.get(category.get(data[2]));
					categoryInfo.put(category.get(data[2]), ++m);
				} else
					categoryInfo.put(category.get(data[2]), 1);
			}
			loop++;
			if (loop % 10000 == 0)
				System.out.println(loop);
		} // ��Ӧ�������while����ѭ��
		br_clickhasBuy.close();
		bw.close();
		br_category.close();
		long e = System.currentTimeMillis();
		System.out.println("\t��ʱ:" + (e - b) + "ms");
	}

}
