import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

public class Day5 {
    private static final char RIGHT = 'R';
    private static final char LEFT = 'L';
    private static final char BACK = 'B';
    private static final char FRONT = 'F';

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("./input-day5"));

        Optional<Integer> max = lines.stream().map(encoded -> toSeatNumber(encoded)).max(Comparator.naturalOrder());

        System.out.println(max.orElseThrow());
    }

    private static int toSeatNumber(String encoded) {
        return calculateRowNumber(encoded) * 8 + calculateColumnNumber(encoded);
    }

    private static int calculateRowNumber(String encoded) {
        return binarySearch(encoded.substring(0, 7), 0, 127, FRONT, BACK);
    }

    private static int calculateColumnNumber(String encoded) {
        return binarySearch(encoded.substring(7), 0, 7, LEFT, RIGHT);
    }

    private static int binarySearch(String encoded, int min, int max, char lowerPartIndicator,
            char upperPartIndicator) {

        if (encoded.isBlank()) {
            return min;
        }

        char symbol = encoded.charAt(0);
        String nextSymbols = encoded.substring(1);

        int middle = (min + max) / 2;

        if (symbol == lowerPartIndicator) {
            return binarySearch(nextSymbols, min, middle, lowerPartIndicator, upperPartIndicator);
        } else if (symbol == upperPartIndicator) {
            return binarySearch(nextSymbols, middle + 1, max, lowerPartIndicator, upperPartIndicator);
        } else {
            throw new IllegalArgumentException("Unrecognized symbol:  " + symbol);
        }
    }

}
