--% index/fmus
htmlcss,d(/mk)
	%utama=__FILE__
	sidebar1.css,f(e=__FILE__=sidebar1.css)
	sidebar1.html,f(e=__FILE__=sidebar1.html)
	sidebar2.css,f(e=__FILE__=sidebar2.css)
	sidebar2.html,f(e=__FILE__=sidebar2.html)
	sidebar3.css,f(e=__FILE__=sidebar3.css)
	sidebar3.html,f(e=__FILE__=sidebar3.html)
	$* npx http-server -p 9200
--#

--% sidebar1.css
body {
  margin: 0;
  padding: 0;
  font-family: verdana;
  background: #fff;
  overflow: hidden;
}

.sidebar {
  position: fixed;
  top: 0;
  left: -250px;
  background: #262626;
  width: 250px;
  height: 100%;
  transition: .3s;
}

.active {
  left: 0;
}

ul {
  margin: 0;
  padding: 20px 0;  
}

ul li {
  list-style: none;  
}

ul li a {
  padding: 10px 20px;
  color: #fff;
  display: block;
  text-decoration: none;
  border-bottom: 1px solid rgba(0,0,0,.2);
}

.sidebarBtn {
  position: absolute;
  top: 0;
  right: -50px;
  width: 50px;
  height: 50px;
  box-sizing: border-box;
  cursor: pointer;
  background: #f5f5f5;
  border: none;
  outline: none;
}

.sidebarBtn span {
  display: block;
  width: 35px;
  height: 3px;
  background: #262626;
  position: absolute;
  top: 24px;
  transition: .3s;
}

.sidebarBtn span:before {
  content: '';
  position: absolute;
  top: -10px;
  left: 0;
  width: 100%;
  height: 3px;
  background: #262626;
  transition: .3s;
}

.sidebarBtn span:after {
  content: '';
  position: absolute;
  top: 10px;
  left: 0;
  width: 100%;
  height: 3px;
  background: #262626;
  transition: .3s;
}

.sidebarBtn.toggle span {
  background: transparent;
}

.sidebarBtn.toggle span:before {
  top: 0;
  transform: rotate(45deg);
}

.sidebarBtn.toggle span:after {
  top: 0;
  transform: rotate(-45deg);
}
--#

--% sidebar1.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="sidebar1.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous"></script>
  <script>
    $(document).ready(function() {
      $('.sidebarBtn').click(function() {
        $('.sidebar').toggleClass('active');
        $('.sidebarBtn').toggleClass('toggle');
      })
    })
  </script>
</head>
<body>
  <div class="sidebar">
    <ul>
      <li><a href="#">Satu</a></li>
      <li><a href="#">Dua</a></li>
      <li><a href="#">Tiga</a></li>
      <li><a href="#">Empat</a></li>
      <li><a href="#">Lima</a></li>
    </ul>
    <button class="sidebarBtn">
      <span>
      </span>
    </button>
  </div>
</body>
</html>
--#


--% sidebar2.css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800;900&display=swap');

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Poppins', sans-serif;
}

body {
  background: #001a25;
}

#toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background: #03a9f4;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

#toggle::before {
  content: '';
  position: absolute;
  width: 28px;
  height: 2px;
  background: #fff;
  transform: translateY(-5px);
  transition: .2s;
}

#toggle::after {
  content: '';
  position: absolute;
  width: 28px;
  height: 2px;
  background: #fff;
  transform: translateY(5px);
  transition: .2s;
}

#toggle.active::before {

  transform: translateY(0px) rotate(45deg);

}

#toggle.active::after {
  transform: translateY(0px) rotate(-45deg);
}

#sidebar {
  position: fixed;
  top: 0;
  left: -300px;
  width: 300px;
  height: 100vh;
  background: #003147;
  transition: .5s;
}

#sidebar.active {
  left: 0px;
}

#sidebar ul {
  position: relative;
  margin-top: 50px;
}

#sidebar ul li {
  list-style: none;
  display: inline-block;
  width: 100%;
  padding: 10px 40px;
}

#sidebar ul li:hover {
  background: #03a9f4;
}

#sidebar ul li a {
  background: #fff;
  text-decoration: none;
  font-size: 1.5em;
  letter-spacing: 2px;
}
--#

--% sidebar2.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="sidebar2.css">

</head>
<body>
  
  <div id="toggle"></div>

  <div id="sidebar">
    <ul>
      <li><a href="#">Satu</a></li>
      <li><a href="#">Dua</a></li>
      <li><a href="#">Tiga</a></li>
      <li><a href="#">Empat</a></li>
      <li><a href="#">Lima</a></li>
    </ul>
  </div>

  <script>
    const toggle = document.getElementById('toggle');
    const sidebar = document.getElementById('sidebar');

    document.onclick = function(e) {
      if (e.target.id !== 'sidebar' && e.target.id !== 'toggle') {
        toggle.classList.remove('active');
        sidebar.classList.remove('active');  
      }
    }

    toggle.onclick = function() {
      toggle.classList.toggle('active');
      sidebar.classList.toggle('active');
    }
  </script>

</body>
</html>
--#


--% sidebar3.css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800;900&display=swap');

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Poppins', sans-serif;
}

body {
  background: #001a25;
}

#toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background: #03a9f4;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

#toggle::before {
  content: '';
  position: absolute;
  width: 28px;
  height: 2px;
  background: #fff;
  transform: translateY(-5px);
  transition: .2s;
}

#toggle::after {
  content: '';
  position: absolute;
  width: 28px;
  height: 2px;
  background: #fff;
  transform: translateY(5px);
  transition: .2s;
}

#toggle.active::before {

  transform: translateY(0px) rotate(45deg);

}

#toggle.active::after {
  transform: translateY(0px) rotate(-45deg);
}

#sidebar {
  position: fixed;
  top: 0;
  left: -300px;
  width: 300px;
  height: 100vh;
  background: #003147;
  transition: .5s;
}

#sidebar.active {
  left: 0px;
}

#sidebar ul {
  position: relative;
  margin-top: 50px;
}

#sidebar ul li {
  list-style: none;
  display: inline-block;
  width: 100%;
  padding: 10px 40px;
}

#sidebar ul li:hover {
  background: #03a9f4;
}

#sidebar ul li a {
  background: #fff;
  text-decoration: none;
  font-size: 1.5em;
  letter-spacing: 2px;
}
--#

--% sidebar3.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="sidebar3.css">

</head>
<body>
  
  <div id="toggle"></div>

  <div id="sidebar">
    <ul>
      <li><a href="#">Satu</a></li>
      <li><a href="#">Dua</a></li>
      <li><a href="#">Tiga</a></li>
      <li><a href="#">Empat</a></li>
      <li><a href="#">Lima</a></li>
    </ul>
  </div>

  <script>
    const toggle = document.getElementById('toggle');
    const sidebar = document.getElementById('sidebar');

    document.onclick = function(e) {
      if (e.target.id !== 'sidebar' && e.target.id !== 'toggle') {
        toggle.classList.remove('active');
        sidebar.classList.remove('active');  
      }
    }

    toggle.onclick = function() {
      toggle.classList.toggle('active');
      sidebar.classList.toggle('active');
    }
  </script>

</body>
</html>
--#
