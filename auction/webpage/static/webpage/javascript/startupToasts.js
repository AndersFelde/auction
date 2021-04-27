const toastContainer = document.querySelector("#startupToasts")
const toastElList = [].slice.call(toastContainer.querySelectorAll(".toast"))
const toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})

for (let i = 0, len = toastList.length; i < len; i++) {
    toastList[i].show()
}
