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

function displayMessage(classname1, classname2, message) {
    let messageList = document.getElementsByClassName("conversation");
    let newDiv = document.createElement("div");
    let newDiv2 = document.createElement("div");
    newDiv.className = classname1;
    newDiv2.className = classname2;
    newDiv.innerHTML = message;
    newDiv2.appendChild(newDiv);
    messageList[0].prepend(newDiv2);
}

function displayMap(coords, apikey) {
    displayMessage("map_container", "grandpy_box", "")
    
    //Initialize the Platform object:
    var platform = new H.service.Platform({
        'apikey': apikey
    });
    // Get the default map types from the Platform object:
    var maptypes = platform.createDefaultLayers();
    // Instantiate the map:
    var map = new H.Map(
        document.querySelector('.map_container'),
        maptypes.vector.normal.map,
        coords = coords,
        );

    var icon = new H.map.Icon("static/img/mapmarker.png");
    // Create the default UI:
    var ui = H.ui.UI.createDefault(map, maptypes, 'fr-FR');
    let marker = new H.map.Marker(coords, { icon: icon });
    map.setCenter(coords);
    map.setZoom(14);
    map.addObject(marker);
}

function displayBadInput(response) {
    let user_input = document.getElementById("user_input").value;
    displayMessage("bubble2", "user_box", user_input)
    displayMessage("bubble", "grandpy_box","🤖👴" + response["grandpy_error"])
}

function displayGoodInput(response) {
    let user_input = document.getElementById("user_input").value;
    let lat = response["lat"]
    let lng = response["lng"]
    let apikey = response["apikey"]
    let coords = {lat, lng}
    displayMessage("bubble2", "user_box", user_input)
    displayMessage("bubble", "grandpy_box",
        "🤖👴" + response["grandpy_address"] + response["address"])
    displayMap(coords, apikey)
    displayMessage("bubble", "grandpy_box",
        "🤖👴" + response["grandpy_descript"] + response["descriptif"])
}

function rezUserInput() {
    let rez = document.getElementById("user_input");
    rez.value = ""
}
