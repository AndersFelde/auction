const url = window.location.href.split("/")

if (url[url.length - 1] == "") {
    url.push("index")
}
const itemId = url[url.length - 1]

const notifyChatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/notify/" + itemId + "?"
)

console.log(itemId)

notifyChatSocket.onclose = function () {
    console.error("Chat socket closed unexpectedly")
}

notifyChatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    if (itemId != data.itemId) {
        console.log(data)
        tempNotify(data.msg)
    }
}
