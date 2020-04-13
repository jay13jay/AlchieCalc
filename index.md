<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>AlchieCalc</title>
    <link rel="shortcut icon" type="image/png" href="static/images/favicon.ico"/>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>  <body>
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container">
        <ul class="nav navbar-nav">
          <li><a class="navbar-brand" href="/calc.html">Alchie Calc</a></li>
        </ul>
      </div>
    </nav>

    <div class="container">
      <div class="jumbotron">
        <!-- Put all main content within the jumbotron -->
        <!-- sidebars should go outside of the container-->
        <form style="width: 15%;">
          <div class="form-group">
            <label for="unitType">Please select unit to use</label>
            <select class="form-control" id="unitType">
              <option>Ounces</option>
              <option>Milli Liters</option>
              <option>Liters</option>
            </select>
          </div>

          <div class="form-group" style="height: 10%;>
            <label for="ABVInput">Enter ABV% of beverage</label>
            <input type="number" min="0" class="form-control" id="ABVInput" rows="1"></textarea>
          </div>

          <div class="form-group">
            <label for="VolumeInput">Enter volume of beverage</label>
            <input type="number" class="form-control" id="VolumeInput" rows="1"></textarea>
          </div>

          <div class="form-group">
            <label for="PriceInput">Enter price of beverage</label>
            <input type="number" min="0" step="0.01" class="form-control" id="PriceInput" rows="1"></textarea>
          </div>
          <!-- Answer = <input type="text" id="answer" name="answer" value=""/>

          <button type="submit" class="btn btn-outline-primary" onclick="javascript:addNumbers()">Calculate</button> -->
          <div id="demo">
            <button type="button" class="btn btn-outline-primary" onclick="loadDoc()">Calculate</button>
            </div>
            
            <script>
            function loadDoc() {
              var xhttp = new XMLHttpRequest();
              xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                  document.getElementById("demo").innerHTML =
                  this.responseText;
                }
              };
              xhttp.open("GET", "static/files/ajax_info.txt", true);
              xhttp.send();
            }
            </script>

        </form>

      </div>
    </div>

    <!-- <script language="javascript">
      function addNumbers()
      {
              var val1 = parseInt(document.getElementById("ABVInput").value);
              var val2 = parseInt(document.getElementById("VolumeInput").value);
              var ansD = document.getElementById("answer");
              var val3 = val1 * val2;
              ansD.value = val3/100;
              document.write(ansD)
      }
</script> -->
  </body>
</html>