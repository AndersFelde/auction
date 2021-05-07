// $(".notifi-card").click(function () {
//     window.location.href = $(this).find("#item-link")[0].href
// })

const readAllNotifiBtn = document.querySelector("#readAllNotifiBtn")
const notificationCards = document.getElementById("notificationCards")

readAllNotifiBtn.onclick = function () {
    notifyChatSocket.send(
        JSON.stringify({
            id: true,
        })
    )

    var itemDivs = notificationCards.querySelectorAll(".border-primary")
    itemDivs.forEach((el) => {
        unmarkNotification(el)
    })
}

function readNotification(itemId) {
    notifyChatSocket.send(
        JSON.stringify({
            id: itemId,
        })
    )

    var itemDiv = notificationCards.querySelectorAll(".notifi-" + itemId)[0]
    console.log(itemDiv)
    unmarkNotification(itemDiv)
}

function unmarkNotification(el) {
    el.classList.remove("border-primary")
    header = el.querySelector("#classHeader")
    header.classList.remove("text-primary")
    header.innerHTML = "New bid"
}
