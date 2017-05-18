package fileOperation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class generate_TestOrClick_sample {
public static void main(String args[]) throws IOException{
	generate_TestOrClick_sample Tcsample=new generate_TestOrClick_sample();
	Tcsample.TestOrClick_sample_function("E:\\Data\\yoochoose-test.dat", "E:\\Data\\yoochoose-test-sample.dat");
	
}



private void TestOrClick_sample_function(String T_or_C_File,String outFile) throws IOException{
	FileReader fr=new FileReader(T_or_C_File);
	BufferedReader br=new BufferedReader(fr);
	
	FileWriter fw=new FileWriter(outFile);
	BufferedWriter bw=new BufferedWriter(fw);
	
	int maxsampleLine=10000;
	int i=0;
	String string=null;
	while((string=br.readLine())!=null){
		if(i<maxsampleLine){	
			i++;
			bw.write(string);
			bw.newLine();
			if(i%100==0)System.out.println(i);
		}
	}
	br.close();
	bw.flush();
	bw.close();
}

}
