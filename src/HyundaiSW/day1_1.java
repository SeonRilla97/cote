package HyundaiSW;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class day1_1 {

    public static void main(String[] args) throws IOException {


        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(bf.readLine());  // Hi Anna         // 입력 데이터 출력

        for(int i = 0 ; i < num ; i++){
        String[] s = bf.readLine().split(" ");
            System.out.println("CASE #" +(i+1) +": " +Integer.parseInt(s[0])+Integer.parseInt(s[1]));
        }

    }
}
