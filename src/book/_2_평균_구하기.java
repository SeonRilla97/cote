package book;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2_평균_구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(bf.readLine());
        String[] split = bf.readLine().split(" ");

        int max = 0 ;
        int sum = 0;

        for (int j = 0; j < i; j++) {
            int i1 = Integer.parseInt(split[j]);
            //최대값 구하기
            if (max < i1) {
                max = i1;
            }
            // Sum 값 구하기
            sum += i1;
        }
        
        //평균 구하기

        double result= (sum *100.0) /  (max * i);

        System.out.println(result);
    }
}
