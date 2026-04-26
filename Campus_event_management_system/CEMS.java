package Campus_event_management_system;

import java.util.LinkedList; //importing linked list to create linked lists
import java.util.ArrayList;
import java.util.List; //importing List to create lists
import java.util.Scanner; //importing a scanner that will be used to collect input
import java.util.Queue;
import java.io.*;

//a class thhat collects input and store it
class Event {
    int eventID;
    String eventName;
    String eventDate;
    String eventTime;
    String location;
    int maxParc;

    // String studName;
    // int studNum;

    List<String> registered = new ArrayList<>(); //registered student array
    Queue<String> waitlist = new LinkedList<>(); //waitlisted student list
}

//class for stuff
class Staff {

    //@SuppressWarnings("resource")
    Scanner input;

    Staff(Scanner input) {
        this.input = input;
    }

    //Staff evnt = new updateEvent();


    //List<Integer> eventsInt = new LinkedList<>();
    //connector to a class that acts as database
    List<Event> events = new LinkedList<>();

    //create event function that collect data to create event
    void create_event() {
        
        System.out.println("\n------------Create Event-------------\n");
        
        System.out.print("Enter 0 on Id input to exit.\n");
        
        while(true) {
            
            System.out.print("Event Id: "); //searching event by id
            int eventID = input.nextInt();
            input.nextLine();
            
            if (eventID == 0) {
                break;
            }
            
            boolean searchID = false;

            for (Event e : events) {
                if (e.eventID == eventID) {
                    searchID = true;
                    break;
                }
            }

            if (searchID) {
                System.out.println("\nID already exist try different Id.\n");
                continue;
            }
            
            //collecting event information
            System.out.print("Event name: ");
            String eventName = input.nextLine();
            
            System.out.print("Event date: (dd/mm/yyyy) ");
            String eventDate = input.nextLine();
            
            System.out.print("Event time: (hh/mm) ");
            String eventTime = input.nextLine();
            
            System.out.print("Location: ");
            String location = input.nextLine();
            
            System.out.print("maximum participants: ");
            int maxParc = input.nextInt();
            input.nextLine();
            
            Event e = new Event();

            //store data
            e.eventID = eventID;
            e.eventName = eventName;

            e.eventDate = eventDate;
            e.eventTime = eventTime;
            e.location = location;
            e.maxParc = maxParc;

            events.add(e); //adding information to the list

            System.out.println("\nEvent Created\n");
            searchID = true;
            break;
        }
    }

    //a function that defines an update function from an ovveriden class
    void update() {
    }

    //the function that displays events for students
    void view() {

        events.sort((a, b) -> a.eventName.compareToIgnoreCase(b.eventName)); //sorting events by name
           
        if (events.isEmpty()) {
            System.out.println("\nNo available events\n");
        }
        else {
            for (Event e : events) {
                System.out.println("-----------------------------------------");
                
                System.out.println("\n\tId: " + e.eventID + "\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                System.out.println("-----------------------------------------");
            }


        }
    }

    //function that deletes events
    void Remove() {
        //Scanner input = new Scanner(System.in);
        //Staff staff = new updateEvent(this.events);        
        
        if (events.isEmpty()) {
            System.out.println("\nNo events Available\n");
            return;
        }

        view();


        System.out.print("Enter event Id to remove event: (0 to exit) ");
        int ID = input.nextInt();
        input.nextLine();
        
        if (ID == 0) {
            return;
        }

        Event toremove = null;

        for (Event e : events) {
            if (e.eventID == ID) {
                toremove = e;
                break;                
            }
        }

        if (toremove != null) {
            events.remove(toremove);
            System.out.println("Event deleted successfully.");
        }
        else {
            System.out.println("Event not found!");
        }
            
    }

    //viewing registered students
    void viewRegistered() {

        System.out.println("\n-------------Participants--------------\n");

        if (events.isEmpty()) {
            System.out.println("\nNo available events\n Create events.\n");
        }
        else {
            for (Event e : events) {
                System.out.println("=========================================");

                System.out.println("------------Event-------------");

                System.out.println("\n\tId: " + e.eventID + "\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                //registered students
                System.out.println("\n------------Registered Students------------");
                if (e.registered.isEmpty()) {
                    System.out.println("None.");
                }
                else {
                    for (String R : e.registered) {
                        System.out.println("Student Number: " + R);
                    }
                }

                //waitlisted students
                System.out.println("\n-------------Wailtist students-------------");
                if (e.waitlist.isEmpty()) {
                    System.out.println("None");
                }
                else {
                    for (String R : e.waitlist) {
                        System.out.println("Student Number: " + R);
                    }
                }

                System.out.println("=========================================");


            }
        }

    }

    //entry function for staff menu
    void optionStaff() {

        System.out.println("\n-------Welcome Staff Member------\n");
        Staff upEvent = new updateEvent(this.events, this.input);

        //Staff updEvent = new updateEvent(this.events);

        List<String> options = new ArrayList<>();
            options.add("1. Create events");
            options.add("2. Update Event details");
            options.add("3. Cancel Event");
            options.add("4. View registered");
            options.add("5. Exit");

        while(true) {

            System.out.println("--------------Staff Menu--------------");

            for(String opt : options) {
                System.out.println(opt);
            }

            System.out.println();

            System.out.print("Enter option: ");
            int option = input.nextInt();
            input.nextLine();

            if (option == 1) {
                create_event();
                saveToFile();
                continue;
            }
            else if (option == 2) {
                upEvent.view();
                saveToFile();
                continue;
            }
            else if (option == 3) {
                Remove();
                saveToFile();
                continue;
            }
            else if (option == 4) {
                viewRegistered();
                saveToFile();
                continue;
            }
            else if (option == 5) {
                break;
            }
            else {
                System.out.println("Option does not found!");
                continue;
            }
        }

    }

    //saving information to text file
    void saveToFile() {
        try (PrintWriter writer = new PrintWriter("events.txt")) {
            for (Event e : events) {

                String reg = String.join(", ", e.registered);
                String wait = String.join(", ", e.waitlist);
                writer.println(
                    e.eventID + " | " +
                    e.eventName + " | " +
                    e.eventDate + " | " +
                    e.eventTime + " | " +
                    e.location + " | " +
                    e.maxParc + " | " +
                    "reg: " + reg + " | " +
                    "wait: " + wait
                );
            }
        } catch (Exception e) {
            System.out.println("Error saving file!");
        }
    }

    //loading information from the text file
    void loadFromFile() {
        events.clear();
        try(Scanner fileScanner = new Scanner(new File("events.txt"))) {
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                String[] parts = line.split("\\|");

                Event e = new Event();
                e.eventID = Integer.parseInt(parts[0].trim());
                e.eventName = parts[1].trim();
                e.eventDate = parts[2].trim();
                e.eventTime = parts[3].trim();
                e.location = parts[4].trim();
                e.maxParc = Integer.parseInt(parts[5].trim());

                //loading registered students from text file
                if (parts.length > 6) {
                    String regPart = parts[6].trim().replace("reg: ", "");
                    if(!regPart.isEmpty()) {
                        String[] regList = regPart.split(", ");
                        for (String r : regList) {
                            e.registered.add(r.trim());
                        }
                    }
                }

                //loading student who are waitlist from text file
                if (parts.length > 7) {
                    String waitPart = parts[7].trim().replace("wait: ", "");
                    if (!waitPart.isEmpty()) {
                        String[] waitList = waitPart.split(", ");
                        for(String w : waitList) {
                            e.waitlist.add(w.trim());
                        }
                    }
                }

                events.add(e);
            }
        } catch (Exception e) {
            System.out.println("Data not found");
        }
    }

}
//extended class for staff functions 
class updateEvent extends Staff{

    //@SuppressWarnings("resource")

    updateEvent(List<Event> events, Scanner input) {
        super(input);
        this.events = events;
    }
    

    @Override
    //view function which only stuff use
    void view() {
        //events.sort((a, b) -> a.eventName.compareToIgnoreCase(b.eventName)); //sorting events by name

        if (events.isEmpty()) {
            System.out.println("\nNo available events\n Create events.\n");
        }
        else {
            for (Event e : events) {
                System.out.println("--------------Events------------------");

                System.out.println("\n\tId: " + e.eventID + "\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                System.out.println("--------------------------------------");
            }

            update(); //calling update function after displaying all events  for easy update

        }
    }

    //update function to update event information
    void update() {

        System.out.println("\n------------Update Event Details----------\n");

        while (true) {

            System.out.print("Select event by Id: "); //id to select event
            int updEvntId = input.nextInt();
            input.nextLine();

            if (updEvntId == 0) {
                break;
            }

            boolean searchId = false;

            for (Event e : events) {
                if (e.eventID == updEvntId) {
                    System.out.println("\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                    //collection updating information
                    while(true) {
                        System.out.print("What you you want to update? ");
                        String upText = input.nextLine();
                        
                        if (upText.equals("name")) {
                            System.out.print("Enter new name: ");
                            String newName = input.nextLine();
                            e.eventName = newName;
                            System.out.println("\nName updated\n");
                            break;
                        }
                        else if(upText.equals("date")) {
                            System.out.print("Enter new Date: ");
                            String newDate = input.nextLine();
                            e.eventDate = newDate;
                            System.out.print("\nDate updated\n");
                            break;
                        }
                        else if (upText.equals("time")) {
                            System.out.print("Enter new time: ");
                            String newTime = input.nextLine();
                            e.eventTime = newTime;
                            System.out.println("\nTime updated\n");
                            break;
                        }
                        else if(upText.equals("location")) {
                            System.out.print("Enter new location: ");
                            String newLoc = input.nextLine();
                            e.location = newLoc;
                            System.out.println("\nLocation updated\n");
                            break;
                        }
                        else if(upText.equals("Max participants")) {
                            System.out.print("Enter new maximum parcticipants: ");
                            int newMax = input.nextInt();
                            input.nextLine();
                            e.maxParc = newMax;
                            System.out.println("\nParticipants updated.\n");
                            break;
                        }
                        else {
                            System.out.println("\nreplacement not found\n");
                            continue;
                        }

                    }

                    searchId = true;
                    break;
                }
            }

            if (searchId == false) {
                System.out.println("Event not found");
                System.out.println("Enter 0 to exit");
                continue;
            }
        }
    }
}

//student class
class Student {

    //@SuppressWarnings("resource")
    Scanner input;
    Staff staff;
    
    Student(Staff staff, Scanner input) {
        this.staff=staff;
        this.input=input;
    }
        
    //student view function
    void view_events() {
        staff.view();
    }

    //function for students to register for function
    void register() {
        

        System.out.println("------------Register for event-----------");

        //collecting information
        System.out.print("Enter event Id: ");
        int eventID = input.nextInt();
        input.nextLine();

        System.out.print("Enter student number: ");
        String studNum = input.nextLine();
        //input.nextLine();

        // System.out.print("Enter name: ");
        // String studName = input.nextLine();

        if (studNum.length() != 9 ) {
            System.out.println("Student number does not exist!");
            return;
        }

        boolean found = false;

        //checking if registered or waitlisted
        for (Event e : staff.events) {
            if (e.eventID == eventID) {
                if (e.registered.contains(studNum) || e.waitlist.contains(studNum)) {
                    System.out.println("Already registered or on waitlist.");
                    return;
                }

                if (e.registered.size() < e.maxParc) {
                    e.registered.add(studNum);
                    //e.registered.add(studName);
                    System.out.println("\nRegistred successfully.\n");
                }
                else {
                    e.waitlist.add(studNum);
                    //e.waitlist.add(studName);
                    System.out.println("\nAdded to wailist\n");
                }

                found = true;
                break;

            }
        }

        if (!found) {
            System.out.println("Event not found");
        }

    }

    //function to cancel registration
    void cancelReg() {

        System.out.println("---------Cancel registration----------");

        staff.view();

        System.out.print("Enter event Id: ");
        int eventID = input.nextInt();
        input.nextLine();

        System.out.print("Enter student number: ");
        String studNum = input.nextLine();

        boolean found = false;

        for (Event e : staff.events){

            if (e.eventID == eventID) {
                //removing from the registration list
                if (e.registered.remove(studNum)) {
                    System.out.println("Registration Cancelled!");

                    if (!e.waitlist.isEmpty()) {
                        new Thread(() -> {
                            try {
                                Thread.sleep(1000); //delay
                            } catch (InterruptedException ex) {}

                            String promoted = e.waitlist.poll();

                            if(promoted != null){
                                e.registered.add(promoted);

                                System.out.println("Student: " + promoted + " has been promoted from waitlist");
                            }

                        }).start();

                        found = true;
                        break;
                    }
                    if (e.waitlist.remove(studNum)) {
                        System.out.print("Removed from waitlist");
                        found= true;
                        break;
                    }
                }
            }
        }
        if (!found) {
            System.out.println("Student or event not found!");
        }

    }

    //view status function for students for events if either wailist or registered
    void viewStatus() {

        System.out.println("\n---------Viest Status----------\n");

        System.out.print("Enter student Number: ");
        String studNum = input.nextLine();

        boolean found = false;

        for (Event e: staff.events) {

            if(e.registered.contains(studNum)) {
                System.out.println("===========================================");
                System.out.println("\tEvent: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tStatus: REGISTERED"); //registered output if registered
                System.out.println("===========================================");
                found = true;
            }

            if (e.waitlist.contains(studNum)) {
                System.out.println("===========================================");
                System.out.println("\tEvent: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tStatus: WAITLIST"); //registered output if registered but under waitlist
                System.out.println("===========================================");
                found = true;
            }
        }
        if (!found) {
            System.out.println("No registration found for this student."); //if student number is not found in the regisdtration or waitlist
        }

    }

    //main entry function for students
    void optionStudent() {

        System.out.println("\n------------Welcome Student-----------\n");

        List<String> option = new LinkedList<>();
            option.add("1. View Events");
            option.add("2. Register for event");
            option.add("3. Cancel registration");
            option.add("4. View status");
            option.add("5. Exit");

        while(true) {

            System.out.println("------------student Menu-----------");

            for(String options : option) {
                System.out.println(options);
            }

            System.out.println();

            System.out.print("Enter option: ");
            int opt = input.nextInt();
            input.nextLine();

            if (opt == 1) {

                System.out.println("\n\t---Events---");
                staff.view();
                staff.saveToFile();
                continue;
            }
            else if (opt == 2) {
                register();
                staff.saveToFile();
                continue;
            }
            else if(opt == 3) {
                cancelReg();
                staff.saveToFile();
                continue;
            }
            else if (opt == 4) {
                viewStatus();
                staff.saveToFile();
                continue;
            }
            else if (opt == 5) {
                break;
            }
            else {
                System.out.println("option not found");
                continue;
            }
        }
    }

}


//main class
public class CEMS {

    //main function
    public static void main(String[] args) {

        //calling classes to main class
        Scanner input = new Scanner(System.in);
        Staff staff = new Staff(input);
        Student student = new Student(staff, input);
        staff.loadFromFile();

        //main menu where staff and student choose thier department
        List<String> department = new LinkedList<>();
            department.add("1. Staff");
            department.add("2. Student");
            department.add("3. Search Event"); 
            department.add("4. Exit"); 

        while(true) { //usimg while loop to validate if user enters wrong unput
            
            System.out.println("----------Main Menu----------");

            for (String d : department) {
                System.out.println("\t" + d);
            }

            ///collecting user input
            System.out.print("Enter option: ");
            int dep = Integer.parseInt(input.nextLine());

            //calling all the functions from classes based on option from user
            if (dep == 1) {

                staff.optionStaff();

                continue;

            }

            else if (dep == 2) {

                student.optionStudent();
                
                continue;
            }

            else if (dep == 3) {

                //searching and sorting events
                System.out.println("---------Search event----------");

                if (staff.events.isEmpty()) {
                    System.out.println("\nNo available events\n");
                    continue;
                }
                
                List<String> sort = new LinkedList<>();
                    sort.add("1. name");
                    sort.add("2. date");

                System.out.println("\t- Sort by: -");

                for (String s : sort) {
                    System.out.println("\t" + s);
                }

                // while (true) {
                //     if (mode == 1) {
                //         break;
                //     }
                //     else if (mode == 2) {
                //         break;
                //     }
                //     else {
                //         System.out.println("option not found");
                //         continue;
                //     }
                // }

                //choosint if sorting with name or date
                System.out.print("Sort by name or date? ");
                int mode = input.nextInt();
                input.nextLine();

                //sorting events
                if (mode == 1) {
                    staff.events.sort((a, b) -> a.eventName.compareToIgnoreCase(b.eventName)); //sorting events by name
                }
                else if (mode == 2) {
                    staff.events.sort((a, b) -> a.eventDate.compareTo(b.eventDate)); //sorting event by date
                }
                else {
                    System.out.println("option not found!");
                    continue;
                }

                //searching event by name
                System.out.print("Search event by name: ");
                String search = input.nextLine();

                boolean found = false;

                for (Event e : staff.events) {

                    //staff.events.sort((a, b) -> a.eventName.compareToIgnoreCase(b.eventName)); //sorting events by name

                    //printing events sorted by name
                    if(mode == 1) {
                         if (e.eventName.toLowerCase().contains(search.toLowerCase())) {
                        System.out.println("--------------Events------------------");

                        System.out.println("\n\tId: " + e.eventID + "\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                        System.out.println("--------------------------------------");
                        found= true;
                        }
                    }
                
                    //printing events sorted by date
                    else if (mode == 2) {
                        if (e.eventDate.toLowerCase().contains(search.toLowerCase())) {
                            System.out.println("--------------Events------------------");

                            System.out.println("\n\tId: " + e.eventID + "\n\tName: " + e.eventName + "\n\tDate: " + e.eventDate + "\n\tTime: " + e.eventTime + "\n\tLocation: " + e.location + "\n\tMax Participants: " + e.maxParc + "\n");

                            System.out.println("--------------------------------------");
                            found = true;
                        }
                    }

                }

                if (!found) {
                    System.out.println("Event not found!");
                    return;
                }

            }

            else if (dep == 4) {
                System.out.println("Exiting....");
                break;
            }
            else {
                System.out.println("Department not found!");
                continue;
            }

        }
        

        staff.saveToFile(); //saving data to file text everytime before the program stops

        input.close(); //closing the Scanner

    }

}
