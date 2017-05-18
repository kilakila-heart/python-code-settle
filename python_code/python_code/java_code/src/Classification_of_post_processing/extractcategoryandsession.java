package Classification_of_post_processing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class extractcategoryandsession {
public static void main(String args[]) throws IOException{
	GetSessionandcategory obj=new GetSessionandcategory();
	obj.getSessionfrompre("D:\\厦大任务\\prediction\\predictionSession.txt", "D:\\厦大任务\\prediction\\GetSessionandcategory.txt");
	
}
}
class GetSessionandcategory{
	public void  getSessionfrompre(String File1,String File2) throws IOException{
		FileReader fr=new FileReader(File1);
		BufferedReader br=new BufferedReader(fr);
		FileWriter fw=new FileWriter(File2);
		BufferedWriter bw=new BufferedWriter(fw);
		
		String string;
		while((string=br.readLine())!=null){
			
				bw.write(string.split(",")[9]+","+string.split(",")[11]);
				bw.newLine();
			
		}
		br.close();
		bw.close();
		
	}
}
