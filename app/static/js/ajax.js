let form = document.querySelector("#user_text_form");
const parent = document.querySelector(".conversation");


function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .catch(error => console.log(error))
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    postFormData("/ajax", new FormData(form))
    .then(response => {
        
        if ("grandpy_error" in response) {
            displayBadInput(response)
            rezUserInput()
        } else {
            displayGoodInput(response)
            rezUserInput()
        }
    })
})


function displayGrandpyMessage(message) {
    let grandpy = document.createElement("p");
    grandpy.className = "bubble bubble-bottom-left";
    parent.appendChild(grandpy);
    grandpy.innerHTML = "🤖👴" + message;
}

function displayUserMessage(user_input) {
    let user = document.createElement("p");
    user.className = "bubble2 bubble-bottom-right";
    parent.appendChild(user);
    user.innerHTML = user_input;
}

function displayInfo(data) {
    let info = document.createElement("p");
    info.className = "info";
    parent.appendChild(info);
    info.innerHTML = data;
}

function rezUserInput() {
    let rez = document.getElementById("user_input");
    rez.value = ""
}

function displayBadInput(response) {
    let user_input = document.getElementById("user_input").value;
    displayUserMessage(user_input)
    displayGrandpyMessage(response["grandpy_error"])
}

function displayGoodInput(response) {
    let user_input = document.getElementById("user_input").value;
    displayUserMessage(user_input)
    displayGrandpyMessage(response["grandpy_address"])
    displayInfo(response["address"])
    displayGrandpyMessage(response["grandpy_descript"])
    displayInfo(response["descriptif"])
    let lat = response["lat"]
    let lng = response["lng"]
    coords = {lat, lng}
    map.setCenter(coords);
    map.setZoom(14);
    map.addObject(new H.map.DomMarker(coords, {icon: icon}));
}
