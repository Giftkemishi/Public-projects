<!DOCTYPE html>

    <html>

        <head>

            <title>
                Fun Near Me
            </title>

            <link rel="stylesheet" type="text/css" href="FNM.css">

        </head>

        <body>

            <h1 align="center" style="color:white;">Fun In Mzansi</h1>

            <div class="main_display">

            

                <form method="POST" action="">

                    <div class="btn_Ins_container">
                        <button type="submit" name="action" value="logIn" class="btn1-1">Log In</button>
                        <button type="submit" name="action" value="signIn" class="btn1-2">Sign In</button>
                    </div>

                    <div class="button-container">

                        <button type="submit" name="action" value="northern_cape" class="btn btn1">Northern Cape</button>

                        <button type="submit" name="action" value="north_west" class="btn btn2">North West</button>

                        <button type="submit" name="action" value="gauteng" class="btn btn3">Gauteng</button>

                        <button type="submit" name="action" value="western_cape" class="btn btn4">Western Cape</button>
                    
                        <button type="submit" name="action" value="limpopo" class="btn btn5">Limpopo</button>
                    
                        <button type="submit" name="action" value="mpumalanga" class="btn btn6">Mpumalanga</button>

                        <button type="submit" name="action" value="free_state" class="btn btn7">Free State</button>

                        <button type="submit" name="action" value="kwazulu" class="btn btn8">Kwazulu Natal</button>

                        <button type="submit" name="action" value="eastern_cape" class="btn btn9">Eastern Cape</button>

                    </div>

                </form>  

                <div class="padding">
                    

                </div>

                <?php

                    if ($_SERVER["REQUEST_METHOD"] == "POST") {

                        if (isset($_POST['action'])) {
                            $action = $_POST['action'];

                            echo '<div class="dynamic-content">';

                            if ($action == 'limpopo') {

                                echo '<div class="btn_margin">';

                                    echo '<form method="POST" action="">';

                                        echo '<button type="submit" name="action" value="polokwane" class="btns btnC1"> Polokwane </button>';
                                        echo '<button type="submit" name="action" value="mokopane" class="btns btnC1"> Mokopane </button>';
                                        echo '<button type="submit" name="action" value="lebcow" class="btns btnC1"> Lebowakgomo </button>';
                                        echo '<button type="submit" name="action" value="venda" class="btns btnC1"> Venda </button>';
                                        echo '<button type="" name="" value="" class="btns btnC1"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'gauteng') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC2">Pretoria</button>';
                                        echo '<button type="" name="" value="" class="btns btnC2">Johannesburg</button>';
                                        echo '<button type="" name="" value="" class="btns btnC2">Mamelodi</button>';
                                        echo '<button type="" name="" value="" class="btns btnC2">Soshanguve</button>';
                                        echo '<button type="" name="" value="" class="btns btnC2"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'northern_cape') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC3">Upington</button>';
                                        echo '<button type="" name="" value="" class="btns btnC3">Kimberly</button>';
                                        echo '<button type="" name="" value="" class="btns btnC3"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC3"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC3"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'kwazulu') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC4">Richards Bay</button>';
                                        echo '<button type="" name="" value="" class="btns btnC4">Pietermaritzburg</button>';
                                        echo '<button type="" name="" value="" class="btns btnC4">Durban</button>';
                                        echo '<button type="" name="" value="" class="btns btnC4"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC4"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'free_state') {

                                echo '<div class="btn_margin">';;

                                echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC5">Welkom</button>';
                                        echo '<button type="" name="" value="" class="btns btnC5">Bloemfontein</button>';
                                        echo '<button type="" name="" value="" class="btns btnC5"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC5"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC5"></button>';

                                    echo '</form>';
                                
                                echo "</div>";

                            } else if ($action == 'mpumalanga') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC6">Mbombela</button>';
                                        echo '<button type="" name="" value="" class="btns btnC6">Hazyview</button>';
                                        echo '<button type="" name="" value="" class="btns btnC6"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC6"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC6"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'north_west') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC7">Mahikeng</button>';
                                        echo '<button type="" name="" value="" class="btns btnC7"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC7"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC7"></button>';
                                        echo '<button type="" name="" value="" class="btns btnC7"></button>';

                                    echo '</form>';
                                
                                echo "</div>";

                            } else if ($action == 'western_cape') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC8">Cape Town</button>';
                                        echo '<button type="" name="" value="" class="btns btnC8">Beaufort west</button>';
                                        echo '<button type="" name="" value="" class="btns btnC8">Oudtshroom</button>';
                                        echo '<button type="" name="" value="" class="btns btnC8">Mossel bay</button>';
                                        echo '<button type="" name="" value="" class="btns btnC8"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'eastern_cape') {

                                echo '<div class="btn_margin">';;

                                    echo '<form>';

                                        echo '<button type="" name="" value="" class="btns btnC9">Bhisho</button>';
                                        echo '<button type="" name="" value="" class="btns btnC9">East london</button>';
                                        echo '<button type="" name="" value="" class="btns btnC9">Gqeberha</button>';
                                        echo '<button type="" name="" value="" class="btns btnC9">Mthata</button>';
                                        echo '<button type="" name="" value="" class="btns btnC9"></button>';

                                    echo '</form>';

                                echo "</div>";

                            } else if ($action == 'logIn') {

                                echo '<div class="sndpage" align="center">';

                                   

                                        echo '<div style="display :flex;"  class="logIn_container">';
                                    
                                            echo '<form class="log_form" method="POST" action="" align="center" style="margin-top: 5%;">';

                                            echo '<h1 class="heading_in_padding">Are You Hosting?</h1>';
                                            echo '<h2 class="heading_in_padding">Log In</h2>';

                                            echo '<input type="hidden" name="action_type" value="log_in">';
                                                
                                                echo '<div class="logF1">';
                                                    echo '<input  style="margin-bottom:10px;" class="input" type="email" name="email" id="mail"placeholder="Email"></input><br>';
                                                    echo '<input style="margin-bottom:15px;" class="input" type="password" name="password" id="pass" placeholder="Password"><br>';
                                                    echo '<button type="submit" name="logIn_sub" value="log_in_btn" class="logbtn" id="loggedbtn">Log In</button>';
                                                    echo '<button class="input" type="submit" name="action" value="home">Home</button>';
                                                echo '</div>';

                                                echo '<div style="display:flex; margin-top: 5px;">';
                                                    echo '<input style="margin-left: 16%;" type="checkbox" name="remember" id="Rmbr" class="Rmbr"><b  style="color: white;">Remember me</b></input><br>';
                                                    echo '<a href="" style="color: white; margin-left: 15%;" type="submit" name="action" value="Signbtn" class="">Create an account</a>';
                                                echo '</div>';
                                                

                                            echo '</form>';

                                        echo '</div>';

                                    

                                    /*if (isset($_POST['log_in_btn'])) {
                                        $action = $_POST['log_in_btn'];
                                        $email = $_POST['email'];
                                        $password = $_POST['password'];
                                        $correctEmail = 'gift@gmail.com';
                                        $correctPassword = '12345';*/

                                        if (isset($_POST['logIn_sub']) && $_POST['logIn_sub'] == 'log_in_btn') {
                                            if (isset($_POST['email']) && isset($_POST['password'])) {
                                              $email = $_POST['email'];
                                              $password = $_POST['password'];
                                              $correctEmail = 'gift@gmail.com';
                                              $correctPassword = '12345';
                                        
                                          

                                        if ($email == $correctEmail && $password == $correctPassword) {

                                             echo '<div style="margin-top: 10%;" class="event_container" align="center">';

                                                echo '<form class="event_form">';

                                                    echo '<input class="input" name="" id="" placeholder="" type=""><br>';

                                                    echo '<input class="input" name="" id="" placeholder="Time and date" type="datetime-local"><br>';

                                                    echo '<input class="input" name="" id="" placeholder="Cell number" type="tel"><br>';

                                                    echo '<input class="input" name="" id="" placeholder="street" type="text"><br>';

                                                    echo '<input class="input" name="" id="" placeholder="City/town" type="text"><br>';
                                                    
                                                    echo '<input class="inputSubbtns" name="" id="" placeholder="Zip code" type="text"><br>';

                                                    echo '<input class="inputSubbtns" name="" id="" placeholder="" type="image"><br>';
                                                   

                                                echo '</form>';

                                             echo '</div>';

                                        } else {
                                            echo "Wrong log ins";

                                        }
                                    }}
                                    

                                echo '</div>';

                                    

                            } else if ($action == 'signIn' || 'Singbtn') {

                                echo '<div class="signIn_container">';

                                    echo '<form class="sign_form" align="center">';

                                    echo '<h1 class="heading_in_padding">Wanna be a Hoster?</h1>';
                                       echo '<h2 class="heading_in_padding">Sign In</h2>';

                                        echo '<div style="margin-top: -20%;">';
                                            echo '<input class="input" type="text" name="name" placeholder="Name:"></input><br>';

                                            echo '<input class="input" type="text" name="surname" placeholder="Surname:"></input><br>';

                                            echo '<input class="input" type="email" name="email" placeholder="Email:"></input><br>';

                                            echo '<input class="input" type="tel" name="telphone" placeholder="Cell Number:"></input><br>';

                                            echo '<input class="input" type="password" name="password" placeholder="Password:"></input><br>';

                                            echo '<input class="input" type="password" name="Conpassword" placeholder="Confirm Password:"></input><br>';

                                            echo '<div style="diplay: relative;">';
                                                echo '<button class="inputSubbtns" type="submit" name="action" value="signedIn">Sign In</button><br>';

                                                echo '<button class="inputSubbtns" type="submit" name="action" value="home">Home</button>';
                                            echo '</div>';    

                                        echo '</div>';

                                    echo '</form>';

                                echo '</div>';

                            } else { echo "Province not found, probably not in Mzansi."; }

                        echo '</div>';

                        }
                    }  


                ?>

                

            </div>

            <script src="FNM.js"> </script>

        </body>

        <footer>

        </footer>

    </html>
