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

const verifyBidButton = document.querySelector("#verifyBidButton")
const verifyModal = new bootstrap.Modal(
    document.querySelector("#verifyModal"),
    { backdrop: "static" }
)
const modalNextBid = document.querySelector("#modalNextBid")

function isInteger(value) {
    return /^\d+$/.test(value)
}

function updateBid(value) {
    bidInput.value = value
    modalNextBid.innerHTML = value
}

verifyBidButton.onclick = function () {
    verifyModal.show()
}

submitBidButton.onclick = function () {
    submitBid(bidInput.value)
}

plussBidButton.onclick = function () {
    updateBid(parseInt(bidInput.value) + increase)
}

minusBidButton.onclick = function () {
    updateBid(parseInt(bidInput.value) - increase)
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    console.log(data)
    if (data.bid) {
        bidSpan.innerHTML = data.bid + " NOK"
        updateBid(parseInt(data.bid) + increase)
        if (data.user) {
            tempNotify("Du la inn bud på: " + data.bid + ",-", "bid")
            bidSpan.innerHTML += " (du)"
        } else {
            tempNotify("Nytt bud på: " + data.bid + ",-", "bid")
        }
    } else {
        if (data.invalid == true) {
            window.location.href = "/logIn"
            return
        }

        tempNotify(data.msg, "error")
        updateBid(parseInt(bidSpan.innerHTML) + increase)
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

const timeSpan = document.querySelector("#time")
var time = timeSpan.innerHTML
var expireTime = new Date(time).getTime()

// Update the count down every 1 second
var x = setInterval(function () {
    // Get today's date and time
    var now = new Date().getTime()

    // Find the distance between now and the count down date
    var distance = expireTime - now

    // Time calculations for days, hours, minutes and seconds
    const timePrefix = ["d", "h", "m", "s"]
    var time = []
    // [days, hours, minutes, seconds]
    time.push(Math.floor(distance / (1000 * 60 * 60 * 24)))
    time.push(Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)))
    time.push(Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)))
    time.push(Math.floor((distance % (1000 * 60)) / 1000))

    time = time.map((time, index) => {
        if (time == 0) {
            return ""
        }
        return String(time) + timePrefix[index] + " "
    })

    // Display the result in the element with id="demo"
    timeSpan.innerHTML = time.join("")

    // If the count down is finished, write some text
    if (distance < 0) {
        clearInterval(x)
        timeSpan.innerHTML = "Ferdig"
    }
}, 1000)

// function updateTime(newTime) {}
