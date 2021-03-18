package service;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnector {
	
	// single-ton pattern: 
	static DBConnector single = null;

	public static DBConnector getInstance() {
		//생성되지 않았으면 생성
		if (single == null)
			single = new DBConnector();
		//생성된 객체정보를 반환
		return single;
	}
	
	private Connection conn; 
	
	public DBConnector() {
		//jdbc 드라이버 주소 
		String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
		// DB 접속 주소
		String DB_URL = "jdbc:mysql://localhost:3306/facemasking?characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false";
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
