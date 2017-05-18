package getData;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public  class getBalanceData {
	public static void main(String args[]) throws IOException {
		getBalanceData GBD=new getBalanceData();
		GBD.getBalanceData_function("E:\\Data\\feature\\balance-monthLen\\yoochoose-feature-balence-",
		          "E:\\Data\\feature\\yoochoose-buys-click-feature-maxBuysFrequentness-monthLen.csv",
		          "E:\\Data\\feature\\yoochoose-notBuys-click-feature-maxBuysFrequentness-monthLen.csv");
	}

	private void getBalanceData_function(String fileName, String buyFile,
			String clickFile) throws IOException {
		// Random random = new Random(47);// 随机数种子
		// int number = random.nextInt(17);// 产生[0-17)的随机数
		for (int i = 0; i < 17; i++) {
			String string = null;
			int number = 0;
			fileName = fileName + String.valueOf(i) + ".arff";
			FileWriter fw = new FileWriter(fileName);
			BufferedWriter bw = new BufferedWriter(fw);

			bw.write("@relation yoochoose-balance-feature\n\n");
			bw.write("@attribute clickNumber numeric\n");
			bw.write("@attribute popularOrNot numeric\n");
			bw.write("@attribute repeatClick numeric\n");
			bw.write("@attribute priceGrade numeric\n");
			bw.write("@attribute categoryValue {3C,1C,0C,9C,7C,2C,4C,5C,6C,SC,8C,-1C,10C,12C,11C,13C,14C,15C,16C,17C,18C,19C,20C,21C,22C,23C,24C,25C,26C,27C,28C,29C,30C}\n");
			bw.write("@attribute buysFrequentness numeric\n");
			bw.write("@attribute month {-1M,0M,1M}\n");
			bw.write("@attribute monthLen numeric\n");
			bw.write("@attribute category {yes,no}\n\n@data\n");

			FileReader fr_buys = new FileReader(buyFile);
			BufferedReader br_buys = new BufferedReader(fr_buys);

			FileReader fr_click = new FileReader(clickFile);
			BufferedReader br_click = new BufferedReader(fr_click);

			while ((string = br_buys.readLine()) != null) {
				if (number == 0) {
					number += 1;
					continue;
				}
				bw.write(string);
				bw.newLine();
			}
			number = 0;

			while ((string = br_click.readLine()) != null) {
				if (number == 0) {
					number += 1;
					continue;
				}
				if ((number + i) % 17 == 0)// ->要按抽样方法写入各个文件
					bw.write(string+ "\n");
				number++;

			}
			br_buys.close();
			br_click.close();
			bw.close();
			System.out.println("第"+(i+1)+"个文件已经生成");
			fileName="E:\\Data\\feature\\balance-monthLen\\yoochoose-feature-balence-";

		}

	}

}
