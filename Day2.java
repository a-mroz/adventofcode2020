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

        long correctPasswords = entries.stream().filter(entry -> passwordCorrect(entry)).count();

        System.out.println(correctPasswords);
    }

    private static class Entry {
        private final int minOccurences;
        private final int maxOccurences;
        private final char checkedCharacter;
        private final String password;

        private Entry(int minOccurences, int maxOccurences, char checkedCharacter, String password) {
            this.minOccurences = minOccurences;
            this.maxOccurences = maxOccurences;
            this.checkedCharacter = checkedCharacter;
            this.password = password;
        }

        static Optional<Entry> of(String input) {
            Matcher matcher = ENTRY_PATTERN.matcher(input);

            if (matcher.find()) {
                return Optional.of(new Entry(Integer.parseInt(matcher.group(1)), Integer.parseInt(matcher.group(2)),
                        matcher.group(3).charAt(0), matcher.group(4)));
            }
            System.out.println("did not match");
            return Optional.empty();
        }
    }

    private static boolean passwordCorrect(Entry entry) {
        long occurences = entry.password.chars().filter(c -> c == entry.checkedCharacter).count();

        return occurences >= entry.minOccurences && occurences <= entry.maxOccurences;
    }

}
