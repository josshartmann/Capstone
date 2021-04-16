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

function time_convert(num) { 
    var hours = Math.floor(num / 60);  
    var minutes = num % 60;
    return hours + ":" + Math.round(minutes);         
}

function popResults(id) {
    var id = id
    var calories = document.getElementById(`caloriesLog-${id}`).innerText;
    var weight = document.getElementById(`weightLog-${id}`).innerText;
    

    var A = ((parseInt(calories) * 200) / (13.5 * 3.5 * parseInt(weight)))
    var runningLog = document.getElementById("runningLog").innerText = time_convert(A)

    var B = (parseInt(calories) * 200) / (10 * 3.5 * parseInt(weight))
    var bicycling16Log = document.getElementById("bicycling16Log").innerText = time_convert(B)

    var C = (parseInt(calories) * 200) / (8 * 3.5 * parseInt(weight))
    var swimmingLog = document.getElementById("swimmingLog").innerText = time_convert(C)

    var D = (parseInt(calories) * 200) / (7 * 3.5 * parseInt(weight))
    var calisthenicsLog = document.getElementById("calisthenicsLog").innerText = time_convert(D)

    var E = (parseInt(calories) * 200) / (4.8 * 3.5 * parseInt(weight))
    var dancingLog = document.getElementById("dancingLog").innerText = time_convert(E)

    var F = (parseInt(calories) * 200) / (4 * 3.5 * parseInt(weight))
    var bicycling10Log = document.getElementById("bicycling10Log").innerText = time_convert(F)

    var G = (parseInt(calories) * 200) / (2 * 3.5 * parseInt(weight))
    var walkingLog = document.getElementById("walkingLog").innerText = time_convert(G)
    

    var element = document.getElementById("logResults");

    if (element.style.display == 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }

    
}