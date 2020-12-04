import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day4 {
    private static final Set<String> VALID_EYE_COLORS = Set.of("amb", "blu", "brn", "gry", "grn", "hzl", "oth");
    private static final Pattern HCL_PATTERN = Pattern.compile("^#[0-9a-z]{6}$");
    private static final Pattern PASSPORT_ID_PATTERN = Pattern.compile("^\\d{9}$");
    private static final Pattern HEIGHT_PATTERN = Pattern.compile("(\\d+)(cm|in)");

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("./input-day4"));
        List<Map<String, String>> passports = passports(lines);

        // Task 1
        System.out.println(task1(passports));

        // Task 2
        System.out.println(task2(passports));
    }

    private static long task1(List<Map<String, String>> passports) {
        return passports.stream().filter(passport -> {
            return passport.containsKey("byr") && passport.containsKey("iyr") && passport.containsKey("eyr")
                    && passport.containsKey("hgt") && passport.containsKey("hcl") && passport.containsKey("ecl")
                    && passport.containsKey("pid");
        }).count();
    }

    private static long task2(List<Map<String, String>> passports) {
        return passports.stream().filter(passport -> {
            return isValidByr(passport.get("byr")) && passport.containsKey("iyr") && isValidIyr(passport.get("iyr"))
                    && passport.containsKey("eyr") && isValidEyr(passport.get("eyr")) && passport.containsKey("hgt")
                    && isValidHgt(passport.get("hgt")) && passport.containsKey("hcl") && isValidHcl(passport.get("hcl"))
                    && passport.containsKey("ecl") && isValidEcl(passport.get("ecl")) && passport.containsKey("pid")
                    && isValidPid(passport.get("pid"));
        }).count();
    }

    private static boolean isValidByr(String byr) {
        return isNumericValueInRange(byr, 1920, 2002);
    }

    private static boolean isValidIyr(String iyr) {
        return isNumericValueInRange(iyr, 2010, 2020);
    }

    private static boolean isValidEyr(String eyr) {
        return isNumericValueInRange(eyr, 2020, 2030);
    }

    private static boolean isValidHcl(String hcl) {
        return HCL_PATTERN.matcher(hcl).matches();
    }

    private static boolean isValidEcl(String ecl) {
        return VALID_EYE_COLORS.contains(ecl);
    }

    private static boolean isValidPid(String pid) {
        return PASSPORT_ID_PATTERN.matcher(pid).matches();
    }

    private static boolean isValidHgt(String hgt) {
        Matcher matcher = HEIGHT_PATTERN.matcher(hgt);
        if (matcher.matches()) {

            int value = Integer.parseInt(matcher.group(1));
            String unit = matcher.group(2);

            if (unit.equals("cm")) {
                return isNumericValueInRange(matcher.group(1), 150, 193);
            }

            if (unit.equals("in")) {
                return isNumericValueInRange(matcher.group(1), 59, 76);
            }
        }

        return false;
    }

    private static List<Map<String, String>> passports(List<String> lines) {
        List<Map<String, String>> passports = new ArrayList<>();

        Map<String, String> passport = new HashMap<>();

        for (String line : lines) {
            if (line.isBlank()) {
                passports.add(passport);
                passport = new HashMap<>();
                continue;
            }

            StringTokenizer tokens = new StringTokenizer(line);
            while (tokens.hasMoreTokens()) {
                String token = tokens.nextToken();
                String[] split = token.split(":");
                passport.put(split[0], split[1]);
            }
        }

        passports.add(passport); // last line

        return passports;

    }

    private static boolean isNumericValueInRange(String validating, int min, int max) {
        if (validating == null || validating.isBlank()) {
            return false;
        }

        try {
            int numeric = Integer.parseInt(validating);
            return numeric >= min && numeric <= max;
        } catch (NumberFormatException exception) {
            System.out.println("Not a number: " + validating);
            return false;
        }
    }

}
