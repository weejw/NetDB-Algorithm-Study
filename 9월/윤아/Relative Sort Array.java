class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        ArrayList<Integer> n1=new ArrayList<Integer>();
        ArrayList<Integer> n2=new ArrayList<Integer>();
        ArrayList<Integer> n3=new ArrayList<Integer>();
        
        for(int num1 : arr1) n1.add(num1);
        for(int num2 : arr2) n2.add(num2);
        for(int num3 : n2){
        	boolean flag = true;
        	while(flag) {
	            if(n1.indexOf(num3)!=-1){
	                n3.add(num3);
	                n1.remove(n1.indexOf(num3));
	            }else {
	            	flag = false;
	            }
        	}
        }
        Collections.sort(n1);
        n3.addAll(n1);
        int[] result = new int[n3.size()];
        int x =0;
        for(Integer num : n3){
            result[x]=num;
            x++;
        }
        System.out.println(n3);
        return result;
    }
}
