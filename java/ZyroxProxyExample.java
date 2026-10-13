// Zyrox Proxy with Java 11+ HttpClient. No dependencies.
//   java ZyroxProxyExample.java
import java.net.Authenticator;
import java.net.InetSocketAddress;
import java.net.PasswordAuthentication;
import java.net.ProxySelector;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class ZyroxProxyExample {

    static HttpClient clientFor(String options) {
        String user = System.getenv("ZYROX_USER") + options;
        char[] pass = System.getenv("ZYROX_PASS").toCharArray();

        return HttpClient.newBuilder()
            .proxy(ProxySelector.of(new InetSocketAddress("host.zyroxproxy.com", 7000)))
            .authenticator(new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(user, pass);
                }
            })
            .connectTimeout(Duration.ofSeconds(30))
            .build();
    }

    static String getIp(HttpClient client) throws Exception {
        HttpRequest req = HttpRequest.newBuilder(URI.create("https://api.ipify.org")).build();
        return client.send(req, HttpResponse.BodyHandlers.ofString()).body();
    }

    public static void main(String[] args) throws Exception {
        // Java disables Basic auth for HTTPS proxy tunnels by default. This must
        // be set before the first request (or pass it with -D on the command line).
        System.setProperty("jdk.http.auth.tunneling.disabledSchemes", "");

        System.out.println("United States: " + getIp(clientFor("-country-us")));

        HttpClient sticky = clientFor("-country-us-session-java1");
        System.out.println("Sticky:        " + getIp(sticky) + " " + getIp(sticky));
    }
}
