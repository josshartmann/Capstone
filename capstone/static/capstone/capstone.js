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
    if (minutes < 10) {
        return hours + ":0" + Math.round(minutes);
    } else {
        return hours + ":" + Math.round(minutes);
    }       
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

function printFunc() {
    window.print();
}


function editFunc() {
    var edit = document.getElementById('btnEdit');
    var save = document.getElementById('btnSave');
    var email = document.getElementById('profileEmail');
    var phone = document.getElementById('profilePhone');
    var profession = document.getElementById('profileProfession');
    var edit_email = document.getElementById('editEmail');
    var edit_phone = document.getElementById('editPhone');
    var edit_profession = document.getElementById('editProfession')

    edit.style.display = 'none';
    save.style.display = 'block';

    email.style.display = 'none';
    phone.style.display = 'none';
    profession.style.display = 'none';
    edit_email.style.display = 'block';
    edit_phone.style.display = 'block';
    edit_profession.style.display = 'block';
}

function save() {
    var edit = document.getElementById('btnEdit');
    var save = document.getElementById('btnSave');
    var email = document.getElementById('profileEmail');
    var phone = document.getElementById('profilePhone');
    var profession = document.getElementById('profileProfession');
    var edit_email = document.getElementById('editEmail');
    var edit_phone = document.getElementById('editPhone');
    var edit_profession = document.getElementById('editProfession');
    var head_profession = document.getElementById('headProfession');
        
    email.innerHTML = edit_email.value;
    phone.innerHTML = edit_phone.value;
    profession.innerHTML = edit_profession.value;
    head_profession.innerHTML = edit_profession.value;

    edit.style.display = 'block';
    save.style.display = 'none';

    email.style.display = 'block';
    phone.style.display = 'block';
    profession.style.display = 'block';
    edit_email.style.display = 'none';
    edit_phone.style.display = 'none';
    edit_profession.style.display = 'none';
}

function openForm() {
    form = document.getElementById("my-form");
    if (form.style.display == "block") {
        document.getElementById("my-form").style.display = "none";
    } else {
        document.getElementById("my-form").style.display = "block";
    }
}

function openWindow(exercise) {
    window.open(`https://www.google.com/search?q=${exercise}&tbm=isch`)
}

window.onload=function(){
    var checkboxes = document.getElementsByClassName('checkme');
    var sendbtn = document.getElementById('createWorkout');
    var length = checkboxes.length;

    for (var i=0;i<length;i++) {
            var box = checkboxes[i];
            var isChecked = box.checked;
            box.onchange = function() {
                sendbtn.disabled = isChecked?true:false;
            }
        }
    }