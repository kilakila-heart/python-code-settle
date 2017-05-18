package generateFeature;

import generateFeature.feature_function;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;

public class getTestFeature {

	// 获得购买点击的特征

	public static void main(String args[]) throws IOException {
		getTestFeature getTFeature = new getTestFeature();
		// //获得购买点击的特征
		getTFeature
				.getTFeature_function(
						"E:\\Data\\feature\\yoochoose-test-feature-maxBuysFrequentness-monthLen.arff",
						10);

	}

	// @SuppressWarnings("unchecked")
	@SuppressWarnings("unchecked")
	private void getTFeature_function(String fileOut, int buyThreshold)
			throws IOException {
		int loop = 0;

		int test_Session = 0;
		int min_test_session = 2311289;

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
		// itemPrice能够统计buy中的项目及其价格
		HashMap<String, Integer> itemPrice = new HashMap<>();
		// 得到buy文件中popularItem的字典
		HashMap<String, Integer> popularItem = new HashMap<>();
		// buysFrequentnessFile存储的是buy中的项目:购买次数的字典
		HashMap<String, Integer> buysFrequentness = new HashMap<>();
		HashMap<String, String> buyMaxMonth = new HashMap<>();
		HashMap<String, Integer> buyMonthLen = new HashMap<>();
		// clickInfo能够统计hasBuyData中出现的项目及其次数
		HashMap<String, Integer> clickInfo = new HashMap<>();
		// categoryInfo能够统计hasBuyData中出现的项目的类别及类别出现次数
		HashMap<String, Integer> categoryInfo = new HashMap<>();
		// category包含点击的项目及其类别
		HashMap<String, String> category = new HashMap<>();
		// ///////////////////////
		// HashMap<String, Integer> s= new HashMap<String, Integer>();

		FileReader fr = new FileReader("E:\\Data\\yoochoose-test.dat");
		BufferedReader br_test = new BufferedReader(fr);

		FileWriter fw = new FileWriter(fileOut);
		BufferedWriter bw = new BufferedWriter(fw);

		FileWriter fw_test_sessionId = new FileWriter(
				"E:\\Data\\feature\\yoochoose-test-sessionId.dat");
		BufferedWriter bw_T_sessionId = new BufferedWriter(fw_test_sessionId);

		// category.dat包含点击的项目及其类别
		FileReader fr_category = new FileReader(
				"E:\\Data\\yoochoose-category.dat");
		BufferedReader br_category = new BufferedReader(fr_category);

		bw.write("@relation yoochoose-test-feature\n\n");
		bw.write("@attribute clickNumber numeric\n");
		bw.write("@attribute popularOrNot numeric\n");
		bw.write("@attribute repeatClick numeric\n");
		bw.write("@attribute priceGrade numeric\n");
		bw.write("@attribute categoryValue {3C,1C,0C,9C,7C,2C,4C,5C,6C,SC,8C,-1C,10C,12C,11C,13C,14C,15C,16C,17C,18C,19C,20C,21C,22C,23C,24C,25C,26C,27C,28C,29C,30C}\n");
		bw.write("@attribute buysFrequentness numeric\n");
		bw.write("@attribute month {-1M,0M,1M}\n");
		bw.write("@attribute monthLen numeric\n");
		bw.write("@attribute category {yes,no}\n\n@data\n");

		// bw.write("clickNumber,popularOrNot,repeatClick,priceGrade,categoryValue,buysFrequentness,month,category\n");
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
		bw_T_sessionId.write("sessionId\n");

		while ((file_buys_line = br_test.readLine()) != null) {
			loop++;
			if (loop % 200000 == 0)
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
								endTime);// 计算时间相差的分钟数
					weekTime = new feature_function()
							.calculateWeekTime(endTime);
					String categoryValue = new feature_function()
							.getCategoryValue(categoryInfo);
					categoryInfo.clear();// ////////////////////////////////////////////每个会话映射重新来

					String returnString = new feature_function().repeatOrNot(
							clickInfo, itemPrice, minPrice, maxPrice,
							buysFrequentness);
					int repeat = Integer.valueOf(returnString.split(";")[0]);
					int priceGrade = Integer
							.valueOf(returnString.split(";")[1]);
					int maxBuysFrequentness = Integer.valueOf(returnString
							.split(";")[2]);
					String month = data[1].split("-")[1];
					int monthRight = -1;
					if (buyMaxMonth.containsKey(data[2])) { // 如果buy也包含clickhasbuy中的项目
						if (buyMaxMonth.get(data[2]).equals(month)) {
							monthRight = 1; // 这是商品销售旺季
						} else {
							monthRight = 0;
						}
					}
					month = String.valueOf(monthRight) + "M";
					int monthLen = -1;
					if (buyMonthLen.containsKey(data[2])) {
						monthLen = buyMonthLen.get(data[2]); // 将此项目购买跨越的月份赋值给monthLen
					}
					bw.write(String.valueOf(clickNumber) + ","
							+ String.valueOf(popularOrNot) + ","
							+ String.valueOf(repeat) + ","
							+ String.valueOf(priceGrade) + "," + categoryValue
							+ "," + String.valueOf(maxBuysFrequentness) + ","
							+ month + "," + String.valueOf(monthLen) + ",?"
							+ "\n");

						bw_T_sessionId.write(String.valueOf(sessionId) + "\n");
					
					beginTime = data[1];
					sessionId = data[0];
				}
				clickNumber = 0;
				popularOrNot = 0;
				int maxBuysFrequentness = 0;
				clickInfo.clear(); // 万万没想到!!!
				// s.clear();

			} else { // 若sessionId== data[0]:
				endTime = data[1];
				if (popularItem.containsKey(data[2]))
					popularOrNot = 1;
			}
			if (clickInfo.containsKey(data[2])) { // clickInfo能够统计hasBuyData中出现的项目及其次数
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
			clickNumber += 1;
			// s.put(data[2],1);//
		
		} // 对应最外面的while读的循环
		br_test.close();
		bw.close();
		br_category.close();
		bw_T_sessionId.close();
		long e = System.currentTimeMillis();
		System.out.println("\t耗时:" + (e - b)/1000 + "s");
	}

}
