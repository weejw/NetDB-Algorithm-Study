class Fair_Candy_Swap {
	public static void main(String[] args) {
		int[] A = {1,1};
	    int[] B = {2,2};
	    fairCandySwap(A,B);
	}
	
    public static int[] fairCandySwap(int[] A, int[] B) {
        int sumA = 0;
        int sumB = 0;
        
        for(int num1 : A) sumA+=num1;
        for(int num2 : B) sumB+=num2;

        int[] result = new int[2];
        
        finish:
        for(int num3 : A) {
        	for(int num4 : B) {
        		int aNow = sumA-num3+num4;
        		int bNow = sumB-num4+num3;
        		if(aNow == bNow) {
        			result[0]=num3;
        			result[1]=num4;
        			break finish;
        		}
        	}
        }
        return result;   
    }
}





