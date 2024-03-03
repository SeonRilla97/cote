package programmers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class 최솟값＿만들기＿lv2 {

    //Todo 	Input [1, 4, 2], [5, 4, 4]
    public static void main(String[] args) throws IOException {
        int[] A = {1, 4, 2};
        int[] B = {5, 4, 4};
        PriorityQueue<Integer> l1 = new PriorityQueue<>();
        PriorityQueue<Integer> l2 = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < B.length; i++) {
            l1.add(A[i]);
            l2.add(B[i]);
        }
        
        int sum = 0;

        while(!l1.isEmpty()) {
            sum += (l1.remove() * l2.remove());
        }
        System.out.println("sum = " + sum);
    }
}
