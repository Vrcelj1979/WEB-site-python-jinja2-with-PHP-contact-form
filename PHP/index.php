<?php

if ($_POST['submit']) {

	if (!$_POST['name']) {
		$error="<br>- Please enter your name";
	}

	if (!$_POST['email']) {
		$error.="<br>- Please enter your email";
	}

	if (!$_POST['message']) {
		$error.="<br>- Please enter a message";
	}

	if (!$_POST['check']) {
		$error.="<br>- Please confirm that are you human";
	}

	if ($error) {
		$result='<div class="alert alert-danger" role="alert"><strong>Whoops, there is an error</strong>. Please correct the following: '.$error.'</div>';
	} else{
		mail("svposejdon@gmail.com", "Contact message", 
        "Name: ".$_POST['name']."    
		Email: ".$_POST['email']."
		Message: ".$_POST['message']);

		{
		$result='<div class="alert alert-success" role="alert">Thank you, I\'ll be in touch shortly</div>';	
		}	

	}


}

?>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>index.php</title>

    
    <link href="https://cpstat-216518.appspot.com/assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cpstat-216518.appspot.com/assets/style.css" rel="stylesheet">

   
  </head>
  <body>
    
    <section id="contact">
      <div class="container">
        <div class="row">
          <div class="col-md-6 col-md-offset-3">
            <h1>Contact form</h1>

            <?php echo $result;?>

            <p>Send a message view the form below</p>

            	<form method="post" role="form">
            		<div class="form-group">
            			<input type="text" name="name" class="form-control" placeholder="Your name" value="<?php echo $_POST['name']; ?>">
            		</div>

            		<div class="form-group">
            			<input type="email" name="email" class="form-control" placeholder="Your email" value="<?php echo $_POST['email']; ?>">
            		</div>

            		<div class="form-group">
            			<textarea name="message" rows="5" class="form-control" placeholder="message..."><?php echo $_POST['message']; ?></textarea>
            		</div>

            		<div class="checkbox">
            			<label>
            				<input type="checkbox" name="check">I am human
            			</label>
            		</div>

            		<div align="center">
            			<input type="submit" name="submit" class="btm btm-secondary" value="send message"/>
            		</div>
            	</form>


          </div>  
        </div>
      </div>
    </section>
   
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    
    <script src="https://cpstat-216518.appspot.com/assets/js/bootstrap.min.js"></script>
  </body>
</html>