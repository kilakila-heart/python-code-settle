package generateFeature;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public final class feature_function {
	/**
	 * ����ģ��getPopularItem public static void main(String args[]) throws
	 * IOException { // ����ģ����� Map map = new HashMap<>(); map =
	 * feature_function.getPopularItem(); Iterator iter =
	 * map.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet() //
	 * ת����map��Set��ͼ���ڵ��õ������������������� while (iter.hasNext()) { // �ӿ�
	 * Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ�� // ���е�Ԫ�����ڴ���
	 * // clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������#itemPrice�ܹ�ͳ��buy�е���Ŀ����۸� Map.Entry
	 * entry = (Map.Entry) iter.next(); String key = (String) entry.getKey();//
	 * Integer val = (Integer) entry.getValue(); System.out.println(key + ":" +
	 * val); } }
	 * 
	 * ����ʱ��Ҫ�ǳ������ļ���дָ������⣬��BufferedReader�����ļ�ĩβʱ������һ�¶�ָ�룬����������!!!
	 * ����ģ��getPopularItem
	 **/

	// �õ�������Ŀ���ֵ�// getPopularItem():popularItem:1��map
	public static HashMap<String, Integer> getPopularItem() throws IOException {
		HashMap<String, Integer> PopularItem_map = new HashMap<String, Integer>();
		FileReader fr = new FileReader(
				"E:\\Data\\yoochoose-buys-analyse-sorted.dat");
		BufferedReader br = new BufferedReader(fr);
		int number = 0;
		int threadNumber = 0;
		String string = null;
		while ((string = br.readLine()) != null) {
			number += Integer.valueOf(string.split("\t")[1]);
		}
		// ��ʱ�Ѿ�������BufferWriter��Ӧ�ļ���ĩβ,�������ļ���дָ��
		System.out.println("number:" + number);
		threadNumber = number * 9 / 10;
		// br.reset();

		fr = new FileReader("E:\\Data\\yoochoose-buys-analyse-sorted.dat");
		br = new BufferedReader(fr);

		int number2 = 0;
		String string2 = null;

		while ((string2 = br.readLine()) != null) {
			number2 += Integer.valueOf(string2.split("\t")[1]);
			if (number2 > threadNumber)
				break;
			PopularItem_map.put(string2.split("\t")[0], 1);// popularItem:1��map
		}

		br.close();
		return PopularItem_map;
	}

	public HashMap<String, Integer> getBuysFrequentness(String buyFile)// #map�洢����buy�е���Ŀ:����������ֵ�
			throws NumberFormatException, IOException {
		FileReader fr = new FileReader(buyFile);
		BufferedReader br = new BufferedReader(fr);

		HashMap<String, Integer> buysFrequentness_map = new HashMap<String, Integer>();
		String string = null;
		while ((string = br.readLine()) != null) {
			buysFrequentness_map.put(string.split("\t")[0],
					Integer.valueOf(string.split("\t")[1]));
			// buysFrequentnessFile�洢����buy�е���Ŀ:����������ֵ�/map
		}
		br.close();
		return buysFrequentness_map;

	}

	public static HashMap<String, String> getDicFromFile(String fileName)
			throws IOException {
		String string = null;
		HashMap<String, String> map = new HashMap<String, String>(); // /////map����ʽ���滹Ҫ��
		FileReader fr = new FileReader(fileName);
		BufferedReader br = new BufferedReader(fr);
		while ((string = br.readLine()) != null) {
			map.put(string.split("\t")[0], string.split("\t")[1]);
		}
		br.close();
		return map;
	}

	public static HashMap<String, Integer> getDicFromFile_Integer(
			String fileName) throws IOException {
		String string = null;
		HashMap<String, Integer> map = new HashMap<String, Integer>(); // /////map����ʽ���滹Ҫ��
		FileReader fr = new FileReader(fileName);
		BufferedReader br = new BufferedReader(fr);
		while ((string = br.readLine()) != null) {
			map.put(string.split("\t")[0],
					Integer.valueOf(string.split("\t")[1]));
		}
		br.close();
		return map;
	}

	public int calculateTime(String start, String end) {
		String[] startData = start.split(":");
		int startHour = Integer.valueOf(startData[0].split("T")[1]);
		int startMinute = Integer.valueOf(startData[1]);
		String[] endData = end.split(":");
		int endHour = Integer.valueOf(endData[0].split("T")[1]);
		int endMinute = Integer.valueOf(endData[1]);
		if (startHour > endHour)
			endHour = endHour + 24; // �����ʼ��ʱ�䷴����ǰ�������24Сʱ
		return (endHour - startHour) * 60 + (endMinute - startMinute); // #���ķ�����
	}

	public int calculateWeekTime(String time) {// �����������ڼ�
		int monthWeekDay[] = new int[10];
		monthWeekDay[4] = 2; // 4��1�������ڶ�
		monthWeekDay[5] = 4;
		monthWeekDay[6] = 7;
		monthWeekDay[7] = 2;
		monthWeekDay[8] = 5;
		monthWeekDay[9] = 1;
		String[] data = time.split("-");
		int day = Integer.valueOf(data[2].split("T")[0]);
		return ((day - 1) + monthWeekDay[Integer.valueOf(data[1])]) % 7;
	}

	/*
	 * �����Ƿ����ظ�����������ؼ۸�����
	 * #clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������#itemPrice�ܹ�ͳ��buy�е���Ŀ����۸�
	 */
	public String repeatOrNot(HashMap<String, Integer> clickInfo,
			HashMap<String, Integer> itemPrice, int minPrice, int maxPrice,
			HashMap<String, Integer> buysFrequentness) {
		int maxBuysFrequentness = 0;
		int grade = -1; // grade���ص���������Ŀ���ִ��������Ǹ��۸�

		// Hashmap�а�ֵ����
		List<Map.Entry<String, Integer>> info = new ArrayList<Map.Entry<String, Integer>>(
				clickInfo.entrySet());
		Collections.sort(info, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> obj1,
					Map.Entry<String, Integer> obj2) {
				return obj2.getValue() - obj1.getValue(); // ����Ŀ�ĳ��ִ����Ӵ�С����
			}
		});

		while (true) {//
			String clickInfo_key = info.get(0).getKey();
			Integer clickInfo_val = info.get(0).getValue();

			// clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������
			if (clickInfo_val > 1) { // ֵ
				if (itemPrice.containsKey(clickInfo_key)) { // ���buy��Ҳ�������Ŀ
					int itemPrice_val = (int) itemPrice.get(clickInfo_key);// buy����Ӧ��Ŀ�ļ۸�
					grade = getPriceGrade(itemPrice_val, minPrice, maxPrice); // ע�����ﻹҪ��ֵ
				} else {
					grade = -1; // ��ʾȱʧ��hasBuyData���������Ŀ�ҳ��ִ�������1��buy��δ����
				}

			} else {// hasBuyData����Ӧ����Ŀ������С��1
				grade = getMostGrade(clickInfo, itemPrice, minPrice, maxPrice);

				// ��hasBuyData����Ӧ����Ŀ���ֵĴ���������1??????????
			}
			break;
		}
		int repeatNumber = 0;

		Iterator iter = clickInfo.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()
		// ת����map��Set��ͼ���ڵ��õ�������������������
		while (iter.hasNext()) {
			// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ��
			// ���е�Ԫ�����ڴ���
			// clickInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ�������#itemPrice�ܹ�ͳ��buy�е���Ŀ����۸�
			Map.Entry entry = (Map.Entry) iter.next();
			String key = (String) entry.getKey();//
			Integer val = (Integer) entry.getValue();
			if (val > 1) {// ���buy�ļ���Ҳ�������Ŀ
				if (buysFrequentness.containsKey(key)) {
					Integer buysFrequentness_val = (Integer) buysFrequentness
							.get(key);
					if (buysFrequentness_val > maxBuysFrequentness) {
						maxBuysFrequentness = buysFrequentness_val;
					}
				}
				repeatNumber++;
			} //
		}
		return String.valueOf(repeatNumber) + ";" + String.valueOf(grade) + ";"
				+ String.valueOf(maxBuysFrequentness);
	}

	public int getPriceGrade(int price, int minPrice, int maxPrice) {
		return (int) Math.log10(price + 1);
	}

	public int getMostGrade(Map clickInfo, Map itemPrice, int minPrice,
			int maxPrice) {
		int grade = -1;// Ĭ�ϼ۸�Ϊ-1;
		HashMap<Integer, Integer> mostGrade_map = new HashMap<>();
		
		Iterator iter = clickInfo.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()
		// ת����map��Set��ͼ���ڵ��õ�������������������
		while (iter.hasNext()) {
			// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ��
			// ���е�Ԫ�����ڴ���

			Map.Entry entry = (Map.Entry) iter.next();
			String key = (String) entry.getKey();
			Integer val = (Integer) entry.getValue();
			if (itemPrice.containsKey(key)) {// ���buy�ļ���Ҳ�������Ŀ
				int itemPrice_val = (int) itemPrice.get(key);
				grade = getPriceGrade(itemPrice_val, minPrice, maxPrice);
				if (mostGrade_map.containsKey(grade)) {
					int i = (int) mostGrade_map.get(grade);
					mostGrade_map.put(grade, ++i);
				} else {
					mostGrade_map.put(grade, 1);
				}
			}
		}
		if (mostGrade_map.size() == 0)
			return -1;
		// ��mostGrade_map��ֵ�Ӵ�С����
		// Hashmap�а�ֵ����
		List<Map.Entry<Integer, Integer>> mostGrade_map_info = new ArrayList<Map.Entry<Integer, Integer>>(
				mostGrade_map.entrySet());
		Collections.sort(mostGrade_map_info,
				new Comparator<Map.Entry<Integer, Integer>>() {
					public int compare(Map.Entry<Integer, Integer> obj1,
							Map.Entry<Integer, Integer> obj2) {
						return obj2.getValue() - obj1.getValue();
					}
				});

		return mostGrade_map_info.get(0).getKey();

	}

	public String getCategoryValue(Map categoryInfo) { // {04=2, 06=1, 07=9}
		// categoryInfo�ܹ�ͳ��hasBuyData�г��ֵ���Ŀ����������ִ���
		if (categoryInfo.size() == 0)
			return "0C";

		// Hashmap�а�ֵ����ķ���
		// http://www.blogjava.net/freeman1984/archive/2011/08/23/357121.html
		List<Map.Entry<String, Integer>> info = new ArrayList<Map.Entry<String, Integer>>(
				categoryInfo.entrySet());
		Collections.sort(info, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> obj1,
					Map.Entry<String, Integer> obj2) {
				return obj2.getValue() - obj1.getValue();
			}
		});
		/*
		 * for (int j = 0; j<info.size();j++) { // info.get(j).getKey() + "\t" +
		 * info.get(j).getValue()); }
		 */
		// System.out.println(info.get(0).getKey());
		return info.get(0).getKey();

	}

	public static List getItemPrice() throws IOException {// ���ؼ���ϵ��
		int maxPrice = 0;
		int price;
		int minPrice = 10000000;
		String string = null;
		String data[];
		String itemId;
		HashMap<String, Integer> itemPrice_map = new HashMap<>(); // Hashmap����ʽҪ����ע��
		FileReader fw = new FileReader("E:\\Data\\yoochoose-buys.dat");
		BufferedReader br = new BufferedReader(fw);
		while ((string = br.readLine()) != null) {
			data = string.split(",");
			itemId = data[2];
			price = Integer.valueOf(data[3]);
			if (price > 0) {// ����۸�Ϊȱʡֵ
				if (itemPrice_map.containsKey(itemId)) {
					if (price > itemPrice_map.get(itemId)) {
						itemPrice_map.put(itemId, price);
					}
				} else {
					itemPrice_map.put(itemId, price);
				}
			}
			if (price > maxPrice)
				maxPrice = price;
			if (price < minPrice)
				minPrice = price;
		}
		/*
		 * Object arr[]=new Object[3]; arr[0]=itemPrice_map; arr[1]=minPrice;
		 * arr[2]=maxPrice; return arr;
		 */
		// *��listЧ��̫��,�ù̶�����ͺ�
		List list = new ArrayList<>();// ArrayList�����������Ԫ��
		list.add(itemPrice_map);
		list.add(minPrice);
		list.add(maxPrice);
		return list;

	}

}
