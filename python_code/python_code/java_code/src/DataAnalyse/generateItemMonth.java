package DataAnalyse;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class generateItemMonth {
	public static void main(String args[]) throws IOException {
		generateItemMonth obj = new generateItemMonth();
		obj.ItemMonth_function("e:\\Data\\yoochoose-buys.dat",
				"e:\\Data\\yoochoose-buyMaxMonth.dat",
				"e:\\Data\\yoochoose-buyMonthLen.dat");
	}

	private void ItemMonth_function(String file_buys, String file_buyMaxMonth,
			String file_buyMonthLen) throws IOException {
		List<Map> list = new ArrayList<>();

		HashMap buyMonthDis = new HashMap<>();

		HashMap buyMaxMonthDis = new HashMap<>();
		HashMap buyMonthLen = new HashMap<>();
		int i = 0;
		String string = null;
		String month; // 用int还是String后面看一下
		String data[] = null;
		String itemIdNow;
		int maxNumber = 0;
		String maxMonth;
		FileReader fr = new FileReader(file_buys);
		BufferedReader br_buy = new BufferedReader(fr);

		FileWriter fr1 = new FileWriter(file_buyMaxMonth);
		BufferedWriter br_buyMaxMonth = new BufferedWriter(fr1);

		FileWriter fr2 = new FileWriter(file_buyMonthLen);
		BufferedWriter br_buyMonthLen = new BufferedWriter(fr2);

		while ((string = br_buy.readLine()) != null) {
			HashMap map = new HashMap<>();
			data = string.split(",");
			month = (data[1].split("-")[1]);
			itemIdNow = data[2];// 表示项目
			if (!buyMonthDis.containsKey(itemIdNow)) {
				buyMonthDis.put(itemIdNow, map); // Bigmap相当于buyMonthDis{}
				// System.out.println(buyMonthDis);
				if (map.containsKey(month)) {
					// System.out.println(buyMonthDis);
					map.put(month, ++i);
				}
				if (!map.containsKey(month)) {
					map.put(month, 1);// 即买的最多的那个月份
				}
				// System.out.println(buyMonthDis);
				continue;
			}

			if (buyMonthDis.containsKey(itemIdNow)) {
				map = (HashMap) buyMonthDis.get(itemIdNow);
				if (map.containsKey(month)) {

					map.put(month, ++i);
				}
				if (!map.containsKey(month)) {
					map.put(month, 1);// 即买的最多的那个月份
				}
				// System.out.println(buyMonthDis);
			}

		}
		// System.out.println(buyMonthDis);
		Iterator Bigiter = buyMonthDis.entrySet().iterator();

		while (Bigiter.hasNext()) {
			Map.Entry Bigentry = (Map.Entry) Bigiter.next();
			String Bigkey = String.valueOf(Bigentry.getKey()); // 得到key-------itemIdNow
			Map Bigval = (Map) Bigentry.getValue();
			Iterator iter = Bigval.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()

			while (iter.hasNext()) {
				// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection
				// 视图，
				// 其中的元素属于此类

				maxMonth = "-1";
				maxNumber = 0;
				Map.Entry entry = (Map.Entry) iter.next();
				String key = (String) entry.getKey();// 键表示月份
				Integer val = (Integer) entry.getValue();// 值表示次数
				System.out.println(key + "出现次" + val);
				if (val > maxNumber) {
					maxNumber = val;
					maxMonth = key;
				}
				if (!iter.hasNext())
					buyMaxMonthDis.put(Bigkey, key); // 常用技巧!!!!! 对了
			}
			// System.out.println(buyMonthDis);
			buyMonthLen.put(Bigkey, Bigval.size());//

		}

		Iterator buyMaxMonthDis_iter = buyMaxMonthDis.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()
		// 转化成map的Set视图，在调用迭代器方法产生迭代器
		while (buyMaxMonthDis_iter.hasNext()) {
			// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图，
			// 其中的元素属于此类

			Map.Entry entry = (Map.Entry) buyMaxMonthDis_iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			br_buyMaxMonth.write(key + "\t" + val);

			br_buyMaxMonth.newLine();// 每迭代输出一次换一行

			br_buyMaxMonth.flush();// 清空缓冲区

		}

		Iterator buyMonthLen_iter = buyMonthLen.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()
		// 转化成map的Set视图，在调用迭代器方法产生迭代器
		while (buyMonthLen_iter.hasNext()) {
			// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图，
			// 其中的元素属于此类

			Map.Entry entry = (Map.Entry) buyMonthLen_iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			br_buyMonthLen.write(key + "\t" + val);

			br_buyMonthLen.newLine();// 每迭代输出一次换一行

		}

		br_buyMonthLen.close();
		br_buyMaxMonth.close();// 关闭缓冲区

	}
}
