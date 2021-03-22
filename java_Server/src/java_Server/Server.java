package java_Server;

import java.io.*;
import java.net.*;

public class Server {
	public static void main(String[] args) {
		  DatagramSocket server = null;
		  DatagramPacket receivePacket, sendPacket;
		  try {
			  
			  File file =null;
			  DataOutputStream dos =null;
			  
			   server = new DatagramSocket(3030);
			   System.out.println("Server Ready...");
			   
			   byte [] buffer = new byte[128];
			   while(true){
			    receivePacket = new DatagramPacket(buffer, buffer.length);
			    server.receive(receivePacket); // 문자열은 receivPacket의 버퍼에 남고
			      //길이는 receivePacket에 남는듯..?
			    String msg = new String(buffer, 0, 
			                   receivePacket.getLength());
			    
			    String filePath = "c:\\prac\\test\\a.txt";
			    try {
			     FileWriter fileWriter = new FileWriter(filePath);
			     fileWriter.write(msg);
			     
			     fileWriter.close();
			    } catch (IOException e) {
			     // TODO Auto-generated catch block
			     e.printStackTrace();
			    }
			  if(msg.equals("bye")) break;
			    
			    System.out.println("Client 로부터 들어온 문자열 : " + msg);
			 
			   }
		  } catch (Exception e) {
		   System.out.println(e.getMessage());
		  }
		 }
		}