function handleNotification(data) {
    const itemDiv = document.querySelectorAll(".item-" + data.itemId)[0]
    const bidPrefixSpan = itemDiv.querySelector("#bidPrefix")
    bidPrefixSpan.innerHTML = ""
}

$(".bid-card").click(function () {
    window.location.href = $(this).find("#item-link")[0].href
})
