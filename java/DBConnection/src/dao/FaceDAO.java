package dao;

import java.sql.Connection;
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
	
	Connection conn;
	
	public FaceDAO() {
		conn = DBConnector.getInstance().getConn();
	}
	
	public List<FaceVO> selectList() {

		List<FaceVO> list = new ArrayList<FaceVO>();
		Statement stmt = null;
		ResultSet rs = null;
		String sql = "";

		try {
			//1.Connection���´�
			conn = DBConnector.getInstance().getConn();
			//2.���ó����ü������ ������
			stmt = conn.createStatement();
			
			//query��
			sql = "select * from face";

			//3.����� ó����ü ������
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
	
	

}
