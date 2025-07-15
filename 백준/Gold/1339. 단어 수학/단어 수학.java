//  단어 수학

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {

    static int N; // 단어 개수
    static int[] arr = new int[26]; // 알파벳의 가중치를 저장하는 배열

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        for(int i =0;i<N;i++){
            String str = br.readLine();
            for(int j =0;j<str.length();j++){
                char c = str.charAt(j);
                arr[c-'A'] += (int)Math.pow(10,str.length()-1-j);
            }
        }
        // arr를 오름차순 정렬
        Arrays.sort(arr);

        int num = 9;
        int turn = 25;
        int ans = 0;
        while(arr[turn] != 0){ // 실제로 등장한 알파벳만 처리
            ans+=arr[turn]*num;
            turn--;
            num--;
        }
        System.out.print(ans);
    }
}