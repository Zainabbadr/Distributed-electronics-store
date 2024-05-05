var userTable = document.getElementById('userTable');
var username = document.getElementById('username');
var firstname = document.getElementById('firstname');
var lastname = document.getElementById('lastname');
var email = document.getElementById('email');
var phone = document.getElementById('phone');
var user = null;
async function getuser() {
    var response = await fetch(`http://${window.location.host}/API/profile/?format=json`);
    var finalResponse = await response.json();
    console.log(finalResponse.username);
    user = finalResponse;
    displayUser();
}
getuser();

function displayUser() {
    username.innerHTML = user.username;
    email.innerHTML = user.email;
    firstname.innerHTML = user.first_name;
    lastname.innerHTML = user.last_name;
    phone.innerHTML = `+20${user.phone}`;
}
