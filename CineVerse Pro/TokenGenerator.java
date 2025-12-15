import java.security.SecureRandom;
import java.util.Base64;

public class TokenGenerator {
    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();
        byte[] values = new byte[20];
        random.nextBytes(values);
        String token = Base64.getUrlEncoder().withoutPadding().encodeToString(values);
        System.out.println("JAVA_SEC_" + token);
    }
}