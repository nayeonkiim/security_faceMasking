package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import service.DBConnector;
import vo.FaceVO;

/* 연결된 데이터베이스 데이터 가져오는 query문 class */

public class FaceDAO {
	
	// single-ton pattern: 
	static FaceDAO single = null;

	public static FaceDAO getInstance() {
		//생성되지 않았으면 생성
		if (single == null)
			single = new FaceDAO();
		//생성된 객체정보를 반환
		return single;
	}
	
	
	
	// 전체 db 불러오기
	public List<FaceVO> selectList() {

		List<FaceVO> list = new ArrayList<FaceVO>();
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "";

		try {
			
			//Connection획득
			conn = new DBConnector().getConn();
					
			//명령처리객체정보를 얻어오기
			stmt = conn.createStatement();
			
			//query문
			sql = "select * from face";

			//결과행 처리객체 얻어오기
			rs = stmt.executeQuery(sql);

			while (rs.next()) {
				FaceVO vo = new FaceVO();
				//현재레코드값=>Vo저장
				vo.setId(rs.getInt("id"));
				vo.setName(rs.getString("name"));

				//ArrayList추가
				list.add(vo);
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {

			try {
				if (rs != null)
					rs.close();
				if (stmt != null)
					stmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		return list;
	}
	
	
	
	
	// insert
	public int insert(FaceVO vo) {
		int res = 0;

		Connection conn = null;
		PreparedStatement pstmt = null;

		String sql = "insert into face values(?,?)";

		try {
			//1.Connection획득
			conn = new DBConnector().getConn();
			
			//2.명령처리객체 획득
			pstmt = conn.prepareStatement(sql);

			//3.pstmt parameter 채우기
			pstmt.setInt(1, vo.getId());
			pstmt.setString(2, vo.getName());
			

			//4.DB로 전송(res:처리된행수)
			res = pstmt.executeUpdate();

		} catch (Exception e) {
			e.printStackTrace();
		} finally {

			try {
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		return res;
	}
	
	

}
