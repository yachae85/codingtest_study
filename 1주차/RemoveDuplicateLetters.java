package 스터디;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class RemoveDuplicateLetters{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        RemoveDuplicateLetters rm = new RemoveDuplicateLetters();
        System.out.println(rm.removeDuplicateLetters(str));
    }
    public String removeDuplicateLetters(String s) {
        boolean[] visit = new boolean[26];
        Set<Character> set = new LinkedHashSet<>();
        Set<String> strings = new LinkedHashSet<>();
        for (int i = 0; i < s.length(); i++)
            set.add(s.charAt(i));

        comb(0, 0, set.size(), "", s, visit, strings);
        return strings.stream().sorted().findFirst().get();
    }
    public void comb(int now, int count, int depth, String newStr, String origin, boolean[] visit, Set<String> strings) {
        if (count == depth)
            strings.add(newStr);
        if (now < origin.length()) {
            char ch = origin.charAt(now);
            int index = ch - 'a';
            if (visit[index]) {
                String change = newStr.replace(String.valueOf(ch), "") + ch;
                comb(now + 1, count, depth, newStr, origin, visit, strings);
                comb(now + 1, count, depth, change, origin, visit, strings);
            } else {
                visit[index] = true;
                comb(now + 1, count + 1, depth, newStr + ch, origin,visit,strings);
                visit[index] = false;
            }
        }
    }
}