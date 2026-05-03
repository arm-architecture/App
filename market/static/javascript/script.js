element = document.getElementById("django-image");
element.addEventListener("click", function() {

     element.style.width = "500px";
     element.style.height = "350px";
     element.style.border = "10px solid red";
     element.style.borderRadius = "50%";
    alert("You clicked the Django logo!");
});