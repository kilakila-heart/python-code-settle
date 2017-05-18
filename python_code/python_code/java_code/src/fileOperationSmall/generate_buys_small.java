package fileOperationSmall;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import fileOperation.generate_TestOrClick_sample;

public class generate_buys_small {

	public static void main(String args[]) throws IOException{
		generate_buys_small buy_small=new generate_buys_small();
		buy_small.buy_small_function("E:\\Data\\yoochoose-buys.dat", "E:\\Data\\yoochoose-buys-small.dat");
		
	}



	private void buy_small_function(String buyFile,String buysmallFile) throws IOException{
		FileReader fr=new FileReader(buyFile);
		BufferedReader br=new BufferedReader(fr);
		
		FileWriter fw=new FileWriter(buysmallFile);
		BufferedWriter bw=new BufferedWriter(fw);
		
		int maxsampleSession=100;
		int i=0;
		String string=null;
		while((string=br.readLine())!=null){
			if(Integer.valueOf(string.split(",")[0])<maxsampleSession){					
				bw.write(string);
				bw.newLine();
				i++;
				if(i%10==0)System.out.println(i);
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}

	}

