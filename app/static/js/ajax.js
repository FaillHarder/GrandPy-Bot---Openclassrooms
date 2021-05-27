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
    // display loader img
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

function createDiv(classname1, classname2) {
    let newDiv = document.createElement("div");
    let newDiv2 = document.createElement("div");
    newDiv.className = classname1;
    newDiv2.className = classname2;
    return divList = [newDiv, newDiv2]
}

function displayGrandpyMessage(message) {
    let messageList = document.getElementsByClassName("conversation");
    let div = createDiv("bubble", "grandpy_box");
    div[0].innerHTML = "🤖👴" + message;
    div[1].appendChild(div[0]);
    messageList[0].prepend(div[1]);
}

function displayUserMessage(user_input) {
    let messageList = document.getElementsByClassName("conversation");
    let div = createDiv("bubble2", "user_box")
    div[0].innerHTML = user_input;
    div[1].appendChild(div[0]);
    messageList[0].prepend(div[1]);
}

function displayMap(coords) {
    let marker = new H.map.Marker(coords, { icon: icon });
    map.setCenter(coords);
    map.setZoom(14);
    map.addObject(marker);
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

function rezUserInput() {
    let rez = document.getElementById("user_input");
    rez.value = ""
}
