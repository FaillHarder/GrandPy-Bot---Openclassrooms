let form = document.querySelector("#user_text_form");
let loader = document.querySelector(".loader");


async function postFormData(url, data) {
    let rep = await fetch(url, {
        method: "POST",
        body: data
    });
    let response = await rep.json();
    return response
}



form.addEventListener("submit", async function (event) {
    event.preventDefault();

    loader.className = "loader";
    let response = await postFormData("/ajax", new FormData(form))
    if ("grandpy_error" in response) {
        displayBadInput(response)    
    } else {
        displayGoodInput(response)
    }
    loader.className += " hidden"
    rezUserInput()
})

function displayGrandpyMessage(message) {
    let messageList = document.getElementsByClassName("conversation");
    let newDiv = document.createElement("div");
    newDiv.className = "bubble bubble-bottom-left";
    newDiv.innerHTML = "🤖👴" + message;
    messageList[0].prepend(newDiv);
}

function displayUserMessage(user_input) {
    let messageList = document.getElementsByClassName("conversation");
    let newDiv = document.createElement("div");
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
    displayMap(coords)
}

function displayMap(coords) {
    let marker = new H.map.Marker(coords, { icon: icon });
    map.setCenter(coords);
    map.setZoom(14);
    map.addObject(marker);
}