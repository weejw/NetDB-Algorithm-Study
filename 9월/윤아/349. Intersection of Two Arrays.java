class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> n1=new ArrayList<Integer>();
        ArrayList<Integer> n2=new ArrayList<Integer>();
        ArrayList<Integer> n3=new ArrayList<Integer>();
        
        for(int num1 : nums1) n1.add(num1);
        for(int num2 : nums2) n2.add(num2);
        
        n2.retainAll(n1);
        for(int num3 : n2){
            if(!n3.contains(num3))
                n3.add(num3);
        }
        
        int[] result = new int[n3.size()];
        
        int x =0;
        for(Integer num : n3){
            result[x]=num;
            x++;
        }
        return result;
    }
}