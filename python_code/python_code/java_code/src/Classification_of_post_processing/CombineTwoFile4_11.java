
package Classification_of_post_processing;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CombineTwoFile4_11 {
	public static void main(String args[]) throws IOException {
		combineFile obj = new combineFile(" ", " ", "");
		obj.combine_IO_File("F:\\4_29_drive_night_data\\4yue25ri_8featurebuterr7\\NaiveBayes\\NaiveBays.arff",
				"D:\\Data\\feature\\yoochoose-test-sessionId.dat",
				"D:\\4_29_drive_night\\prediction\\4_25_NaiveBays__7_feature_predictionSession.txt");

	}
}


class combineFile {
	String File1;
	String File2;
	String File3;

	public combineFile(String File1, String File2, String File3) {
		File1 = this.File1;
		File2 = this.File2;
		File3 = this.File3;
	}

	public void combine_IO_File(String Filea, String Fileb, String Filem)
			throws IOException {
		String string = null;
		String s = null;
		int number = 1;
		int n = 13;
		int k = 0;
		FileReader fr = new FileReader(Filea);
		BufferedReader br = new BufferedReader(fr);

		FileWriter fw = new FileWriter(Filem);
		BufferedWriter out = new BufferedWriter(fw);
		FileReader freader = new FileReader(Fileb);
		BufferedReader breader = new BufferedReader(freader);
	label:	while ((string = br.readLine()) != null) {
			if (number < n) {
				number++;
				continue;
			}

			while ((s = breader.readLine()) != null) {
				if (k < 1) {
					k++;
					continue;
				}

				
					out.write(string + "," + s);
					out.newLine();
				
				continue label;
			}
		}
		br.close();
		out.close();
		breader.close();

	}
}
