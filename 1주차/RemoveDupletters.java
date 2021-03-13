import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;

public class RemoveDuplLetters {
    public static int[] count = new int[26];
    public static boolean[] check = new boolean[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(removeDuplicateLetters(br.readLine()));
    }

    public static String removeDuplicateLetters(String s) {
        StringBuilder sb = new StringBuilder();
        Stack<Character> st = new Stack();
        counting(s);

        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            if (!check[chr - 'a']) {
                if (!st.isEmpty())
                    remove(st, chr);
                check[chr - 'a'] = true;
                st.push(chr);
            }
            count[chr - 'a']--;
        }

        for (Character tok : st)
            sb.append(tok);

        return sb.toString();
    }

    public static void remove(Stack<Character> st, char chr) {
        ArrayList<Character> delList = new ArrayList();
        for (int i = st.size() - 1; i >= 0; i--) {
            char character = st.get(i);
            if (chr < character && count[character - 'a'] > 0) {
                check[character - 'a'] = false;
                delList.add(character);
            } else
                break;
        }
        delList.forEach(st::remove);
    }

    public static void counting(String s) {
        for (int i = 0; i < s.length(); i++)
            count[s.charAt(i) - 'a']++;
    }
}