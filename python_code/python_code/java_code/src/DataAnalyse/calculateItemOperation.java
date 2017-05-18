package DataAnalyse;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

import java.io.FileReader;
import java.io.FileWriter;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;

import java.util.List;
import java.util.Map;

public class calculateItemOperation {
	public void calculateItemOperation_function(String inFile, String outFile)
			throws IOException {
		HashMap map = new HashMap();
		

		// 为了可能对大文件的写入，设置缓冲区还是必要的
		int bufferSize = 20 * 1024 * 1024;// 设读取文件的缓存为20MB

		FileWriter fw = new FileWriter(outFile);
		BufferedWriter bw = new BufferedWriter(fw, bufferSize);

		FileReader fr = new FileReader(inFile);
		BufferedReader br = new BufferedReader(fr, bufferSize);

		StringBuilder strb = new StringBuilder();// 动态字符串
		while (true) {
			String line = br.readLine();
			if (line == null) {
				break;
			}
			int maxSplit = 4;// 移植时可能要随文件的不同而改变
			//int maxSplit = 5;
			String[] sourceStrArray = line.split(",", maxSplit);
			String keyStr = sourceStrArray[2].trim();

			if (keyStr.length() > 0) { // 字符串的长度>0;
				// int keyInt = Integer.parseInt(keyStr);
				String keyInt = keyStr;// 对值出现的次数进行计数
				if (!map.containsKey(keyInt))
					map.put(keyInt, 1);
				else {
					int i = (int) map.get(keyInt);
					map.put(keyInt, ++i);
				}
			}
			

		}
	//Hashmap中按值排序的方法
	//http://www.blogjava.net/freeman1984/archive/2011/08/23/357121.html
		List<Map.Entry<String, Integer>> info = new ArrayList<Map.Entry<String, Integer>>(map.entrySet());
        Collections.sort(info, new Comparator<Map.Entry<String, Integer>>() {
            public int compare(Map.Entry<String, Integer> obj1, Map.Entry<String, Integer> obj2) {
                return obj2.getValue() - obj1.getValue();
            }
        });

        for (int j = 0; j<info.size();j++) {
            bw.write(info.get(j).getKey() + "\t" + info.get(j).getValue());
            bw.newLine();
            if(j%1000==0) System.out.println(j);
        }
        
        
    	bw.flush();// 清空缓冲区
		bw.close();// 关闭缓冲区
		br.close();
    }
	
	
	public static void main(String args[]) throws IOException {
		calculateItemOperation cal=new calculateItemOperation();
	//	cal.calculateItemOperation_function("E:\\Data\\yoochoose-clicks.dat","E:\\Data\\yoochoose-clicks-analyse-sorted.dat");
		cal.calculateItemOperation_function("E:\\Data\\yoochoose-buys.dat","E:\\Data\\yoochoose-buys-analyse-sorted.dat");	
		
	}
}
