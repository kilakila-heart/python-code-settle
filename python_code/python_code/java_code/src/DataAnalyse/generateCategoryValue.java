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
			categoryId = data[3].trim();// trim()������py�е�strip()
			if (categoryId.length() > 3)
				categoryId = "-1C";
			categoryId = categoryId + "C";

			category_map.put(data[2], categoryId);

		}

		Iterator iter = category_map.entrySet().iterator();// Ϊ��ʹ��map�ĵ�����Ҫʹ��map.entrySet()
		// ת����map��Set��ͼ���ڵ��õ�������������������
		while (iter.hasNext()) {
			// �ӿ� Map.Entry<K,V>ӳ�����-ֵ�ԣ���Map.entrySet ��������ӳ��� collection ��ͼ��
			// ���е�Ԫ�����ڴ���

			Map.Entry entry = (Map.Entry) iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();

			bw.write(key + "\t" + val);

			bw.newLine();// ÿ�������һ�λ�һ��

			bw.flush();// ��ջ�����

		}

		bw.close();

		br.close();
		bw.close();
		// System.out.println(category_map);
		return category_map;

	}

}
