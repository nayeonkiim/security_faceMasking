import java.util.List;

import dao.FaceDAO;
import vo.FaceVO;

public class Connection {
	public static void main(String[] args) {
		
		List<FaceVO>list = FaceDAO.getInstance().selectList();
		
		for(int i=0;i<list.size();i++) {
			System.out.println(list.get(i).getId() + " / " + list.get(i).getName());
		}
		
	}

}
