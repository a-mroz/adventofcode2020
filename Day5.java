import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Comparator;
import java.util.List;
import java.util.Set;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day5 {
    private static final int MAX_COLUMN = 7;
    private static final int MAX_ROW = 127;

    private static final char RIGHT = 'R';
    private static final char LEFT = 'L';
    private static final char BACK = 'B';
    private static final char FRONT = 'F';

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("./input-day5"));

        Supplier<Stream<Integer>> seatsStreamSupplier = () -> lines.stream().map(encoded -> toSeatNumber(encoded));
        Integer max = seatsStreamSupplier.get().max(Comparator.naturalOrder()).orElseThrow();

        // Part 1
        System.out.println(max);

        // Part 2
        Integer min = seatsStreamSupplier.get().min(Comparator.naturalOrder()).orElseThrow();
        Set<Integer> seats = seatsStreamSupplier.get().collect(Collectors.toSet());

        IntStream.range(min + 1, max).forEach(candidate -> {
            if (!seats.contains(candidate)) {
                System.out.println(candidate);
            }
        });
    }

    private static int toSeatNumber(String encoded) {
        return calculateRowNumber(encoded) * 8 + calculateColumnNumber(encoded);
    }

    private static int calculateRowNumber(String encoded) {
        String rowPart = encoded.substring(0, 7); // first 7 symbols
        return binarySearch(rowPart, 0, MAX_ROW, FRONT, BACK);
    }

    private static int calculateColumnNumber(String encoded) {
        String columnPart = encoded.substring(7);
        return binarySearch(columnPart, 0, MAX_COLUMN, LEFT, RIGHT);
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
