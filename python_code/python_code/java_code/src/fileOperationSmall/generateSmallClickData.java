package fileOperationSmall;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class generateSmallClickData {

	public static void main(String args[]) throws IOException {
		generateSmallClickData click_small = new generateSmallClickData();
		click_small.click_small_function("E:\\Data\\yoochoose-clicks.dat",
				"E:\\Data\\yoochoose-clicks-small.dat");

	}

	private void click_small_function(String clickFile, String clicksmallFile)
			throws IOException {
		FileReader fr = new FileReader(clickFile);
		BufferedReader br = new BufferedReader(fr);

		FileWriter fw = new FileWriter(clicksmallFile);
		BufferedWriter bw = new BufferedWriter(fw);

		int maxsampleSession = 100000;
		int i = 0;
		String string = null;
		while ((string = br.readLine()) != null) {
			if (Integer.valueOf(string.split(",")[0])< maxsampleSession)
			{			
			bw.write(string);
			bw.newLine();
			}
			i++;
			if (i % 100000 == 0) {
				System.out.println(i);
			}
		}

		br.close();
		
		bw.close();
	}
}
