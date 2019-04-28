package com.cyberpointllc.stac.auth;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.math.BigInteger;

/**
 * This class is used to verify that the user is connected to the real SnapBuddy host.
 * The user specifies her private key and the server's public key. The program prints the master secret
 * and the user's public key.
 * The user then copies their public key into the SnapBuddy authentication page and presses
 * "Compute Master Secret". The following page will list the server's computed master secret. If
 * the server's master secret matches the user's, the user will be satisfied and continue logging in.
 */
public class KeyExchangeVerifier {

    public static void main(String[] args) throws Exception {
        KeyExchangeVerifierHelper0 conditionObj0 = new  KeyExchangeVerifierHelper0(2);
        if (args.length != conditionObj0.getValue()) {
            throw new  IllegalArgumentException("Must specify <user's private key> <server's public key file>");
        }
        try {
            KeyExchangeServer keyExchangeServer = new  KeyExchangeServer(args[0]);
            String serversPublicKeyString = getServerKey(args[1]);
            BigInteger serversPublicKey;
            if (serversPublicKeyString.startsWith("0x")) {
                serversPublicKey = new  BigInteger(serversPublicKeyString.substring(2), 16);
            } else {
                serversPublicKey = new  BigInteger(serversPublicKeyString);
            }
            BigInteger masterSecret = keyExchangeServer.generateMasterSecret(serversPublicKey);
            System.out.println("Computed user's public key: ");
            System.out.println("\tpaste this in to the server when prompted.");
            System.out.println(keyExchangeServer.getPublicKey());
            System.out.println("\nExpected response: ");
            System.out.println("\tmake sure this is the server's response.");
            System.out.println(masterSecret.toString(10));
        } catch (NumberFormatException e) {
            throw new  IllegalArgumentException("Error: keys must be hexadecimal or decimal numbers");
        }
    }

    private static String getServerKey(String serverKeyPath) throws IOException {
        File serverKeyFile = new  File(serverKeyPath);
        InputStream inputStream = FileUtils.openInputStream(serverKeyFile);
        if (inputStream != null) {
            StringWriter stringWriter = new  StringWriter();
            IOUtils.copy(inputStream, stringWriter, null);
            return stringWriter.toString();
        }
        return null;
    }

    public static class KeyExchangeVerifierHelper0 {

        public KeyExchangeVerifierHelper0(int conditionRHS) {
            this.conditionRHS = conditionRHS;
        }

        private int conditionRHS;

        public int getValue() {
            return conditionRHS;
        }
    }
}
