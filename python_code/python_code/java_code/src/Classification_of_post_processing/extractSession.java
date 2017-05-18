package Classification_of_post_processing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class extractSession {
public static void main(String args[]) throws IOException{
	getSession obj=new getSession();
	obj.getSessionfrompre("D:\\4_29_drive_night\\prediction\\4_25_NaiveBays__7_feature_predictionSession.txt", "D:\\4_29_drive_night\\prediction\\4_25_NaiveBays__7_feature__GetSession.txt");
	
}
}
class getSession{
	public void  getSessionfrompre(String File1,String File2) throws IOException{
		FileReader fr=new FileReader(File1);
		BufferedReader br=new BufferedReader(fr);
		FileWriter fw=new FileWriter(File2);
		BufferedWriter bw=new BufferedWriter(fw);
		
		String string;
		while((string=br.readLine())!=null){
			String a=string.split(",")[9];
			//different number of features
			if(string.split(",")[8].equalsIgnoreCase("yes")){
				bw.write(string.split(",")[10]);
			/*if(string.split(",")[6].equalsIgnoreCase("yes")){
					bw.write(string.split(",")[8]);
			*/	
				bw.newLine();
			}
		}
		br.close();
		bw.close();
		
	}
}
