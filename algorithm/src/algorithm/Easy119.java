package algorithm;

import java.util.ArrayList;
import java.util.List;

public class Easy119 {
	public static void main(String[] args) {
		Solutions s = new Solutions();
		System.out.println(s.generate(5));
	}
}
class Solutions {
    public List<Integer> generate(int numRows) {
    	ArrayList<Integer> arr;
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
    	for(int i=0;i<numRows+1;i++) {
    		arr = new ArrayList<Integer>();
    		if(i==0) {
    			arr.add(1);
    			result.add(arr);
    		}else if(i==1) {
    			arr.add(1);
    			arr.add(1);
    			result.add(arr);
    		}
    		else {
    			arr.add(1);
    			for(int x=0;x<result.get(i-1).size()-1;x++) {
    				arr.add(result.get(i-1).get(x)+result.get(i-1).get(x+1));
    			}
    			arr.add(1);
    			result.add(arr);
    		}
    	}
		return result.get(result.size()-1);
    }
}