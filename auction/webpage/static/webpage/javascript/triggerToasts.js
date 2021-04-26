const toastElList = [].slice.call(document.querySelectorAll(".toast"))
const toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})

for (let i = 0, len = toastList.length; i < len; i++) {
    toastList[i].show()
}
