import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day3 {
    private static final char TREE = '#';

    public static void main(String[] args) throws IOException {
        List<String> map = Files.readAllLines(Path.of("./input-day3"));

        // Task 1
        System.out.println(traverse(map, 1, 3));

        // Task 2
        long task2Result = traverse(map, 1, 1) * traverse(map, 1, 3) * traverse(map, 1, 5) * traverse(map, 1, 7)
                * traverse(map, 2, 1);

        System.out.println(task2Result);
    }

    private static long traverse(List<String> map, int rowStep, int colStep) {
        long result = 0;

        int col = 0;

        for (int row = 0; row < map.size(); row += rowStep) {
            String line = map.get(row);

            if (line.charAt(col) == TREE) {
                result++;
            }

            col = (col + colStep) % line.length();
        }

        return result;
    }
}