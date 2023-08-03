# Microservices-with-Docker-flask-and-react

<p>Projet de creation d'un site web de gestion d'interactions utilisateurs (login , register , authentification , authorization , test unitaires , developpement et Integration continu , ...) et les operations CRUD sur base de données avec React et flask , tout ceci empaqueter dans des conteneurs Docker pour une meilleure autonomie et modelisé suivant une architecture microservice.</p>
<p>
	<img alt="Static Badge" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
	<img alt="Static Badge" src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white">
</p>
<h2>Table de matiere</h2>
<ol style = "list-type-style: squarre">
	<li><a href = "">Concept de microservices</a></li>
	<li><a href = "">Architecture du site</a></li>
	<li><a href = "">Differents microservices</a></li>
	<li><a href = "">Interface utilisateur</a></li>
	<li><a href = "">Installation et utilisation du projet</a></li>
  	<li><a href = "">Crédit </a></li>  
</ol>
<div style = "border-top = 2px solid red" id = "h1">
  <h2 font-color = "red">Concept d'architecture microservice</h2>
	<p>L'architecture Microservices propose une solution en principe simple : découper une application en petits services, appelés Microservices, parfaitement autonomes, qui exposent une API REST que les autres microservices pourront consommer. <br>
	<img alt = "Image de microservice" src = "https://user.oc-static.com/upload/2021/12/15/16395870123069_FR_4668056_Banner%26Statics_p1c2-1.jpg"/><br>
		Chaque microservice est parfaitement autonome : il a sa propre base de données, son propre serveur d'application (Tomcat, Jetty, etc.), ses propres librairies et ainsi de suite. La plupart du temps, ces microservices sont chacun dans un container Docker, ils sont donc totalement indépendants y compris vis-à-vis de la machine sur laquelle ils tournent.
	</p>
</div>
<div style = "border-top = 2px solid red" id = "h2">
  <h2 font-color = "red">Architecture du site</h2>
	<p>Le site web fonctionne suivant une architecture de microservices. C'est-à-dire que toutes les fonctionalités du systeme sont divisées en de petits microservices possedant chacun sa base de données , ses langages de programmations spécifiques, empaquetés dans des containeurs Docker et retournant une reponse sous format JSON qui sera integré à l'interface utilisateur.<br>
	Comme services , c'est un site web qui permet d'inscrire et/ou de connecter les utilisateurs aux fonctionnalité d'un système en passant par les tests d'interface, d'authentification , des integrations contitnues et la sauvegarde des information utilisateurs dans une base de données. A chaque fonctionnalités il existe un service specialisé. Chaque service est empaqueter sous Docker puis deployé avec <strong>Amazon EC2<strong>.<br>
		<img alt = "Image de l'architecture" src = "./docs/Architecture.jpeg" />
	</p>
	
</div>
<div style = "border-top = 2px solid red" id="h3">
  <h2 font-color = "red">Differents services</h2>
	<p></p>
</div>
<div style = "border-top = 2px solid red" id="h4">
  <h2 font-color = "red">Interface utilisateur</h2>
	<p></p>
</div>
<div style = "border-top = 2px solid red" id = "h5">
  <h2 font-color = "red">Installation et utilisation du projet</h2>
	<h3><li>A partir de Docker</li> </h3>
	<p>Docker. Docker est un logiciel qui permet de créer et de gérer des conteneurs, qui sont des environnements isolés pour exécuter des applications. Pour installer Docker, vous devez suivre les étapes suivantes, selon votre système d’exploitation:</p>
	<h3><li>Grace à l'environnement virtuel</li></h3> 
</div>
<div style = "border-top = 2px solid red" id ="h6">
  <h2 font-color = "red">Credits</h2>
	<h3>Langages utilisés</h3>
	<p>
		<img alt="Static Badge" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  		<img alt="Static Badge" src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
		<img alt="Static Badge" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
	</p>
 <h3>Me contacter</h3>
 <p>
	 <img alt="Static Badge" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Quora-%23B92B27.svg?&style=for-the-badge&logo=Quora&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
 </p>
	
</div>
