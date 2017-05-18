package DataAnalyse;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class generateCategoryValue {
	public static void main(String args[]) throws IOException {
		generateCategoryValue GCV = new generateCategoryValue();
		GCV.generateCategoryFile("E:\\Data\\yoochoose-clicks.dat",
				"E:\\Data\\yoochoose-category.dat");
	}

	private Map generateCategoryFile(String clickFile, String categoryfile)
			throws IOException {
		int i = 0;
		String string = null;
		String categoryId;
		String data[];
		FileReader fr = new FileReader(clickFile);
		BufferedReader br = new BufferedReader(fr);

		FileWriter fw = new FileWriter(categoryfile);
		BufferedWriter bw = new BufferedWriter(fw);
		HashMap category_map = new HashMap<>();
		while ((string = br.readLine()) != null) {
			i++;
			if (i % 1000000 == 0)
				System.out.println(i);
			data = string.split(",");
			categoryId = data[3].trim();// trim()类似于py中的strip()
			if (categoryId.length() > 3)
				categoryId = "-1C";
			categoryId = categoryId + "C";

			category_map.put(data[2], categoryId);

		}

		Iterator iter = category_map.entrySet().iterator();// 为了使用map的迭代器要使用map.entrySet()
		// 转化成map的Set视图，在调用迭代器方法产生迭代器
		while (iter.hasNext()) {
			// 接口 Map.Entry<K,V>映射项（键-值对）。Map.entrySet 方法返回映射的 collection 视图，
			// 其中的元素属于此类

			Map.Entry entry = (Map.Entry) iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			bw.write(key + "\t" + val);

			bw.newLine();// 每迭代输出一次换一行

			bw.flush();// 清空缓冲区

		}

		bw.close();

		br.close();
		bw.close();
		// System.out.println(category_map);
		return category_map;

	}

}
