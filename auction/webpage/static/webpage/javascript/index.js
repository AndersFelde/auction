$(".item-clickable").click(function () {
    console.log($(this).children(".item-id")[0].value)
    window.location.pathname = "/item/" + $(this).children(".item-id")[0].value
    // var roomName = document.querySelector("#room-name-input").value
    // window.location.pathname = "/room/" + roomName
})
