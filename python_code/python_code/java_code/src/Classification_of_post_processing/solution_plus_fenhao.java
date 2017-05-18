package Classification_of_post_processing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class solution_plus_fenhao {
public static void main(String args[]) throws IOException{
	solution_plus obj=new solution_plus();
	obj.getSession_plus("D:\\4_29_drive_night\\solution4_25_NaiveBays_7_feature.dat", "D:\\4_29_drive_night\\solution429_Final_NaiveBays_7_feature.dat");
	
}
}
class solution_plus{
	public void  getSession_plus(String File1,String File2) throws IOException{
		FileReader fr=new FileReader(File1);
		BufferedReader br=new BufferedReader(fr);
		FileWriter fw=new FileWriter(File2);
		BufferedWriter bw=new BufferedWriter(fw);
		
		String string;
		while((string=br.readLine())!=null){
			
				bw.write(string+";");
				bw.newLine();
			
		}
		br.close();
		bw.close();
		
	}
}
