package firstGui;

import javax.swing.JOptionPane;
import java.util.Scanner;

public class virus {

    public static void main(String[] args) {

        String name;
        name = JOptionPane.showInputDialog("Enter name:");

        JOptionPane.showMessageDialog(null, "Hello " + name);

        int cont = JOptionPane.showConfirmDialog(null, "Do you know what is a vuris?");

        if (cont == JOptionPane.YES_OPTION) {
            int unf = JOptionPane.showConfirmDialog(null, "Unfortunately this is a virus! i have access to your Pc, do you understand?");
            if (unf ==JOptionPane.NO_OPTION){
                JOptionPane.showMessageDialog(null, "Downloading data");
                JOptionPane.showMessageDialog(null, "Accessing files!");
                JOptionPane.showMessageDialog(null, "Encrypting files");
                JOptionPane.showMessageDialog(null, "Wait, almost done");
                String seti = JOptionPane.showInputDialog("Are you setisfied with our service?");
                JOptionPane.showMessageDialog(null, "Ok! bye " + name + " you'll be fine. happens to everyone.");

                JOptionPane.showMessageDialog(null, "I downloaded you data long time ago");
                JOptionPane.showMessageDialog(null, "Bye " + name + " You are not alone.");
            } else {
                JOptionPane.showMessageDialog(null, "since you understand i am gonna steal your data neh " + name + "?");
                JOptionPane.showMessageDialog(null, "Downloading data");
                JOptionPane.showMessageDialog(null, "Accessing files!");
                JOptionPane.showMessageDialog(null, "Encrypting files");
                JOptionPane.showMessageDialog(null, "Wait, almost done");
                String seti = JOptionPane.showInputDialog("Are you setisfied with our service?");
                JOptionPane.showMessageDialog(null, "Ok! bye " + name + " you'll be fine. happens to everyone.");

            }

        } else {
            int und = JOptionPane.showConfirmDialog(null, "Since you don't know what is a virus, we will works just fine, right?");
            if (und == JOptionPane.YES_OPTION) {
                int down = JOptionPane.showConfirmDialog(null, "I want to download your data, do you give m access?");
                if (down == JOptionPane.YES_OPTION){
                    JOptionPane.showMessageDialog(null, "Downloading data");
                    JOptionPane.showMessageDialog(null, "Accessing files!");
                    JOptionPane.showMessageDialog(null, "Encrypting files");
                    JOptionPane.showMessageDialog(null, "Wait, almost done");
                    String seti = JOptionPane.showInputDialog("Are you setisfied with our service?");
                    JOptionPane.showMessageDialog(null, "Ok! bye " + name + " you'll be fine. happens to everyone.");

                } else {
                    JOptionPane.showMessageDialog(null, "Downloading data");
                    JOptionPane.showMessageDialog(null, "Accessing files!");
                    JOptionPane.showMessageDialog(null, "Encrypting files");
                    JOptionPane.showMessageDialog(null, "Wait, almost done");
                    JOptionPane.showMessageDialog(null, "I downloaded logn time ago!");
                    String seti = JOptionPane.showInputDialog("Are you setisfied with our service?");
                    JOptionPane.showMessageDialog(null, "Ok! bye " + name + " you'll be fine. happens to everyone.");

                }
            } else {
                JOptionPane.showMessageDialog(null, "Downloading data");
                JOptionPane.showMessageDialog(null, "Accessing files!");
                JOptionPane.showMessageDialog(null, "Encrypting files");
                JOptionPane.showMessageDialog(null, "Wait, almost done");
                String set = JOptionPane.showInputDialog("Are you setisfied with our service?");
                JOptionPane.showMessageDialog(null, "Ok! bye " + name + " you'll be fine. happens to everyone.");

            }
        }

    }
    
}
