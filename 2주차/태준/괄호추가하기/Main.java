import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static long N = 0;
    public static ArrayList<Character> operator = new ArrayList<>();
    public static ArrayList<Integer> operand = new ArrayList<>();
    public static boolean[] check;
    public static long max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String input = br.readLine();

        for (int i = 0; i < N; i++) {
            char tmp = input.charAt(i);
            if (i % 2 == 0)
                operand.add((tmp - '0'));
            else
                operator.add(tmp);
        }
        check = new boolean[operand.size()];
        makeRule(0, operand.size() - 1);
        System.out.println(max);
    }

    public static long calculateALl(ArrayList<Long> operandCopy, ArrayList<Character> operatorCopy) {
        long n1 = 0, n2 = 0;
        char op;
        while (operandCopy.size() > 1 && operatorCopy.size() > 0) {
            n1 = operandCopy.remove(0);
            n2 = operandCopy.remove(0);
            op = operatorCopy.remove(0);
            operandCopy.add(0, calculate(n1, n2, op));
        }
        return operandCopy.get(0);
    }

    public static long calculate(long n1, long n2, char op) {
        long ans = 0;
        if (op == '*')
            ans = n1 * n2;
        else if (op == '+')
            ans = n1 + n2;
        else
            ans = n1 - n2;
        return ans;
    }

    public static void makeRule(int now, int end) {
        if (now >= end) {
            long ans = 0;
            int i = 0, j = 0;
            ArrayList<Character> operatorCopy = new ArrayList<>();
            ArrayList<Long> operandCopy = new ArrayList<>();
            while (i < operand.size()) {
                if (check[i]) {
                    int n1 = operand.get(i);
                    int n2 = operand.get(++i);
                    char op = operator.get(j);
                    operandCopy.add(calculate(n1, n2, op));
                    if (j + 1 < operator.size())
                        operatorCopy.add(operator.get(++j));
                } else {
                    operandCopy.add((long) operand.get(i));
                    if (j < operator.size())
                        operatorCopy.add(operator.get(j));
                }
                i++;
                j++;
            }
            ans = calculateALl(operandCopy,operatorCopy);

            if(ans > max)
                max = ans;
        } else {
            check[now] = true;
            makeRule(now + 2, end);
            check[now] = false;
            makeRule(now + 1, end);
        }
    }
}