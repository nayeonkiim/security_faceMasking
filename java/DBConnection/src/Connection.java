import java.util.List;

import dao.FaceDAO;
import vo.FaceVO;

public class Connection {
	public static void main(String[] args) {
		
		
		
		List<FaceVO>list = FaceDAO.getInstance().selectList();
		
		for(int i=0;i<list.size();i++) {
			System.out.println(list.get(i).getId() + " / " + list.get(i).getName());
		}
		
		
		FaceVO vo = new FaceVO();
		vo.setId(9);
		vo.setName("wwww");
		
		int res = FaceDAO.getInstance().insert(vo);
		
		if(res > 0) {
			System.out.println("insert ¼º°ø!");
		}
		
		
		
		
	}

}
