import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Day2 {

    private static final Pattern ENTRY_PATTERN = Pattern.compile("^(\\d+)-(\\d+) (.): (.*)$");

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("./input-day2"));

        List<Entry> entries = lines.stream().map(Entry::of).flatMap(Optional::stream).collect(Collectors.toList());

        // Task 1
        long correctPasswordsLegacyPolicy = entries.stream().filter(entry -> isPasswordCorrectLegacyPolicy(entry))
                .count();
        System.out.println(correctPasswordsLegacyPolicy);

        // Task 2
        long correctPasswordsCorporatePolicy = entries.stream().filter(entry -> isPasswordCorrectCorporatePolicy(entry))
                .count();
        System.out.println(correctPasswordsCorporatePolicy);
    }

    private static class Entry {
        // the `first` and `second` variables have different meaning, depending on the
        // task. In the real world, I would think about separate classes
        private final int first;
        private final int second;
        private final char checkedCharacter;
        private final String password;

        private Entry(int first, int second, char checkedCharacter, String password) {
            this.first = first;
            this.second = second;
            this.checkedCharacter = checkedCharacter;
            this.password = password;
        }

        static Optional<Entry> of(String input) {
            Matcher matcher = ENTRY_PATTERN.matcher(input);

            if (matcher.find()) {
                return Optional.of(new Entry(Integer.parseInt(matcher.group(1)), Integer.parseInt(matcher.group(2)),
                        matcher.group(3).charAt(0), matcher.group(4)));
            }
            System.out.println("Did not match: " + input); // or throw instead
            return Optional.empty();
        }
    }

    // In real wold: strategy pattern instead of two methods
    private static boolean isPasswordCorrectLegacyPolicy(Entry entry) {
        long occurences = entry.password.chars().filter(c -> c == entry.checkedCharacter).count();

        return occurences >= entry.first && occurences <= entry.second;
    }

    private static boolean isPasswordCorrectCorporatePolicy(Entry entry) {
        return entry.password.charAt(entry.first - 1) == entry.checkedCharacter
                ^ entry.password.charAt(entry.second - 1) == entry.checkedCharacter;
    }

}
