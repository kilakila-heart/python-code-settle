package DataAnalyse;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;

public class generateClicksHasBuys {
	public static void main(String args[]) throws IOException {
		generateClicksHasBuys  genClickHasBuy=new generateClicksHasBuys();
		genClickHasBuy.generateClicksHasBuys_function("E:\\Data\\yoochoose-buys.dat","E:\\Data\\yoochoose-clicks.dat",
	"E:\\Data\\yoochoose-clicks-hasBuyData.dat","E:\\Data\\yoochoose-clicks-notBuyData.dat");
	}

	private void generateClicksHasBuys_function(String inFileBuys,
			String inFileClicks, String outFile, String outFile2)
			throws IOException {

		String string_buy = null;
		String string_click = null;
		int numberAll = 0;
		int number = 0;

		FileReader fr_B = new FileReader(inFileBuys);
		BufferedReader br_B = new BufferedReader(fr_B);

		FileReader fr_C = new FileReader(inFileClicks);
		BufferedReader br_C = new BufferedReader(fr_C);

		FileWriter fw_hasbuy = new FileWriter(outFile);
		BufferedWriter bw_hasbuy = new BufferedWriter(fw_hasbuy);

		FileWriter fw_notbuy = new FileWriter(outFile2);
		BufferedWriter bw_notbuy = new BufferedWriter(fw_notbuy);

		HashMap<String, Integer> map = new HashMap<>();
		while ((string_buy = br_B.readLine()) != null) {
			map.put(string_buy.split(",")[0], 1);

		}
		while ((string_click = br_C.readLine()) != null) {
			numberAll++;

			if (numberAll % 100000 == 0)
				System.out.println(numberAll);
			if (map.containsKey(string_click.split(",")[0])) {
				number++;
				bw_hasbuy.write(string_click);
				bw_hasbuy.newLine();
				continue;
			}
			bw_notbuy.write(string_click);
			bw_notbuy.newLine();
		}
		// 最外层的流关闭的时候也会调用内层流关闭的方法
		br_B.close();
		br_C.close();
		bw_hasbuy.close();
		bw_notbuy.close();

	}

}
