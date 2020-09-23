import java.util.Stack;

public class Valid_Parentheses {
	public static void main(String[] args) {
		String s = "{[]}";
		isValid(s);
	}
	public static boolean isValid(String s) {
		String[] array_s;
		
		array_s = s.split("");
		Stack<String> st = new Stack<String>();
		
		for(String c1 : array_s) {
			if(c1.equals("[")||c1.equals("{")||c1.equals("(")) {
				st.push(c1);
			}
			if(st.isEmpty()){
				return false;
			}			
			switch(c1){
			case "]" :
				if(!st.peek().equals("[")) {
					return false;
				}else {
					st.pop();
				}
				break;
			case "}" :
				if(!st.peek().equals("{")) {
					return false;
				}else {
					st.pop();
				}
				break;
			case ")" :
				if(!st.peek().equals("(")) {
					return false;
				}else {
					st.pop();
				}
				break;
			}
		}
		return st.isEmpty();
    }
}

