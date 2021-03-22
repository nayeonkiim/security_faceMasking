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

/* ����� �����ͺ��̽� ������ �������� query�� class */

public class FaceDAO {
	
	// single-ton pattern: 
	static FaceDAO single = null;

	public static FaceDAO getInstance() {
		//�������� �ʾ����� ����
		if (single == null)
			single = new FaceDAO();
		//������ ��ü������ ��ȯ
		return single;
	}
	
	
	
	// ��ü db �ҷ�����
	public List<FaceVO> selectList() {

		List<FaceVO> list = new ArrayList<FaceVO>();
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "";

		try {
			
			//Connectionȹ��
			conn = new DBConnector().getConn();
					
			//���ó����ü������ ������
			stmt = conn.createStatement();
			
			//query��
			sql = "select * from face";

			//����� ó����ü ������
			rs = stmt.executeQuery(sql);

			while (rs.next()) {
				FaceVO vo = new FaceVO();
				//���緹�ڵ尪=>Vo����
				vo.setId(rs.getInt("id"));
				vo.setName(rs.getString("name"));

				//ArrayList�߰�
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
			//1.Connectionȹ��
			conn = new DBConnector().getConn();
			
			//2.���ó����ü ȹ��
			pstmt = conn.prepareStatement(sql);

			//3.pstmt parameter ä���
			pstmt.setInt(1, vo.getId());
			pstmt.setString(2, vo.getName());
			

			//4.DB�� ����(res:ó�������)
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
