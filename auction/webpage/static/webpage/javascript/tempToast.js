const tempToastContainer = document.querySelector("#tempToast")
const tempToastMsg = tempToastContainer.querySelector("#toastMessage")
const tempToastHeader = tempToastContainer.querySelector("#toastHeader")
const tempToast = new bootstrap.Toast(
    tempToastContainer.querySelectorAll(".toast")[0]
)
const notificationSound = new Audio(
    "/static/webpage/audio/iphone_notification.mp3"
)
var prevType

function tempNotify(msg, type) {
    tempToastMsg.innerHTML = msg

    if (typeof prevType == "string") {
        tempToastHeader.classList.remove(prevType)
    }

    tempToastHeader.classList.add(type)
    prevType = type
    var notificationSound = new Audio("/static/webpage/audio/" + type + ".mp3")
    notificationSound.play()
    tempToast.show()
}
