

let form = document.querySelector("#user_text_form");
let text = document.querySelector(".conversation");


function posFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error))
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    posFormData("/ajax", new FormData(form))
    .then(response => {
        
        displayGrandpyMessage(response["grandpy_address"])
        displayInfo(response["address"])
        displayGrandpyMessage(response["grandpy_descript"])
        displayInfo(response["descriptif"])
        
        let lat = response["lat"]
        let lng = response["lng"]
        coords = {lat, lng}
        map.setCenter(coords);
        map.addObject(new H.map.DomMarker(coords, {icon: icon}));
    })
})

const parent = document.querySelector(".conversation");

function displayUserMessage(submit) {
    let user = document.createElement("p");
    parent.appendChild(user);
    user.innerHTML = submit;
}

function displayGrandpyMessage(message) {
    let grandpy = document.createElement("p");
    grandpy.className = "bubble bubble-bottom-left";
    parent.appendChild(grandpy);
    grandpy.innerHTML = message;
}

function displayInfo(data) {
    let info = document.createElement("p");
    info.className = "info";
    parent.appendChild(info);
    info.innerHTML = data;
}

