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
    const messageList = document.getElementsByClassName("conversation");
    const newDiv = document.createElement("div");
    newDiv.className = "bubble bubble-bottom-left";
    newDiv.innerHTML = "🤖👴" + message;
    messageList[0].prepend(newDiv);
}

function displayUserMessage(user_input) {
    const messageList = document.getElementsByClassName("conversation");
    const newDiv = document.createElement("div");
    newDiv.className = "bubble2 bubble-bottom-right";
    newDiv.innerHTML = user_input;
    messageList[0].prepend(newDiv);
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
    displayGrandpyMessage(response["grandpy_address"] + response["address"])
    displayGrandpyMessage(response["grandpy_descript"] + response["descriptif"])
    let lat = response["lat"]
    let lng = response["lng"]
    coords = {lat, lng}
    map.setCenter(coords);
    map.setZoom(14);
    map.addObject(new H.map.DomMarker(coords, {icon: icon}));
}
