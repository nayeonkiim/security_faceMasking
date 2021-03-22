package service;

import java.sql.Connection;
import java.sql.DriverManager;


/* DB연결 class */

public class DBConnector {
	
	private Connection conn; 
	
	public DBConnector() {
		//jdbc 드라이버 주소 
		String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
		
		String unicode = "characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false&autoReconnect=true&validationQuery=select 1";
		// DB 접속 주소
		String DB_URL = "jdbc:mysql://localhost:3306/facemasking?" + unicode;
		// DB ID
		String USERNAME = "root"; 
		// DB Password
		String PASSWORD = "1234";
		
		try { 
			Class.forName(JDBC_DRIVER); 
			//Class 클래스의 forName()함수를 이용해서 해당 클래스를 메모리로 로드 하는 것입니다. 
			//URL, ID, password를 입력하여 데이터베이스에 접속합니다. 
			conn = DriverManager.getConnection(DB_URL,USERNAME,PASSWORD); 
			// 접속결과를 출력합니다. 
			if (conn != null){
				System.out.println("성공");
			} 
			
			else{
				System.out.println("실패");
				
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
