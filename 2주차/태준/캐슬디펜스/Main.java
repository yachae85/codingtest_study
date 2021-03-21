import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N = 0, M = 0, D = 0, max = 0;
    public static int[][] Map;
    public static boolean[] visit;
    public static ArrayList<Point> Enemy = new ArrayList<>();
    public static ArrayList<Point> Archer = new ArrayList<>();

    public static class Point {
        int x = 0;
        int y = 0;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        Map = new int[N][M];
        visit = new boolean[M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                Map[i][j] = Integer.parseInt(st.nextToken());
                if (Map[i][j] == 1)
                    Enemy.add(new Point(i, j));
            }
        }
        decideArcher(0, 0);
        System.out.println(max);
    }

    /**
     * 배치가 완료된 후 게임
     * 공통된 적을 떄릴 수 있으므로, 궁수의 한턴당 Set으로 관리
     * 조건은 dist로 체크하되, 같다면 적의 y좌표확인
     */
    public static void playGame() {
        int min = 0, i = 0, t = 0, j = 0;
        Point target = null;
        Set<Point> killed = new LinkedHashSet<>();
        Set<Point> shouldDelete = new LinkedHashSet<>();
        ArrayList<Point> enemyCopy = new ArrayList<>(Enemy);
        for (t = 0; t < N; t++) {
            for (Point archer : Archer) {
                target = null;
                min = Integer.MAX_VALUE;
                for (Point enemy : enemyCopy) {
                    if (shouldCheck(enemy, t)) {
                        int dist = kill(archer, enemy, t);
                        if (dist != -1 && dist <= min) {
                            if (dist == min) {
                                if (enemy.y < target.y)
                                    target = enemy;
                            } else {
                                min = dist;
                                target = enemy;
                            }
                        }
                    } else
                        shouldDelete.add(enemy);
                }
                if (target != null) {
                    killed.add(target);
                    shouldDelete.add(target);
                }
            }
            shouldDelete.forEach(enemyCopy::remove);
            shouldDelete.clear();
        }
        max = Math.max(max, killed.size());
    }

    /**
     * 맵을 벗어나지 않았으면 일단 check
     */
    public static boolean shouldCheck(Point enemy, int floor) {
        return enemy.x + floor < N;
    }

    /**
     * 궁수와 적사이의 거리
     */
    public static int getDistance(Point enemy, Point archer, int floor) {
        return Math.abs(archer.x - (enemy.x + floor)) + (Math.abs(archer.y - enemy.y));
    }

    /**
     * 죽일 수 있으면 dist 리턴, 아니면 -1
     */
    public static int kill(Point archer, Point enemy, int floor) {
        int dist = getDistance(enemy, archer, floor);
        if (dist <= D)
            return dist;
        else
            return -1;
    }

    /**
     * 조합으로 궁수배치
     */
    public static void decideArcher(int now, int decided) {
        if (decided == 3) {
            Archer.clear();
            for (int i = 0; i < M; i++) {
                if (visit[i])
                    Archer.add(new Point(N, i));
            }
            playGame();
        } else if (now < M) {
            visit[now] = true;
            decideArcher(now + 1, decided + 1);
            visit[now] = false;
            decideArcher(now + 1, decided);
        }
    }
}