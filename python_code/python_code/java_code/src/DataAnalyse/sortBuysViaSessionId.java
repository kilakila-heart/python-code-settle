package DataAnalyse;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class sortBuysViaSessionId {
	public void sortBuysViaSessionIdfunction(String infile, String outfile)
			throws IOException {
		//

		String string = null;

		List<String> list = new ArrayList<String>();

		FileReader fr = new FileReader(infile);
		BufferedReader br = new BufferedReader(fr);

		FileWriter fw = new FileWriter(outfile);
		BufferedWriter bw = new BufferedWriter(fw);
		while ((string = br.readLine()) != null) {
			list.add(string);

		}

		Collections.sort(list, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				if (Integer.valueOf(o1.split(",")[0]) < Integer.valueOf(o2
						.split(",")[0])) {
					return -1;
				}
				if (Integer.valueOf(o1.split(",")[0]) > Integer.valueOf(o2
						.split(",")[0])) {
					return 1;
				}

				return 0;
			}

		});
		for (int i = 0; i < list.size(); i++) {

			bw.write(list.get(i));//如果这里也加一，则可以实现抽样
			bw.newLine();
			if(i%1000==0) System.out.println(i);
		}
		bw.close();
	}

	public static void main(String args[]) throws IOException {
		sortBuysViaSessionId sViaSessionId = new sortBuysViaSessionId();
		sViaSessionId.sortBuysViaSessionIdfunction("E:\\Data\\yoochoose-buys.dat","E:\\Data\\yoochoose-buys-sorted.dat");
		//sViaSessionId.sortBuysViaSessionIdfunction("D:\\Data\\yoochoose-buys.dat","D:\\Data\\yoochoose-buys-sorted.dat");
		System.out.println("ok");
	}
}
