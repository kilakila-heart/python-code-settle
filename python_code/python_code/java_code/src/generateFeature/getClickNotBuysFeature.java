package generateFeature;


import generateFeature.feature_function;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;

import org.omg.CORBA.PRIVATE_MEMBER;


//��ù�����������
public class getClickNotBuysFeature {
	public static void main(String args[]) throws IOException {
		getClickNotBuysFeature C_NotBuyFeature = new getClickNotBuysFeature();
		// //��ù�����������
		C_NotBuyFeature.ClickNotBuys_function(
						"E:\\Data\\feature\\yoochoose-notBuys-click-feature-maxBuysFrequentness-monthLen.csv",
						10);

	}

	// @SuppressWarnings("unchecked")
	@SuppressWarnings("unchecked")
	private void ClickNotBuys_function(String fileOut, int buyThreshold)
			throws IOException {
		int minPrice, maxPrice;
		@SuppressWarnings("unused")
		int time = 0;
		@SuppressWarnings("unused")
		int weekTime;
		String beginTime = "-1", endTime = "-1";
		String sessionId = "-1";
		String file_buys_line = null;
		int loop = 0;
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
		// clickInfo�ܹ�ͳ��NotBuyData�г��ֵ���Ŀ�������
		HashMap<String, Integer> clickInfo = new HashMap<>();
		// categoryInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ����������ִ���
		HashMap<String, Integer> categoryInfo = new HashMap<>();
		// category�����������Ŀ�������
		HashMap<String, String> category = new HashMap<>();
		int bufferSize = 20 * 1024 * 1024;// ���д�ļ��Ļ���Ϊ20MB
		FileReader fr = new FileReader(
				"E:\\Data\\yoochoose-clicks-notBuyData.dat");
		BufferedReader br_clickNotBuy = new BufferedReader(fr,bufferSize);

		FileWriter fw = new FileWriter(fileOut);
		BufferedWriter bw = new BufferedWriter(fw,bufferSize);

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
		while ((file_buys_line = br_clickNotBuy.readLine()) != null) {			
			loop++;
			if (loop % 100000 == 0)
				System.out.println(loop);
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
							+ month + "," + String.valueOf(monthLen) + ",no"
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
			if (clickInfo.containsKey(data[2])) { // clickInfo�ܹ�ͳ��notBuyData�г��ֵ���Ŀ�������
				int j = (int) clickInfo.get(data[2]);
				clickInfo.put(data[2], ++j);
			} else
				clickInfo.put(data[2], 1);
			
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
			clickNumber = 1 + clickNumber;
			
		} // ��Ӧ�������while����ѭ��
		br_clickNotBuy.close();
		bw.close();
		br_category.close();
		long e = System.currentTimeMillis();
		System.out.println("\t��ʱ:" + (e - b)/1000 + "s");
	}

}
