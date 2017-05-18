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
		

		// Ϊ�˿��ܶԴ��ļ���д�룬���û��������Ǳ�Ҫ��
		int bufferSize = 20 * 1024 * 1024;// ���ȡ�ļ��Ļ���Ϊ20MB

		FileWriter fw = new FileWriter(outFile);
		BufferedWriter bw = new BufferedWriter(fw, bufferSize);

		FileReader fr = new FileReader(inFile);
		BufferedReader br = new BufferedReader(fr, bufferSize);

		StringBuilder strb = new StringBuilder();// ��̬�ַ���
		while (true) {
			String line = br.readLine();
			if (line == null) {
				break;
			}
			int maxSplit = 4;// ��ֲʱ����Ҫ���ļ��Ĳ�ͬ���ı�
			//int maxSplit = 5;
			String[] sourceStrArray = line.split(",", maxSplit);
			String keyStr = sourceStrArray[2].trim();

			if (keyStr.length() > 0) { // �ַ����ĳ���>0;
				// int keyInt = Integer.parseInt(keyStr);
				String keyInt = keyStr;// ��ֵ���ֵĴ������м���
				if (!map.containsKey(keyInt))
					map.put(keyInt, 1);
				else {
					int i = (int) map.get(keyInt);
					map.put(keyInt, ++i);
				}
			}
			

		}
	//Hashmap�а�ֵ����ķ���
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
        
        
    	bw.flush();// ��ջ�����
		bw.close();// �رջ�����
		br.close();
    }
	
	
	public static void main(String args[]) throws IOException {
		calculateItemOperation cal=new calculateItemOperation();
	//	cal.calculateItemOperation_function("E:\\Data\\yoochoose-clicks.dat","E:\\Data\\yoochoose-clicks-analyse-sorted.dat");
		cal.calculateItemOperation_function("E:\\Data\\yoochoose-buys.dat","E:\\Data\\yoochoose-buys-analyse-sorted.dat");	
		
	}
}
