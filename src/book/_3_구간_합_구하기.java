package book;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1 <= N <= 100,000 : 숫자 수
 * 1 <= M <= 100,000 : 합연산 시행 수
 *
 * */
public class _3_구간_합_구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = bf.readLine().split(" ");
        String[] origin = bf.readLine().split(" ");

        //구간 합 구하기
        int[] subSum = new int[Integer.parseInt(NM[0])+1];
        subSum[0]=0;
        for (int i = 1; i <= origin.length; i++) {
            int i1 = Integer.parseInt(origin[i-1]);
            subSum[i] = subSum[i-1] + i1;
        }
        for (int i = 0; i < Integer.parseInt(NM[1]); i++) {
            String[] split = bf.readLine().split(" ");
            int i1 = Integer.parseInt(split[0]);
            int i2 = Integer.parseInt(split[1]);

            int result = subSum[i2] - subSum[i1-1];
            System.out.println(result);
        }
    }
}
