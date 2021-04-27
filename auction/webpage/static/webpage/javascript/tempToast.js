const tempToastContainer = document.querySelector("#tempToast")
const tempToastMsg = tempToastContainer.querySelector("#toastMessage")
const tempToast = new bootstrap.Toast(
    tempToastContainer.querySelectorAll(".toast")[0]
)
const notificationSound = new Audio(
    "/static/webpage/audio/iphone_notification.mp3"
)

function tempNotify(msg) {
    tempToastMsg.innerHTML = msg
    notificationSound.play()
    tempToast.show()
}
