package Classification_of_post_processing;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class getSampletrainData {
public static void main(String args[]) throws IOException{
	getsampleTrainFile obj=new getsampleTrainFile();
	obj.getsample("D:\\Data\\five_feature\\balance-month\\yoochoose-feature-all-0.arff","D:\\Data\\five_feature\\balance-month\\yoochoose-feature-all-sample.arff");
}
}
class getsampleTrainFile{
	public void getsample(String file1,String file2) throws IOException{
		final int dataLine=8;
		int number=0;
		double i;
		Random random=new Random();
		
		FileReader fr=new FileReader(file1);
		BufferedReader br=new BufferedReader(fr);
		FileWriter fw=new FileWriter(file2);
		BufferedWriter bw=new BufferedWriter(fw);
		String string=null;
		while((string=br.readLine())!=null){
			i=Math.random();
			if(number<dataLine){
				number++;
				continue;
			}
			if(i<0.5){
				bw.write(string);
				bw.newLine();
			}
				
		}
		
		br.close();
		bw.close();
	}
}
