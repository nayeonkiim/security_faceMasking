package service;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnector {
	
	// single-ton pattern: 
	static DBConnector single = null;

	public static DBConnector getInstance() {
		//�������� �ʾ����� ����
		if (single == null)
			single = new DBConnector();
		//������ ��ü������ ��ȯ
		return single;
	}
	
	private Connection conn; 
	
	public DBConnector() {
		//jdbc ����̹� �ּ� 
		String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
		// DB ���� �ּ�
		String DB_URL = "jdbc:mysql://localhost:3306/facemasking?characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false";
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
