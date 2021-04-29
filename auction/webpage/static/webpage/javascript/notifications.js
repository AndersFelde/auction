const url = window.location.href.split("/")

if (url[url.length - 1] == "") {
    url.push("index")
}
const itemId = url[url.length - 1]

const notifyChatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/notify/" + itemId
)

notifyChatSocket.onclose = function () {
    console.error("Chat socket closed unexpectedly")
}

notifyChatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    tempNotify(data.msg)

    console.log(data)
    const itemDiv = document.querySelector("#item-" + data.itemId)
    const bidSpan = itemDiv.querySelector("#bidSpan")
    bidSpan.innerHTML = data.bid
}
