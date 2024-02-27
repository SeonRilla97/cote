package HyundaiSW;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.logging.SimpleFormatter;

public class day1_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0 ;
        for(int i = 0 ; i < 5 ; i++){

            String[] s = bf.readLine().split(" ");
            String[] first = s[0].split(":");
            String[] second = s[1].split(":");

            int fin1 = (Integer.parseInt(second[0]) - Integer.parseInt(first[0])) * 60;
            int fin2 = (Integer.parseInt(second[1]) - Integer.parseInt(first[1]));

            sum += (fin1 + fin2);
        }
        System.out.println(sum);
    }
}
