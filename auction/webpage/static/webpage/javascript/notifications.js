const url = window.location.href.split("/")

if (url[url.length - 1] == "") {
    url.push("index")
}
const itemId = url[url.length - 1]

const notifyChatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/notify/" + itemId
)

const notifiNavSpanList = document.querySelectorAll(".notifiNav")

var notifications

notifyChatSocket.onopen = function () {
    console.log("joe")
    notifyChatSocket.send(
        JSON.stringify({
            type: "getNotifications",
        })
    )
}

notifyChatSocket.onclose = function () {
    console.error("Chat socket closed unexpectedly")
}

notifyChatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    if (data.msg) {
        tempNotify(data.msg, "bid")

        if (typeof handleNotification === "function") {
            handleNotification(data)
        }
        // if (itemId == "index") {
        //     const itemDiv = document.querySelector("#item-" + data.itemId)
        //     const bidSpan = itemDiv.querySelector("#bidSpan")
        //     bidSpan.innerHTML = data.bid + " NOK"
        // } else if (itemId == "myBids") {
        //     const itemDiv = document.querySelectorAll(".item-" + data.itemId)[0]
        //     const bidPrefixSpan = itemDiv.querySelector("#bidPrefix")
        //     bidPrefixSpan.innerHTML = ""
        // }

        updateNotifications(notifications + 1)
    } else {
        updateNotifications(data.count)
    }
}

function updateNotifications(number) {
    if (number > 0) {
        notifiNavSpanList.forEach((el) => {
            el.innerHTML = "(" + number + ")"
        })
    }
    notifications = number
}
