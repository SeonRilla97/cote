package programmers;

import java.util.Stack;

public class JadenCase_문자열_만들기_lv2 {
    public static void main(String[] args) {
        String s ="  p eo ple 2unFollowed   me";
//        String s1= "1a2B3C";
//        String s ="for the last   week";
        char[] charArr = s.toLowerCase().toCharArray();

        int i = 0;

        while (i != charArr.length){
            char t = charArr[i];

            //문장의 첫 글자를 대문자로 바꾸는것
            if( i== 0 ){
                if( t > 'a' && t < 'z') {
                    charArr[i] = Character.toUpperCase(t);
                }
                i++;
                continue;
            }

            if( charArr[i-1] == ' ' && t > 'a' && t < 'z' ){
                charArr[i] = Character.toUpperCase(t);
            }
            i++;
        }
        System.out.println(String.valueOf(charArr));
    }
}
