function handleNotification(data) {
    const itemDiv = document.querySelectorAll(".item-" + data.itemId)[0]
    const bidPrefixSpan = itemDiv.querySelector("#bidPrefix")
    bidPrefixSpan.innerHTML = ""
}
