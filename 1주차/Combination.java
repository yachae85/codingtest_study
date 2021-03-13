package 스터디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Combination {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        List<List<Integer>> ans = combine(n, k);
        for (List<Integer> subset : ans)
            System.out.println(subset);
    }
    public static List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();
        boolean[] visit = new boolean[n];

        func(0, n, 0, k, ans, visit);
        return ans;
    }
    public static void func(int now, int size, int count, int depth, List<List<Integer>> ans, boolean[] visit) {
        if (count == depth) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                if (visit[i])
                    subset.add(i+1);
            }
            ans.add(subset);
        } else if (now < size) {
            visit[now] = true;
            func(now + 1, size, count + 1, depth, ans, visit);
            visit[now] = false;
            func(now + 1, size, count, depth, ans, visit);

        }
    }
}