package book;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

public class _1_숫자의_합_구하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(bf.readLine());

        char[] arrj = bf.readLine().toCharArray();

        int sum =0;
        for (int j = 0; j < i; j++) {
            sum += arrj[j] - '0';
        }
        System.out.println(sum);
    }
}
