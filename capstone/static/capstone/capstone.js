function showIndex(){
    var index = document.getElementById("index");
    var login = document.getElementById("login");
    var register = document.getElementById("register");

    if (index.style.display === "none") {
        index.style.display = "block";
        login.style.display = "none";
        register.style.display = "none";
    }
}

function showLogin(){
    var index = document.getElementById("index");
    var login = document.getElementById("login");
    var register = document.getElementById("register");

    if (login.style.display === "none") {
        login.style.display = "block";
        register.style.display = "none";
        index.style.display = "none";
    }
}

function showRegister(){
    var index = document.getElementById("index");
    var login = document.getElementById("login");
    var register = document.getElementById("register");

    if (register.style.display === "none") {
        register.style.display = "block";
        index.style.display = "none";
        login.style.display = "none";
    }
}

function results(){
    var calculator = document.getElementById("calculator");
    var calcResults = document.getElementById("calc-results");

    var food = document.getElementById("food").value;
    var calories = document.getElementById("calories").value;
    var weight = document.getElementById("weight").value;

    if (calculator.style.display === "none") {
        calculator.style.display = "block";
        calcResults.style.display = "none";
    } else {
        calculator.style.display = "none";
        calcResults.style.display = "block";
    }
}