package Classification_of_post_processing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;

public class solution_io {
	LinkedList<String> list = new LinkedList<String>();

	public void read(String fileinputname) {
		File file = new File(fileinputname);

		if (file.exists() && file.isFile()) {
			try {
				BufferedReader input = new BufferedReader(new FileReader(file));
				String text;

				while ((text = input.readLine()) != null)
					list.add(text);
			} catch (IOException ioException) {
				System.err.println("File Error!");
			}
		}

		for (int i = list.size() - 1; i >= 0; i--) {
			System.out.println(list.get(i).toUpperCase());
		}
	}

	public void write(String fileoutputname) {
		File out = new File(fileoutputname);
		if (out.exists()) {
			out.delete();
		}

		/*
		 * try { if (out.createNewFile()) { BufferedWriter output = new
		 * BufferedWriter(new FileWriter(out)); for (int i = 0; i < list.size();
		 * i++) { output.write( "  " + list.get(i) + "\r\n"); } output.close();
		 * } } catch (IOException e) { // TODO Auto-generated catch block
		 * e.printStackTrace(); }
		 */
		try {
			if (out.createNewFile()) {
				BufferedWriter output = new BufferedWriter(new FileWriter(out));
				for (int i = list.size() - 1; i >= 0; i--) {
					output.write("  " + list.get(i).toUpperCase() + "\r\n");
				}
				output.close();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
   public void FindSword(String word){
	   for (int i = list.size() - 1; i >= 0; i--){
	//	   String candidate =  list.previous();
//	  if(candidate.indexOf(word) != -1) System.out.println(list.get(i).toUpperCase());
   }
	
   }
	
	public static void main(String[] args) {
		if (args.length != 2)
			System.out.println("≤Œ ˝ ‰»Î¥ÌŒÛ");
		else {
			solution_io obj = new solution_io();
			obj.read(args[0]);
			obj.write(args[1]);
			

		}
	}
}