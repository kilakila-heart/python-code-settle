package Classification_of_post_processing;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class differentpricecommodity {
//static int count=0;
	
	public static void main(String[] args) throws IOException {
		HashMap map = new HashMap();
		File file = new File("D://厦大任务//中间数据//buy中不同价格的商品在Session中出现的次数.txt");
		FileInputStream fileInputStream = new FileInputStream(file);
		BufferedInputStream bufferedInputStream = new BufferedInputStream(
				fileInputStream);

		InputStreamReader inputStreamReader = new InputStreamReader(
				bufferedInputStream);
		BufferedReader input = new BufferedReader(inputStreamReader);

		FileWriter output = new FileWriter("c://output2_3" + ".txt");
		int bufferSize = 20 * 1024 * 1024;// 设读取文件的缓存为20MB
		BufferedWriter output1 = new BufferedWriter(output, bufferSize);

		StringBuilder strb = new StringBuilder();//动态字符串
		while (true) {
			int line = input.read();

			if (line== -1) {
				break;
			}
			// strb.append(line);
			// String result = strb.toString();
			/*int maxSplit = 2;
			String[] sourceStrArray = line.split("\t" , 2);
		
				
				
			// for(int i=0;i<sourceStrArray.length;i++)
			// {
			// System.out.println(sourceStrArray[0]);
			// HashMap map = new HashMap();
			String keyStr = sourceStrArray[0].trim();
			if (keyStr.length() >= 0) {            //字符串的长度>0;
				// int keyInt = Integer.parseInt(keyStr);
				String keyInt = keyStr;//对值出现的次数进行计数
				if (!map.containsKey(keyInt))
					map.put(keyInt, 1);
				else {
					int i = (int) map.get(keyInt);
					map.put(keyInt, ++i);
				}
			}
			// }

		}
		Iterator iter = map.entrySet().iterator();//为了使用map的迭代器要使用map.entrySet()
		while (iter.hasNext()) {
			Map.Entry entry = (Map.Entry) iter.next();
			Object key = entry.getKey();
			Object val = entry.getValue();
			System.out.println(key + "出现次" + val);
			output1.write(key + "\t" + val);

			output1.newLine();//每迭代输出一次换一行
			System.out.println();
			output1.flush();//清空缓冲区

		}
		output1.close();//关闭缓冲区
			/*/
	}


		
	}}

