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
		String month; // ��int����String���濴һ��
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
			itemIdNow = data[2];// ��ʾ��Ŀ
			if (!buyMonthDis.containsKey(itemIdNow)) {
				buyMonthDis.put(itemIdNow, map); // Bigmap�൱��buyMonthDis{}
				// System.out.println(buyMonthDis);
				if (map.containsKey(month)) {
					// System.out.println(buyMonthDis);
					map.put(month, ++i);
				}
				if (!map.containsKey(month)) {
					map.put(month, 1);// ����������Ǹ��·�
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
					map.put(month, 1);// ����������Ǹ��·�
				}
				// System.out.println(buyMonthDis);
			}

		}
		// System.out.println(buyMonthDis);
		Iterator Bigiter = buyMonthDis.entrySet().iterator();

		while (Bigiter.hasNext()) {
			Map.Entry Bigentry = (Map.Entry) Bigiter.next();
			String Bigkey = String.valueOf(Bigentry.getKey()); // �õ�key-------itemIdNow
			Map Bigval = (Map) Bigentry.getValue();
			Iterator iter = Bigval.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()

			while (iter.hasNext()) {
				// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection
				// ��ͼ��
				// ���е�Ԫ�����ڴ���

				maxMonth = "-1";
				maxNumber = 0;
				Map.Entry entry = (Map.Entry) iter.next();
				String key = (String) entry.getKey();// ����ʾ�·�
				Integer val = (Integer) entry.getValue();// ֵ��ʾ����
				System.out.println(key + "���ִ�" + val);
				if (val > maxNumber) {
					maxNumber = val;
					maxMonth = key;
				}
				if (!iter.hasNext())
					buyMaxMonthDis.put(Bigkey, key); // ���ü���!!!!! ����
			}
			// System.out.println(buyMonthDis);
			buyMonthLen.put(Bigkey, Bigval.size());//

		}

		Iterator buyMaxMonthDis_iter = buyMaxMonthDis.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()
		// ת����map��Set��ͼ���ڵ��õ�������������������
		while (buyMaxMonthDis_iter.hasNext()) {
			// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ��
			// ���е�Ԫ�����ڴ���

			Map.Entry entry = (Map.Entry) buyMaxMonthDis_iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			br_buyMaxMonth.write(key + "\t" + val);

			br_buyMaxMonth.newLine();// ÿ�������һ�λ�һ��

			br_buyMaxMonth.flush();// ��ջ�����

		}

		Iterator buyMonthLen_iter = buyMonthLen.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()
		// ת����map��Set��ͼ���ڵ��õ�������������������
		while (buyMonthLen_iter.hasNext()) {
			// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ��
			// ���е�Ԫ�����ڴ���

			Map.Entry entry = (Map.Entry) buyMonthLen_iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			br_buyMonthLen.write(key + "\t" + val);

			br_buyMonthLen.newLine();// ÿ�������һ�λ�һ��

		}

		br_buyMonthLen.close();
		br_buyMaxMonth.close();// �رջ�����

	}
}
