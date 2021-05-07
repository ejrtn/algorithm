package algorithm;

import java.util.ArrayList;
import java.util.List;

public class Easy118 {
	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.generate(1));
	}
}
class Solution {
    public List<List<Integer>> generate(int numRows) {
    	ArrayList<Integer> arr;
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
    	for(int i=0;i<numRows;i++) {
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
		return result;
    }
}