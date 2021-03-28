package service;

import java.sql.Connection;
import java.sql.DriverManager;


/* DB���� class */

public class DBConnector {
	
	private Connection conn; 
	
	public DBConnector() {
		//jdbc ����̹� �ּ� 
		String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
		
		String unicode = "characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false&autoReconnect=true&validationQuery=select 1";
		// DB ���� �ּ�
		String DB_URL = "jdbc:mysql://localhost:3306/facemasking?" + unicode;
		// DB ID
		String USERNAME = "root"; 
		// DB Password
		String PASSWORD = "1234";
		
		try { 
			Class.forName(JDBC_DRIVER); 
			//Class Ŭ������ forName()�Լ��� �̿��ؼ� �ش� Ŭ������ �޸𸮷� �ε� �ϴ� ���Դϴ�. 
			//URL, ID, password�� �Է��Ͽ� �����ͺ��̽��� �����մϴ�. 
			conn = DriverManager.getConnection(DB_URL,USERNAME,PASSWORD); 
			// ���Ӱ���� ����մϴ�. 
			if (conn != null){
				System.out.println("����");
			} 
			
			else{
				System.out.println("����");
				
				} 
		} 
		
		catch (Exception e) { 
			e.printStackTrace(); 
		}
		
	}
	
	public Connection getConn() {
		return conn;
	}
	
	

}
