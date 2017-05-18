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
	 * 测试模块getPopularItem public static void main(String args[]) throws
	 * IOException { // 函数模块测试 Map map = new HashMap<>(); map =
	 * feature_function.getPopularItem(); Iterator iter =
	 * map.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet() //
	 * 转化成map的Set视图，在调用迭代器方法产生迭代器 while (iter.hasNext()) { // 接口
	 * Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图， // 其中的元素属于此类
	 * // clickInfo能够统计hasBuyData中出现的项目及其次数#itemPrice能够统计buy中的项目及其价格 Map.Entry
	 * entry = (Map.Entry) iter.next(); String key = (String) entry.getKey();//
	 * Integer val = (Integer) entry.getValue(); System.out.println(key + ":" +
	 * val); } }
	 * 
	 * 测试时主要是出现了文件读写指针的问题，当BufferedReader读到文件末尾时需重置一下读指针，方法见代码!!!
	 * 测试模块getPopularItem
	 **/

	// 得到流行项目的字典// getPopularItem():popularItem:1的map
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
		// 此时已经读到了BufferWriter对应文件的末尾,需重置文件读写指针
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
			PopularItem_map.put(string2.split("\t")[0], 1);// popularItem:1的map
		}

		br.close();
		return PopularItem_map;
	}

	public HashMap<String, Integer> getBuysFrequentness(String buyFile)// #map存储的是buy中的项目:购买次数的字典
			throws NumberFormatException, IOException {
		FileReader fr = new FileReader(buyFile);
		BufferedReader br = new BufferedReader(fr);

		HashMap<String, Integer> buysFrequentness_map = new HashMap<String, Integer>();
		String string = null;
		while ((string = br.readLine()) != null) {
			buysFrequentness_map.put(string.split("\t")[0],
					Integer.valueOf(string.split("\t")[1]));
			// buysFrequentnessFile存储的是buy中的项目:购买次数的字典/map
		}
		br.close();
		return buysFrequentness_map;

	}

	public static HashMap<String, String> getDicFromFile(String fileName)
			throws IOException {
		String string = null;
		HashMap<String, String> map = new HashMap<String, String>(); // /////map的形式后面还要查
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
		HashMap<String, Integer> map = new HashMap<String, Integer>(); // /////map的形式后面还要查
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
			endHour = endHour + 24; // 如果开始的时间反而在前面则加上24小时
		return (endHour - startHour) * 60 + (endMinute - startMinute); // #相差的分钟数
	}

	public int calculateWeekTime(String time) {// 计算属于星期几
		int monthWeekDay[] = new int[10];
		monthWeekDay[4] = 2; // 4月1日是星期二
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
	 * 计算是否有重复点击，并返回价格区间
	 * #clickInfo能够统计hasBuyData中出现的项目及其次数#itemPrice能够统计buy中的项目及其价格
	 */
	public String repeatOrNot(HashMap<String, Integer> clickInfo,
			HashMap<String, Integer> itemPrice, int minPrice, int maxPrice,
			HashMap<String, Integer> buysFrequentness) {
		int maxBuysFrequentness = 0;
		int grade = -1; // grade返回的最终是项目出现次数最大的那个价格级

		// Hashmap中按值排序
		List<Map.Entry<String, Integer>> info = new ArrayList<Map.Entry<String, Integer>>(
				clickInfo.entrySet());
		Collections.sort(info, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> obj1,
					Map.Entry<String, Integer> obj2) {
				return obj2.getValue() - obj1.getValue(); // 按项目的出现次数从大到小排序
			}
		});

		while (true) {//
			String clickInfo_key = info.get(0).getKey();
			Integer clickInfo_val = info.get(0).getValue();

			// clickInfo能够统计hasBuyData中出现的项目及其次数
			if (clickInfo_val > 1) { // 值
				if (itemPrice.containsKey(clickInfo_key)) { // 如果buy中也有这个项目
					int itemPrice_val = (int) itemPrice.get(clickInfo_key);// buy中相应项目的价格
					grade = getPriceGrade(itemPrice_val, minPrice, maxPrice); // 注意这里还要传值
				} else {
					grade = -1; // 表示缺失即hasBuyData中有这个项目且出现次数大于1但buy中未出现
				}

			} else {// hasBuyData中相应的项目但次数小于1
				grade = getMostGrade(clickInfo, itemPrice, minPrice, maxPrice);

				// 若hasBuyData中相应的项目出现的次数不大于1??????????
			}
			break;
		}
		int repeatNumber = 0;

		Iterator iter = clickInfo.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()
		// 转化成map的Set视图，在调用迭代器方法产生迭代器
		while (iter.hasNext()) {
			// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图，
			// 其中的元素属于此类
			// clickInfo能够统计hasBuyData中出现的项目及其次数#itemPrice能够统计buy中的项目及其价格
			Map.Entry entry = (Map.Entry) iter.next();
			String key = (String) entry.getKey();//
			Integer val = (Integer) entry.getValue();
			if (val > 1) {// 如果buy文件中也有这个项目
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
		int grade = -1;// 默认价格级为-1;
		HashMap<Integer, Integer> mostGrade_map = new HashMap<>();
		
		Iterator iter = clickInfo.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()
		// 转化成map的Set视图，在调用迭代器方法产生迭代器
		while (iter.hasNext()) {
			// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图，
			// 其中的元素属于此类

			Map.Entry entry = (Map.Entry) iter.next();
			String key = (String) entry.getKey();
			Integer val = (Integer) entry.getValue();
			if (itemPrice.containsKey(key)) {// 如果buy文件中也有这个项目
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
		// 将mostGrade_map按值从大到小排序
		// Hashmap中按值排序
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
		// categoryInfo能够统计hasBuyData中出现的项目的类别及类别出现次数
		if (categoryInfo.size() == 0)
			return "0C";

		// Hashmap中按值排序的方法
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

	public static List getItemPrice() throws IOException {// 返回集合系列
		int maxPrice = 0;
		int price;
		int minPrice = 10000000;
		String string = null;
		String data[];
		String itemId;
		HashMap<String, Integer> itemPrice_map = new HashMap<>(); // Hashmap的形式要加以注意
		FileReader fw = new FileReader("E:\\Data\\yoochoose-buys.dat");
		BufferedReader br = new BufferedReader(fw);
		while ((string = br.readLine()) != null) {
			data = string.split(",");
			itemId = data[2];
			price = Integer.valueOf(data[3]);
			if (price > 0) {// 如果价格不为缺省值
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
		// *用list效率太低,用固定数组就好
		List list = new ArrayList<>();// ArrayList长于随机访问元素
		list.add(itemPrice_map);
		list.add(minPrice);
		list.add(maxPrice);
		return list;

	}

}
