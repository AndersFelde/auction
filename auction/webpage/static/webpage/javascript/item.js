const roomName = JSON.parse(document.getElementById("itemId").textContent)

const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/bid/" + roomName + "/"
)

const bidInput = document.querySelector("#bidInput")
const bidSpan = document.querySelector("#bidSpan")
const priceSpan = document.querySelector("#priceSpan")
const increase = parseInt(priceSpan.innerHTML) * 0.1

const plussBidButton = document.querySelector("#plussBidButton")
const minusBidButton = document.querySelector("#minusBidButton")
const submitBidButton = document.querySelector("#submitBid")

function isInteger(value) {
    return /^\d+$/.test(value)
}
submitBidButton.onclick = function () {
    submitBid(bidInput.value)
}

plussBidButton.onclick = function () {
    bidInput.value = parseInt(bidInput.value) + increase
}

minusBidButton.onclick = function () {
    bidInput.value = parseInt(bidInput.value) - increase
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    console.log(data)
    if (data.bid) {
        bidSpan.innerHTML = data.bid
        bidInput.value = parseInt(data.bid) + increase
    } else {
        alert("Fuck off")
        bidInput.value = parseInt(bidSpan.innerHTML) + increase
    }
}

chatSocket.onclose = function () {
    console.error("Chat socket closed unexpectedly")
}

function submitBid(value) {
    if (isInteger(value) == false) {
        alert("Fuck off")
        return
    }

    chatSocket.send(
        JSON.stringify({
            bid: value,
        })
    )
}

bidInput.onkeyup = function (e) {
    if (e.keyCode === 13) {
        submitBid(bidInput.value)
    }
}
